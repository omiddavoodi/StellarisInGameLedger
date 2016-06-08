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

Before you launch the game, run "start.py". If you are on Linux, make sure you have the right permissions.

If you have done everything right, you should see the prompt "Server Starts - localhost:12852".

---DO NOT CLOSE THIS, LAUNCH THE GAME---

After you are inside your game, do a new save. Then, click on the "Help" button on the bottom right corner of the screen.
