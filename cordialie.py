
#AUTHOR : 9socket
#GITHUB : https://github.com/9socket
#REPO   : https://github.com/9socket/cordialie


#Cordialie is a free and open source program.
#Feel free to modify/change it in any way.


#IMPORTED MODULES
import argparse, random, time, hashlib
from datetime import datetime


#MARKS DATETIME
clock = datetime.now()


#ARGPARSE ARGUEMENTS
parser = argparse.ArgumentParser(description='Command arguements for Cordialie')

parser.add_argument('-f', '--file', type=str, help='File used for list.')
parser.add_argument('-a', '--amount', type=int, help='Amount of words generated.')
parser.add_argument('-k', '--keywords', type=int, help='Amount of keywords wanted.')
parser.add_argument('-t', '--type', type=int, help='Type of list generated.')
parser.add_argument('-s', '--seconds_aka_timedmode', help='Seconds between each generation.')
parser.add_argument('-hs', '--hash', type=int, help='Displays hash for each generation.')
args = parser.parse_args()


#LIST FOR PASSWORD PROFILING
uni = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','-','=','<','>','?']

num = ['1','2','3','4','5','6','7','8','9','0']

let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

spe = ['!','@','#','$','%','^','&','-','=','<','>','?']


#SPECIFIES LIST TYPE WHEN -t IS USED
list_type = 'default/all'
if (args.type):
    if (args.type) == 1:
        uni = (uni)
    if (args.type) == 2:
        uni = (num)
        list_type = 'Numbers only'
    if (args.type) == 3:
        uni = (let)
        list_type = 'Letters only'
    if (args.type) == 4:
        uni = (spe)
        list_type = 'Special characters only'


#DEFINES SECONDS IF -s IS USED
if (args.seconds_aka_timedmode):
    seconds = int(args.seconds_aka_timedmode)


#CORDIALIE BANNER
def banner():
    print("                    _ _       _ _       ")
    print("   ___ ___  _ __ __| (_) __ _| (_) ___  ")
    print("  / __/ _ \| '__/ _` | |/ _` | | |/ _ \ ")
    print(" | (_| (_) | | | (_| | | (_| | | |  __/ ")
    print("  \___\___/|_|  \__,_|_|\__,_|_|_|\___| ")
       
                                      
