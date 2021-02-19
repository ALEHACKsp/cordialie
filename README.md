# cordialie
Cordialie is a highly customizable and dynamic password profiler. Print hundreds to millions of possible combinations for a specific target easily, and efficiently. Usage is simple, with easy to edit open source code.  This script revolves around OSINT and social engineering, as wordlist are based off of your targets personal information.
This script does not perform any form of dictionary attack itself, but it's great for building up a wordlist when you perform one in a pen-testing enviroment.

# awareness
Cordialie was also designed to teach people an important aspect of Cyber Security.  And that heavly revolves around the passwords people use for any account.  Hopefully this 
tool demostrates why it's a bad idea to use passwords containing personal information, as this script heavily takes advantage of that.  A good password would be considered as a string of random characters, 25+ letters long.  A password manager is a great option as well, theres no such thing as too many precautions when it comes to security.

# features
• Generate a wordlist in a short amount of time, with the length and keyword amount of your choice. (Note that using a high length may take a more longer then usual)
• Easy to read and edit source code. Every step is noted, and put into one .py file.
• Cross platform, can run on Windows, Linux, Mac, etc.
• All modules used are (should) be preinstalled with python.
• Generated list are dynamic, meaning you can choose to combine keywords with numbers only, letters only, etc.
• Allows for a small varaity of hashes to print with each word, for possible data breach observation.
• A load of small handy features, that may fit to your liking.

# usage
Minimum usage: "python3 cordialie.py -f [FILE] -a [LIST AMOUNT] -k [KEYWORD AMOUNT]
