![alt text](https://github.com/9socket/cordialie/logo/cordialielogo.png?raw=true)

# cordialie
Cordialie is a highly customizable and dynamic password profiler. Print hundreds to millions of possible combinations for a specific target easily, and efficiently. Usage is simple, with easy to edit open source code.  This script revolves around OSINT and social engineering, as wordlist are based off of your targets personal information.
This script does not perform any form of dictionary attack itself, but it's great for building up a wordlist when you perform one in a pen-testing enviroment.

# awareness
Cordialie was also designed to teach people an important aspect of Cyber Security.  And that heavly revolves around the passwords people use for any account.  Hopefully this 
tool demostrates why it's a bad idea to use passwords containing personal information, as this script heavily takes advantage of that.  A good password would be considered as a string of random characters, 25+ letters long.  A password manager is a great option as well, theres no such thing as too many precautions when it comes to security.

# features
• Easy to read and edit source code. Every step is noted, and put into one .py file.<br/>
• Cross platform, can run on Windows, Linux, Mac, etc.<br/>
• All modules used are (should) be preinstalled with python.<br/>
• Generated list are dynamic, meaning you can choose to combine keywords with numbers only, letters only, etc.<br/>
• Allows for a small varaity of hashes to print with each word, for possible data breach observation.<br/>
• A load of small handy features, that may fit to your liking.

# usage
Minimum usage: "python3 cordialie.py -f [FILE] -a [LIST AMOUNT] -k [KEYWORD AMOUNT]" (Linux example) <br/>

Optional usage:
  -pm [Print Mode] : Displays every generated word on your cmd/terminal.<br/>
  -s  [Seconds]    : Waits the amount of time inbetween each generation in seconds. <br/>
  -t  [List Type]  : Allows you to generate list to your liking. <br/>
         default/1 - all<br/>
                 2 - numbers only<br/>
                 3 - letters only<br/>
                 4 - extra characters only<br/>
  -h  [Hash]       : Prints chosen hash with each generation for data breach observation.<br/>
                 1 - md5<br/>
                 2 - md4<br/>
                 3 - sha1<br/>
                 4 - sha224<br/>
                 5 - sha256
