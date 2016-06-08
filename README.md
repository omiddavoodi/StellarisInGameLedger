# StellarisInGameLedger

This is a ledger mod and its associated out of game scripts for Paradox Interactive's startegy game "Stellaris".

The associated scripts located in the "server" directory are released under MIT license. Other files found in the "mod" directory are for public domain.

# What is InGameLedger?

InGameLedger is a mod for Paradox Interactive's "Stellaris" that implements a simple in-game ledger that presents a range of important measures of the empires in the current playthrough. For each of the playthrough's empires, these measures are:
* Military Power
* Number of Colonized Planets
* Number of Planets Under Control
* Number of Subject Empires
* Current Energy Credits
* Net Energy Income
* Current Minerals
* Net Mineral Income
* Current Influence
* Net Influence Income

In addition to these measures, it calculates a rudimentary weighted score that some players might find useful.

# How can I use it?

To use the mod, you should first download the latest version from here and extract it. It consists of two parts, a typical Stellaris mod, located in the "mod" directory, and a python script located in the "server" directory.

You should copy the contents of the "mod" directory into Stellaris' mod directory. For Windows users, it can be found in "MyDocument/ParadoxInteractive/Stellaris/mod"

Before you can use the mod, you should install Python 3. Python3 can be downloaded for free from here: https://www.python.org/downloads/release/python-351/

After you have installed Python3, you should configure the mod so that it can find your "save game" directory.
At first, find somewhere suitable for the mod's "server" directory on your computer. Inside this folder, there should be a python script called "start.py".

Easy way on Windows (And most versions of Linux with a decent GUI):
* Go to "MyDocument/ParadoxInteractive/Stellaris/" or your respective Stellaris directory.
* Drag "save games" onto "start.py". You should see the prompt: "Path successfully configured."
* If everything goes well, a new file called "path.txt" should be created in the same directory as "start.py".

Harder way:
* Create a file called "path.txt" in the same directory as that of "start.py"
* Open it with the text editor of your choice
* Copy/Paste or simply type the address of your Stellaris "save games" directory here.

Before you launch the game, run "start.py". If you are on Linux, make sure you have the right permissions. Remember that you can only run it with Python3.

If you have done everything right, you should see the prompt "Server Starts - localhost:12852".

---DO NOT CLOSE THIS, LAUNCH THE GAME---

After you are inside your game, do a new save. Then, click on the "Help" button on the bottom right corner of the screen. This should normally send you to the Wiki. Now, click on the first button on the top of the help dialog. Wait a little. Your should now be able to see your game's ledger.

# Important Notes

* The ledger DOES NOT show the game's "most recent" information. It extracts the information from your "LATEST SAVE". This means that if you load an old save and immediately hit the ledger button, it will show the stats of your LAST SAVED GAME BEFORE YOU LOADED THIS ONE.
* It actually can't show the ledger for Ironman games.
* It is better to make the game autosave monthly, so that the oldest ledger you get will be from last month.
* If you want to see the ledger for the game's current time, just do a save. The ledger will always show the latest save.
* Economic statistics are actually always for the previous month. So for example, there CAN be diffrences between you current net energy income and the one you see in the ledger.
* It takes some time for the ledger to show each time. This is because right now, the algorithm that parses the save is quite inefficient. I'm working on improving its speed right now.

# It doesn't Work!!

This mod is still under development and there are certainly going to be bugs and problems. But before you contact me about it read these, because they might solve your problem. If they didn't, fell free to contact me for bug report.

I can't configure the mod: Are you sure you have Python (As I said above, you should install it)? Are you sure you have Python3? Do your enviroment variables contain python3? Are your sure it is being run with Python3? Are you actually sure that it isn't configured? (If you are on linux, Are you sure you have the right permission?)

I can't run "start.py". It says "Error: Save directory path not set": You haven't (successfully?) configured the mod.

I can't run "start.py" at all. It closes the moment it is started: Check that you are running it with Python3, that you have the right permissions (Linux users), and that TCP Port 12852 is free on your computer.

I can't find the ledger button: Are you sure that you have installed the "mod" part correctly? Are you sure that You have activated the mod? Are you sure you don't have another mod that adds more buttons to the in-game browser?

Stellaris Launcher says the mod is out of date: Although the launcher will say that, it doesn't mean that it won't run. You can still launch the game and check it for yourself. As the mod part is pretty light, I doubt it will really cause any problems, even if it isn't tested on newer versions of the game.

I found the ledger button and clicked on it, but nothing happens: Do other buttons work? Is SteamOverlay enabled? Do you see the Wiki? Is the game geniune and activated on steam?

I found the ledger button and clicked on it, but it shows an error page: Have you run "start.py" successfully? Did it show "Server Starts - localhost:12852"? Is it still running?

The ledger is showing inaccurate information: Is it by any chance, showing an incorrect economy related statistics? If so, read the "Important Notes" section above.

# FAQ

**How does it actually work?**

The game has a browser integrated into it. I'm reading the save files and extracting relevant information from them, turning them into an html page and serving them inside your own computer. The ledger button just makes the ingame browser show the address "localhost:12852".



**Why does it show outdated economy information?**

Right now, there is no "easy" way to extract that data from the save. That information is simply not cached and trying to calculate them will make the code even slower.



**I can help with something, do you need help?**

Yes! I need help in several fields:
* The current ledger UI is pretty ugly. Can you design something good and elegant?
* The current ledger button is even uglier. Can you design a good one?
* My knowledge of the save's gamestate is quite limited. Can you help me with it so this can extract more information from the save?
* My knowledge of modding in general isn't high. All the other mods I made were personal and not intended for public release. Can you help me make a proper and polished mod?

If you can, and want to help, please contact me. :)



**Why Python3?**

Because I only have python3 installed on my computer. :)

In general, I only use python3. You too should probably migrate. It's not like those old times where you could hardly find a proper library that worked for py3. Most of the big ones have already migrated and there is a push to phase python 2 out. For example, look at Ubuntu 16.0.4 which only contains python 3 by default.



**I want to fork this and do some awesome thing with it, do permit this?**

Of course! Do whatever you want to do with it. The code is released under MIT license and the mod is for public domain. Although it would be cool if you mention me. :)




# Contact

I'm https://www.reddit.com/user/Ariestinak on reddit. 

You can also contact me from my email: ariestinak@gmail.com