#STARTS PROGRAM IF ARGUEMENTS ARE SPECIFIED CORRECTLY                          
if (args.file) and (args.amount) and (args.keywords):
    

    #DEFINES AMOUNT OF KEYWORDS, AND CREATES EMPTY LIST
    num = (args.keywords)
    base = int(0)
    keywords = []
    
    banner()
    print(' ======================================')
    

    #STARTS PROCESS FOR IMPLYNG KEYWORDS. KEYWORDS GET ADDED TO 'keywords' LIST
    for i in range(num):
        base = (base) + int(1)
        tag = f'#{base}'
        key = input(f' {tag}> ')
        keywords.append(key)
        

        #OPENS OR CREATES FILE FOR WORDLIST
        f = open((args.file), "a")


        #MAKRS TIME BEFORE GENERATING LIST
        time_start = clock.strftime("%H:%M:%S")
    

    #DEFINES COMBOS FOR POSSIBLE PASSWORDS  |  keywords = defined list of target  uni = premade list for profiling
    for i in range(args.amount):
        com0 = f'{random.choice(keywords)}'
        com1 = f'{random.choice(uni)}{random.choice(keywords)}'
        com2 = f'{random.choice(keywords)}{random.choice(uni)}'
        
        com3 = f'{random.choice(uni)}{random.choice(uni)}{random.choice(keywords)}'
        com4 = f'{random.choice(keywords)}{random.choice(uni)}{random.choice(uni)}'
        
        com5 = f'{random.choice(uni)}{random.choice(keywords)}{random.choice(uni)}{random.choice(uni)}'
        com6 = f'{random.choice(uni)}{random.choice(uni)}{random.choice(keywords)}{random.choice(uni)}'
        
        com7 = f'{random.choice(uni)}{random.choice(keywords)}{random.choice(uni)}'
        com8 = f'{random.choice(uni)}{random.choice(uni)}{random.choice(keywords)}{random.choice(uni)}{random.choice(uni)}'

        com9 = f'{random.choice(keywords)}_{random.choice(uni)}{random.choice(uni)}'
        com10 = f'{random.choice(uni)}{random.choice(uni)}_{random.choice(keywords)}'

        com11 = f'_{random.choice(keywords)}{random.choice(uni)}{random.choice(uni)}'
        com12 = f'{random.choice(uni)}{random.choice(uni)}{random.choice(keywords)}_'
        

        #PUT ALL COMBOS IN LIST AND RANDOMLY CHOOSES ONE
        combos = [com0,com1,com2,com3,com4,com5,com6,com7,com8,com9,com10,com11,com12]
        word = f'{random.choice(combos)}'
        

        #WAITS TIME SPECIFIED INM -s IS USED
        if (args.seconds_aka_timedmode):
            time.sleep(seconds)


        #DEFINES HASH TYPE AND HASES CHOOSEN GENERATION TO HASH WHEN -hs IS USED
        hash_option = 'None'
        if (args.hash):
            if (args.hash) == 1:
                hh = hashlib.md5(word.encode())
                hash_option = 'md5'
            if (args.hash) == 2: 
                hh = hashlib.sha1(word.encode())
                hash_option = 'sha1'
            if (args.hash) == 3: 
                hh = hashlib.sha224(word.encode())
                hash_option = 'sha224'
            if (args.hash) == 4: 
                hh = hashlib.sha256(word.encode())
                hash_option = 'sha256'
            if (args.hash) == 5: 
                hh = hashlib.sha384(word.encode())
                hash_option = 'sha384'
            if (args.hash) == 6: 
                hh = hashlib.sha512(word.encode())
                hash_option = 'sha512'

            try:
                hh = (hh.hexdigest())
                word = f'{word} : {hh}'
            except:
                print(' ')
                print(' ERROR: Invalid hash input.')
                exit()


        #COMBINES \n WITH GENERATION TO INDEX NEW LINE THEN WRITES IT ON FILE
        word = f'{word}\n'
        f.write(word)


    #MARKS TIME AFTER GENERATING LIST
    clock = datetime.now()
    time_end = clock.strftime("%H:%M:%S")
       

    #PRINTS LIST CONFIGURATIONS
    print(' ======================================')
    print(f' {args.amount} words have been generated to {args.file}')
    print(' Check the file directory for the list')
    print(' ______________________________________')
    print(f' Time Started : {time_start}')
    print(f' Time Stopped : {time_end}')
    print(f' Algorithm    : {hash_option}')
    print(f' List Type    : {list_type}')
   
    
#PRINTS USAGE IF ARGUEMENTS ARNT DEFINED CORRECTLY    
else:
    banner()
    print(' ======================================')
    print(' CORDIALIE: USAGE ')
    print(' ')
    print(' "cordialie.py -f (filename) -a (list amount) -k (keyword amount)"')
    print(' ')
    print(' Optional_______')
    print(' -t [option]: list type                ::: Defines character print type.')
    print('          default = all')
    print('                1 = all')
    print('                2 = numbers')
    print('                3 = letters')
    print('                4 = extra characters')
    print(' -s [seconds]: timed mode              ::: Seconds between generation. (for slower devices)')
    print(' -hs [hash]: hash print                ::: Prints password hash w/ each generation.')
    print('                1 = md5')
    print('                2 = sha1')
    print('                3 = sha224')
    print('                4 = sha256')
    print('                5 = sha384')
    print('                6 = sha512')
    print(' ')
    print(' GitHub | https://github.com/9socket/cordialie')
  
#LEGAL DISCLAIMER : Cordialie is not made for attacking accounts/websites/platforms you don't own, or have permission to.  No one but yourself is responsible for any misuse of this script.