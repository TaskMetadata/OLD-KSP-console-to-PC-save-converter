# Requirements and instructions
## Requirements:

1. A C# compiler. I’ll be using [Visual Studio community](https://www.visualstudio.microsoft.com), as it’s simple and works in my case. Installation instructions (for the required components) are provided within the main instructions.

2. If you're on Xbox, this [repo (xbcsmgr)](https://www.github.com/billynothingelse/xbcsmgr). It is a cloud save manager for the Xbox Network. It downloads raw save files from the cloud.

3. The Python script included in this repo. It converts/extracts the compressed console savefiles to PC readable ones. On this page, I sometimes refer to it as an ‘extractor’ or ‘python extractor’.

4. Python for CMD. By extension, you’ll need the ‘pip install’ plugin, so you can download the package ‘dissect.cstruct’. All 3 are required. Installation instructions for all 3 are provided within the main instructions.


## Important notes:

A demo video: https://youtu.be/Ul6BC5hLKJs

1. I use ‘savegame’ to refer to the options seen on the ‘load game’ menu on the main menu. I use ‘quicksaves’ to refer to the options seen in the ‘load’ menu on the pause menu while in a savegame.

2. As far as I know, no major data is lost when converting, but I haven’t had much time to test it. Will update this page when I get the chance to check it all.

3. I’ve written this page for use with a Windows computer and an Xbox. 
This should still work on Mac and Linux, albeit some instructions might be wrong (e.g. there is no Microsoft Store on Mac or Linux). Use equivalent methods for them.\
***As for Playstation*** – The Playstation edition is very similar to the Xbox edition, if not identical, and their save structures are the same. Therefore, the .py extractor on this page can be used on their files too. However, you'll need another way to actually get the save files off the console; this page only has instructions for downloading the saves off of Xboxes (steps 1-3). I've heard that the PS4 can download savefiles onto USB, and apparently there is a subscription service for Playstation 5 that allows uploading savefiles to the cloud. Sometime soon, I’ll confirm which methods work. Therefore, steps 1 to 3 are for Xbox only (as they are instructions to download the saves from an Xbox) but I still *highly recommend* reading step 3, as it includes info that is seen in the Playstation version too. Steps 4 and 5 apply to both consoles - once you have obtained the save files from a playstation, you may proceed to step 3/4. Do also note that I may mention Xbox buttons or Xbox saves, but generally you can replace it with an equivalent process or word for Playstation.


## Instructions:

(sorry for the excessive length. Majority of it is explanation and additional information)

