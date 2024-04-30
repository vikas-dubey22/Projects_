#Commit Processed Successfully
import random
print("WELCOME TO HAND CRICKET :::")
userchoice = input("CHOOSE ODD OR EVE :")
compchoice=""
print("Userchoice - ",userchoice)
if userchoice.lower()=="eve":
    compchoice="odd"
elif userchoice.lower()=="odd":
    compchoice="eve"
else:
    print("wrong choice")
print("Computer choice - ",compchoice)
utoss = int(input("enter the choice for toss from 0-6::"))
comptoss = random.randint(0,6)
print("Utoss - ",utoss)
print("Comptoss - ",comptoss)
if utoss<=6:
    s = utoss+comptoss
print(s)
compdec = ''
l = ["batting","bowling"]
udecision=''
if s%2==0:
    if userchoice=='eve':
        udecision = input("Batting or bowling -> DECIDE")
        if udecision.lower()=='batting':
            compdec='bowling'
        elif udecision.lower()=='bowling':
            compdec='batting'
        else:
            print("toss dealyed")
    else:
        compdec = random.choice(l)
        if compdec.lower()=='batting':
            udecision='bowling'
        elif compdec.lower()=='bowling':
            udecision='batting'
else:
    if userchoice=='odd':
        udecision = input("Batting or bowling")
        if udecision.lower()=='batting':
            compdec='bowling'
        elif udecision.lower()=='bowling':
            compdec='batting'
        else:
            print("toss dealyed")
    else:
        compdec = random.choice(l)
        if compdec.lower()=='batting':
            udecision='bowling'
        elif compdec.lower()=='bowling':
            udecision='batting'
print("USER DECISION -",udecision)
print("COMPUTER DECISION -",compdec)
sc = 0
sec = 0
if udecision=='batting':
    print("user is batting , kindly provide inputs from 0-6")
    print("1ST INNINGS :")
    while True:
        innings_1 = int(input())
        comp_bowl = random.randint(0,6)
        print("USER MOVES ->",innings_1,"COMPUTER MOVES ->",comp_bowl)
        if innings_1==comp_bowl:
            print("Batsman out at :",sc)
            break
        else:
            sc = sc+innings_1
    sc = sc+1
    print("Target is ",sc)
    print("2ND INNINGS")
    while True:
        innings_2 = int(input())
        comp_bat = random.randint(0,6)
        print("USER MOVES ->",innings_2,"COMPUTER MOVES ->",comp_bat)
        if innings_2==comp_bat:
            print("Batsman out ",sec)
            break
        else:
            sec = sec+innings_2
            if sec>=sc:
                break
    if sec>=sc:
        print("COMPUTER HAS WON THE MATCH")
    else:
        print("USER HAS WON THE MATCH")
else:
    print("user is bowling,kindly provide inputs from 0-6")
    print("1ST INNINGS")
    while True:
        innings_1 = int(input())
        comp_bat = random.randint(0,6)
        print("USER MOVES->",innings_1," COMPUTER MOVES ->",comp_bat)
        if comp_bat==innings_1:
            print("Batsman is out at",sc)
            break
        else:
            sc = sc+comp_bat
    sc = sc+1
    print("Target is :",sc)
    print("User is batting now, Kindly provide inputs from 0-6")
    print("2ND INNINGS")
    while True:
        innings_2 = int(input())
        comp_bowl = random.randint(0,6)
        print("USER MOVES ->",innings_2," COMPUTER MOVES",comp_bowl)
        if innings_2==comp_bowl:
            print("Batsman is out at",sec)
            break
        else:
            sec = sec+innings_2
            if sec>=sc:
                break
    if sec>sc:
        print("USER HAS WON THE MATCH")
    else:
        print("COMPUTER HAS WON THE MATCH")
