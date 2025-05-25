"""
Extracts individual files from KSP Xbox Savegame blobs
"""

import io
import os
import argparse
import pathlib
import struct
import lzma

from dissect import cstruct

TYPES = cstruct.cstruct()
TYPES.load("""
struct KSP_BLOB_ENTRY {
  UINT EntryLen;
  BYTE Padding;
  BYTE FilenameLen;
  BYTE Padding2;
  BYTE LastFileMarker;
  CHAR Filename[FilenameLen];
  BYTE Data[EntryLen];
};
""")

def read_u32(data: bytes, offset: int) -> int:
    return struct.unpack("<I", data[offset:offset+4])[0]

def decompress(data: bytes) -> bytes:
    context = lzma.LZMADecompressor(
        format=lzma.FORMAT_RAW,
        filters=[
            {"id": lzma.FILTER_LZMA1},
        ]
    )
    return context.decompress(data)

def extract_file(inputfile: io.BufferedReader, outputdir: pathlib.Path, dryrun: bool) -> None:
    inputfile.seek(0, os.SEEK_END)
    total_filesize = inputfile.tell()
    inputfile.seek(0, os.SEEK_SET)

    while True:
        parsed = TYPES.KSP_BLOB_ENTRY(inputfile)

        # Did we reach EOF yet?
        if parsed.LastFileMarker:
            assert parsed.Filename == b""
            assert inputfile.tell() == total_filesize
            break

        # Strip leading "\" of filename and null terminator
        filename = parsed.Filename.decode('utf-8').strip()[1:-1]

        compressed = False
        if filename.endswith(".cmp"):
            compressed = True
            filename = filename[:-4]

        target_filepath = outputdir.joinpath(pathlib.PureWindowsPath(filename))

        if not target_filepath.parent.exists() and not dryrun:
            target_filepath.parent.mkdir(parents=True, exist_ok=True)
        
        if not dryrun:
            compressed_data = parsed.Data.dumps()

            if compressed:
                compressed_length = len(compressed_data)
                uncompressed_length = read_u32(compressed_data, 5)

                print(f"{target_filepath} ({compressed_length=:X} {uncompressed_length=:X})")

                without_header = compressed_data[9:]
                data = decompress(without_header)

                assert len(data) == uncompressed_length, "Mismatch of decompressed data size"
            else:
                data = compressed_data

            with io.open(target_filepath, "wb") as f:
                f.write(data)
        else:
            print(target_filepath)

def main() -> None:
    parser = argparse.ArgumentParser("KSP Savegame blob extractor")
    parser.add_argument("inputfile", help="Input file", type=argparse.FileType('rb'))
    parser.add_argument("outputdir", help="Output directory")
    parser.add_argument("--dry", action="store_true", help="Dry-Run (no extraction, no folder/file creation)")
    args = parser.parse_args()

    extract_file(args.inputfile, pathlib.Path(args.outputdir), args.dry)

if __name__ == '__main__':
    main()