1. Your KSP saves should be backed up to the Xbox Network. That is, ensure you’ve been online while running the game, perhaps leave it running for a little while with a savegame loaded to make sure it has backed up the latest saves.
2. Installing the C# compiler: First, [download Visual Studio](https://www.visualstudio.microsoft.com). Once you run the installer: when prompted, select the workload of `.NET desktop development`, then go to the ‘individual components’ tab and select the following: `C# and Visual Basic Roslyn Compilers`; `C# and Visual Basic`; and `.NET 7.0 Runtime (out of support)`. Make sure you are installing .NET 7.0 as well as the default others. You can deselect all of the 'optional' packages under `.NET desktop development` in the right-hand list. Install the selected components.
3. Preparing xbcsmgr: Next, go to the Github page for [xbcsmgr](https://www.github.com/billynothingelse/xbcsmgr), click the green `code` button, and then copy the clone link there. Open Visual Studio - it should bring you to a homescreen with ‘get started’; click the `Clone a repository` button, and paste the Github clone link in the `repository location`. The path is not important. Once that’s done, you should be looking at a window that has a green play button at the top, with the text `XboxCsMgr.Client`. that button will start the application. The output box will come up with a lot of text; that is normal.
4. Running xbcsmgr: Note that xbcsmgr pulls any Xbox save data that is associated with the logged in *Xbox* account. That is, not the Microsoft Store account, not the logged-in windows account, but the account that is logged in on the PC Xbox app. At least, that’s how I get it to work. You should now have a white box with a list of your played games on the left. Scroll down on this list until you find KSP. Click on it. If the app crashes, that’s fine, click the stop/reload button and reopen it. After clicking it, a folder should appear on the right. Click the triangle next to it, which should reveal a bunch of files. These are all compressed folders, and each one corresponds to a savegame. I call them pseudo-folder-files. You’ll need to download each of these pseudo-folder-files by right-clicking on them and clicking download. The names of the pseudo-folder-files themselves will be gibberish (except ‘common’, which contains scenario and tutorial saves). The python decompressor in this repo that we’ll use later does not repair the filenames. In-game, though, the savegames will have their correct names. You'll be able to rename those folders at the end. If you’d like, you can verify that you have downloaded all the files by comparing the size in MB of all of the files you downloaded added together, with the reported size of your user’s save data for the game on Xbox (hamburger button on the game>manage game and addons>save data> check the listed save data for your user).
5. Preparing python: We’ll now install the Python-related programs. First, we’ll need to install Python for command prompt. In the Microsoft Store, search for ‘Python’ and select the newest one (although any should work). Install that. You’ll need the pip installer package for Python, too, but installing Python via the MS store should’ve installed it automatically. We’ll be using pip to install ‘dissect.cstruct’ which is a required package for this blob extractor. Once python has finished downloading, open command prompt (press Win+R and type `cmd`). Type in `pip install dissect.cstruct`. This should install dissect.cstruct; confirm that by checking for the message ‘Successfully installed dissect.cstruct’.
6. Running the python extractor: Finally, We’ll prepare for and run the Python script that converts the savegame pseudo-folder-files into folders & files. Download the python extractor (the .py file) from this repo into an empty folder by clicking on it at the top of the page and clicking the download button on the righthand side. Also in that same folder, create more folders, naming them for each savegame/pseudo-folder-files we’ll be extracting – for now, use the same names as the gibberish names of the pseudo-folder-files, so we know which pseudo-folder-file was extracted where. Later, you’ll be able to check the correct name of the savegame and rename the folder for it.\
The syntax (in cmd) for the extractor (the .py file) is `python [path to the extractor] [path to the input file] [path to the output folder]` without the square brackets. The extractor takes one of the input pseudo-folder-files downloaded from xbcsmgr, and extracts it into an output folder. See example #1 in [the examples section](#Examples-see-hashtags-above) for an example. Note that the extractor can only do one savegame/pseudo-folder-file at a time.

This should now have extracted compressed pseudo-folder-files, into blobs of files and then decompressed them. The output folders (i.e. the ones you created and named with the gibberish names) are the folders you can put into the saves directory in the game. The game's 'load saved games' menu also doesn't show the correct names, but the in-game ( when you've loaded a savegame/quicksave) menu does, on the top bar of the menu. Therefore, you can put one folder in at a time, launch the game, load one of the (concurrently gibberish-named) savegames, see the correct name in the in-game menu, and rename the savegame on the 'load saved games' menu and the savegame folder. This is optional, however.


# Credits

- Massive thanks to [tuxuser](https://www.github.com/tuxuser) - he did all of the programming, reverse engineering, everything to do with manipulating the savefiles to make them readable. He did the decompression, the blob extraction (unpacking), the compiling, the decompiling, the algorithm analysis, the encryption-related-documentation reading, the assembly.. a lot. Thanks, man!!
- Me - I wrote the documentation, and put a few puzzle pieces together regarding how to take the savefiles off an Xbox and how to interpret them.
- [Billynothingelse](https://www.github.com/billynothingelse) - for having created the save transferer program that would end up being my holy grail, after I struggled to find any method that worked.
- JonnyOThan, over on discord - helped with some questions I had about the savefiles.
- Everyone who said this was impossible - You awakened the stubbornness in me, and made me pursue this further.
- Everyone else who uses this - I hope this helps you, and you do something fun/cool with it.

# Faq/common errors, and bugs
## xbcsmgr/Visual Studio:
- **“Exception thrown: value cannot be null” for “var xblcredentials”:** Need to log into the Xbox app with an Xbox account/MS account with an Xbox profile.
- **“XboxCsMgr.XboxLive.Exceptions.XboxAuthException: '400: Bad Request'”:** Same as previous.
- **Other Xbox-live-related errors:** Possible situations:
  - Account isn't logged in. Confirm you are logged into the Xbox app with the MS/Xbox account that the KSP saves are under. I don't think you need to have that account linked to windows.
  - Xbox app is corrupt. Reinstall it, or repair it (either through the xbox app, or through windows settings).

## Python:
- **Pip:**
  - If you get an error related to pip not being found or recognised, you’ll probably need to install pip manually; you can find instructions for that online.
  - It may tell you that there's a newer version; there shouldn't be any need to update.
- **dissect.cstruct:**
  - if you get an error about dissect.cstruct not installing properly, you've most likely corrupted something, or its unable to find the installation path, or it doesn't have an internet connection. Try rectifying those. If you still have issues, let me know.
  - **".... not on PATH":** Not a problem. It should still work.

- **“Errno 2: no such file or directory”:** Ensure you include the ‘.py’ extension in the filename for the extractor path.

## Generic Visual Studio:
- **nuget vulnerability/bouncy castle cryptography vulnerability:** Doesn't really affect a project like this.

## Bugs:
- The 'common' pseudo-folder-file (which includes scenario saves and tutorial saves) doesn't work straight up - I've been extremely busy and haven't had much time at all to test anything.

- Need to test and fix DLC part names' mismatches

Both of those should hopefully be fixed within july

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
