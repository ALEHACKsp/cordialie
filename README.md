![Logo](https://github.com/9socket/cordialie/blob/main/Images/cordialielogo.png)

# cordialie
Cordialie is a highly customizable and dynamic password profiler. Print hundreds to millions of possible combinations for a specific target easily, and efficiently. Usage is simple, with easy to edit open source code.  This script revolves around [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence) and [Social Engineering](https://en.wikipedia.org/wiki/Social_engineering_(security)), as wordlist are based off of your targets personal information.
This script does not perform any form of dictionary attack itself, but it's great for building up a wordlist when you perform one in a pen-testing enviroment.

# awareness
Cordialie was also designed to teach people an important aspect of Cyber Security.  And that heavly revolves around the passwords people use for any account.  Hopefully this 
tool demostrates why it's a bad idea to use passwords containing personal information, as this script heavily takes advantage of that.  A good password would be considered as a string of random characters, 25+ letters long.  A password manager is a great option as well, theres no such thing as too many precautions when it comes to security.<br/>

And obviously, this tool shouldn't be misued with the intent of attacking unathroized accounts or platforms.  No one but yourself is resonsible for misuse.  This is made for penetration enviroments, where permission is granted.

# features
• Easy to read and edit source code. Every step is noted, and put into one .py file.<br/>
• Cross platform, can run on Windows, Linux, Mac, etc.<br/>
• All modules used are (should) be preinstalled with python.<br/>
• Generated list are dynamic, meaning you can choose to combine keywords with numbers only, letters only, etc.<br/>
• Allows for a small varaity of hashes to print with each word, for possible data breach observation.<br/>
• A load of small handy features, that may fit to your liking.

# usage
Minimum usage: "python3 cordialie.py -f [FILE] -a [LIST AMOUNT] -k [KEYWORD AMOUNT]" (Linux example) <br/>

![Usage](https://github.com/9socket/cordialie/blob/main/Images/CordialieUsage.png)<br/>
Read the Cordialie guide installed with the repo for more information.<br/>
Example: "python3 cordialie.py -f target.txt -a 500000 -k 10" <br/>

• Note that choosing a file that already exsit in the directory, will add onto it for list extension, and won't overwrite it.

# installation
Installing is very simple, with 2 different methods. <br/>
1. "git clone https://github.com/9socket/cordialie.git".<br/>
2. Simply just download the .zip file.<br/>

And just incase you haven't realized, python is also required to run this script. [Download Python](https://www.python.org/downloads/)

# code
As mentioned earlier, Cordialie is open source, and easy to edit. Each step is noted, and the script is 214 lines in total (including notes/gaps) <br/>
Line 105 is where the combos are defined for the list, so if you want any of your own added, define the variable, and put it in the list 'combos'.
