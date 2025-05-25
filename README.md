**Kerbal Space Program Savegame Transfer Guide**
=============================================

**Introduction**
---------------

This guide provides step-by-step instructions on how to transfer Kerbal Space Program (KSP) savegames from an Xbox to a PC. The process involves using a C# compiler, a Python script, and a cloud save manager.

**Requirements**
---------------

* A C# compiler (e.g., Visual Studio Community)
* The xbcsmgr repository (for Xbox savegame management)
* Python for CMD (with pip install plugin)
* The `dissect.cstruct` package (install via pip)

**Step 1: Download and Install Required Components**
------------------------------------------------

1. **Visual Studio Community**: Download and install Visual Studio Community. Select the `.NET desktop development` workload and the following individual components:
	* C# and Visual Basic Roslyn Compilers
	* C# and Visual Basic
	* .NET 7.0 Runtime (out of support)
2. **xbcsmgr**: Clone the xbcsmgr repository from GitHub.
3. **Python for CMD**: Install Python for CMD from the Microsoft Store.
4. **pip install**: Install the `dissect.cstruct` package via pip: `pip install dissect.cstruct`

**Step 2: Download Savegames from Xbox**
--------------------------------------

1. **Ensure KSP saves are backed up**: Run KSP on Xbox and ensure that your saves are backed up to the Xbox Network.
2. **Run xbcsmgr**: Open Visual Studio, clone the xbcsmgr repository, and run the application.
3. **Download savegames**: Select your Xbox account, find KSP in the list of games, and download the compressed savegame files (pseudo-folder-files).

**Step 3: Prepare and Run Python Script**
--------------------------------------

1. **Download Python extractor**: Download the Python extractor script from this repository.
2. **Create output folders**: Create folders for each savegame/pseudo-folder-file with the same name as the gibberish filename.
3. **Run Python script**: Use the command `python [path to extractor] [path to input file] [path to output folder]` to extract the savegame files.

**Step 4: Transfer Savegames to PC**
----------------------------------

1. **Copy output folders**: Copy the extracted savegame folders to the KSP saves directory on your PC.
2. **Rename folders (optional)**: Rename the folders to their correct names using the in-game load saved games menu.

**Troubleshooting**
-----------------

* **Exception thrown: value cannot be null**: Log in to the Xbox app with an Xbox account/MS account with an Xbox profile.
* **XboxCsMgr.XboxLive.Exceptions.XboxAuthException: '400: Bad Request'**: Same as previous.
* **Pip errors**: Install pip manually or update to the latest version.

**Credits**
----------

* **tuxuser**: Programming, reverse engineering, and manipulating savefiles.
* **Me**: Documentation and puzzle piece assembly.
* **Billynothingelse**: Save transferer program.
* **JonnyOThan**: Help with savefile questions.

**Examples**
------------

* **Example 1**: `python "C:\Users\JohnDoe\Desktop\python extractor\extract.py" C:\Users\JohnDoe\Desktop\xbcsmgrfiles\gibberishname C:\Users\JohnDoe\Desktop\outputkspsavegames\gibberishname1\`
