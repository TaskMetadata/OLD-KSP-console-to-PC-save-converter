# Requirements and instructions
## Requirements:

1. The dotnet compiler. I’ll be using [Visual Studio community](https://www.visualstudio.microsoft.com), as it’s simple and works in my case.

2.The xbox cloud save from [repo (xbcsmgr)](https://www.github.com/billynothingelse/xbcsmgr).

3. This gthub repo code downloaded on your computer
   
4. Python 3.9+

## Instructions:

(sorry for the excessive length. Majority of it is explanation and additional information)

1. Your KSP saves should be backed up to the Xbox Network. That is, ensure you’ve been online while running the game, perhaps leave it running for a little while with a savegame loaded to make sure it has backed up the latest saves.

2. Download xbcsmgr from GitHub. If using visule studio 2022 make sure you have the c# desktop option checked in the installer if not [Getting Started](https://learn.microsoft.com/en-us/visualstudio/get-started/csharp/?view=vs-2022), Click the green play button in the top center of the screen. If using dotnet cli cd in to the xbcsmgr and run dotnet run
   
3. Note that xbcsmgr pulls any Xbox save data that is associated with the logged in *Xbox* account. That is, not the Microsoft Store account, not the logged-in windows account, but the account that is logged in on the PC Xbox app. At least, that’s how I get it to work. You should now have a white box with a list of your played games on the left. Scroll down on this list until you find KSP. Click on it. If the app crashes, that’s fine, click the stop/reload button and reopen it. After clicking it, a folder should appear on the right. Click the triangle next to it, which should reveal a bunch of files. These are all compressed folders, and each one corresponds to a savegame. I call them pseudo-folder-files. You’ll need to download each of these pseudo-folder-files by right-clicking on them and clicking download. The names of the pseudo-folder-files themselves will be gibberish (except ‘common’, which contains scenario saves). The python decompressor in this repo that we’ll use later does not repair the filenames. In-game, though, the savegames will have their correct names. You'll be able to rename those folders at the end. If you’d like, you can verify that you have downloaded all the files by comparing the size in MB of all of the files you downloaded added together, with the reported size of your user’s save data for the game on Xbox (hamburger button on the game>manage game and addons>save data> check the listed save data for your user).

5. With the save data extracted you can know open you terminal ( Windows terminal for windows ) you will first need to install dissect.cstruct with pip ```bash pip install dissect.cstruct ``` 

6. Now with the packages installed we can know run the extract.py file from this repo. Make sure the terminal path is located where you downloaded this repo. Then you can run ```bash python ./extracter.py [path to the input file] [path to the output folder]``` for example ```bash python “C:\Users\JohnDoe\Desktop\python extractor\extract.py” C:\Users\JohnDoe\Desktop\xbcsmgrfiles\gameSave C:\Users\JohnDoe\Desktop\outputkspsavegames\gameSave ```

# Credits

- Massive thanks to [tuxuser](https://www.github.com/tuxuser) - he did all of the programming, reverse engineering, everything to do with manipulating the savefiles to make them readable. He did the decompression, the blob extraction (unpacking), the compiling, the decompiling, the algorithm analysis, the encryption-related-documentation reading, the assembly.. a lot. Thanks, man!!
- Me - I wrote the documentation, and put a few puzzle pieces together regarding how to take the savefiles off an Xbox and how to interpret them.
- [Billynothingelse](https://www.github.com/billynothingelse) - for having created the save transferer program that would end up being my holy grail, after I struggled to find any method that worked.
- JonnyOThan, over on discord - helped with some questions I had about the savefiles.
- Everyone who said this was impossible - You awakened the stubbornness in me, and made me pursue this further.
- Everyone else who uses this - I hope this helps you, and you do something fun/cool with it.

# Faq/common errors:
## xbcsmgr/Visual Studio:
- **“Exception thrown: value cannot be null” for “var xblcredentials”:** Need to log into the Xbox app with an Xbox account/MS account with an Xbox profile.
- **“XboxCsMgr.XboxLive.Exceptions.XboxAuthException: '400: Bad Request'”:** Same as previous.
- **Other Xbox-live-related errors:** Possible situations:
  - Account isn't logged in. Confirm you are logged into the Xbox app with the MS/Xbox account that the KSP saves are under. I don't think you need to have that account linked to windows.
  - Xbox app is corrupt. Reinstall it, or repair it (either through the xbox app, or through windows settings)

# Examples (see hashtags above)

#1. If I had the python extractor with the path ‘C:\Users\JohnDoe\Desktop\python extractor\extract.py’, and had the input pseudo-folder-file from xbcsmgr with the path ‘C:\Users\JohnDoe\Desktop\xbcsmgrfiles\gibberishname’, and wanted to output it to a folder with the path ‘C:\Users\JohnDoe\Desktop\outputkspsavegames\gibberishname1\’, I would use the command ‘python “C:\Users\JohnDoe\Desktop\python extractor\extract.py” C:\Users\JohnDoe\Desktop\xbcsmgrfiles\gibberishname C:\Users\JohnDoe\Desktop\outputkspsavegames\gibberishname1\’ (the first path has quotation marks as it contains a space, otherwise cmd would treat the path as 2 separate terms).


# More info/backstory
I started playing KSP on the Xbox, and since I first started I immediately knew I’d rather play on PC. Especially as I have an Xbox One S, arguably underpowered even for a 10 year old game like KSP. ‘Optimised and enhanced for Xbox’ my ass!
In about October 2024, I started launching bigger ships and realised I really need to find a way to transfer my savefile to PC, because my Xbox wasn’t tolerating it at all.
I asked about whether it would be possible to transfer the savefile across on the KSP reddit’s discord. Everyone said it was impossible. 
Anyway… I’m too stubborn for anyone’s good, so I joined multiple Xbox modding scene servers, trying to gather information on how savefiles work (in terms of Xbox’s functions), how I could transfer it, and how the savefiles might work on KSP’s side.
Eventually, I met [tuxuser](https://www.github.com/tuxuser). I was entirely planning on figuring out transferring, encryption, and programming of the transfer application myself, but in the end Tuxuser did almost all of it (thanks again, man!)
Here’s what we looked at, in order:
Getting the files from the Xbox in the first place. I tried numerous methods, including taking the HDD out and connecting it via PC to decrypt it using various Github projects ( – which didn’t work: I first had a look at the partitions windows had discovered without any conversion program – of which there was only one that was readable by windows; I tried a conversion program by Github user ‘gitfurious’ and managed to get the python program running, but it would always fail and spit out an error… likely due to a lack of skills on my part; and tried one by user ‘brandonreynolds’ which I remember did error a few times when trying to launch it in visual studio… I don’t remember whether I got it working in the end – I think it did succeed in converting partitions into a windows-readable format, but the partitions/drives that were shown in file explorer afterwards were all of the same ones shown in ADV file explorer on Xbox – i.e. all of the partitions that are hidden in ADV were also missing here. I’m not sure whether this is due to a fault in the conversion, or that the partitions were still hidden somehow… perhaps those partitions are encrypted and either the converter or windows couldn’t read it. Anyhow, I then switched methods and tried a cloud save manager (xbcsmgr) which found the savefiles…

 … albeit it downloaded any and all files in raw form, with no file extensions. The savefiles could be opened via text/hex editors only, and it was mostly garbled Unicode with a bit of plaintext mixed in. I then confirmed that the files were fully intact and readable – I downloaded (via xbcsmgr) a Minecraft: Xbox One Edition savefile, which had a file in it that, when opened in a text editor (notepad :) ), showed some plaintext, including the letters ‘.jpg’. I added .jpg onto the end of file name and voila, it worked, a functioning image. I presume this plaintext, which is also present in the KSP files, must be a file header or metadata or something along those lines.
 
I took a look at the KSP savefiles again. We determined that the files that xbcsmgr downloaded[a] (in my case, there were 2 files with gibberish 26 letter words as filenames, which I later determined were the 2 savegames I had; and 1 file with the name ‘common’, which I later determined to contain the scenario savegames, and possibly other things) were actually folders containing files in them, as these pseudo-folder files[a] (which mostly contained gibberish Unicode) contained multiple small sections of plaintext that appeared to be strings of filenames and extensions, which we presumed were the headers for the files in these pseudo-folder files. It made more sense this way, anyway, as that’s how the savegames files are stored on PC – in folders, also laid out in that way.

Tux (and separately, a discord user, JonnyOThan, but I forgot to tell Tux so he eventually figured it out on his own :sweat_smile: ) noticed that there were repeating patterns in the pseudo-folder-files, that there were many headers and accompanying data. He determined that these were the actual files and folder structures we want, and called each of them blobs. He wrote a python program to extract the blobs out of the pseudo-folder-files. This yielded a lot of smaller files and folders, with correct filenames, and seemingly correct file extensions… except that they were compressed, with a ‘.cmp’ file extension after the correct one in the filename. We had extracted all the files from the pseudo-folder-files into their correct layout as per the PC version of the game, but they were compressed.

Tux set out to figure out what compression was being used. He took a quick look at the blobs, and considered LZMA compression after realising that the file headers have specific features that are seen in headers formed by LZMA compression. He then checked out a PS4 dump of the game, which had a file named ‘tempsavemanager.prx’; that lead him to consider and try to match up the blobs with XML identifier lookup table compression, but then found a function named ‘LzmaDecompress’ in the .prx file so went back to trying LZMA. He tried recreating the decompression algorithm to no avail, and tried various unpackers, also to no avail. Finally, he discovered that LZMA can have an extra parameter called ‘FORMAT_RAW’, and manually assembled the LZMA ‘filter chain’ through trial and error; and putting this all together into a homemade decompressor finally returned plaintext data for all the files.
