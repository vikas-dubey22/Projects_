import random 
print("ROCK PAPER SCISCCORS:::\n")
print("RULES OF THE GAME \n - Inputs -> rock,paper,scissors\n - 5 rounds will be played\n - Winning Score should be 3")
print("Round 1 \n")
rounds = 1
while(rounds<=5):
    print("ROUND :",rounds)
    user_ip = input()
    l = ["rock","paper","scisscors"]
    comp_ip = random.choice(l)
    print("\nROUND ",rounds," INPUTS 1) User move - ",user_ip,"\n 2) AI move",comp_ip)
    u_score = 0
    c_score = 0
    if user_ip.lower()=='rock':
        if comp_ip=='paper':
          c_score +=1
          print("AI wins the round\n")
        elif comp_ip=='scisscors':
           u_score+=1
           print("User wins the round\n")
        else:
            print("Round Tied\n")
    elif user_ip=='paper':
        if comp_ip=='scisscors':
          c_score +=1
          print("AI wins the round\n")
        elif comp_ip=='rock':
           u_score+=1
           print("User wins the round\n")
        else:
            print("Round Tied\n")
    elif user_ip=='scisscors':
        if comp_ip=='rock':
           c_score +=1
           print("AI wins the round\n")
        elif comp_ip=='paper':
             u_score+=1
             print("User wins the round\n")
        else:
            print("Round Tied\n")
    if u_score==3 or c_score==3:
        if u_score==3:
            print("\nUSER WON THE GAME")
        else:
            print("\nAI WON THE GAME")
        break
    rounds = rounds+1
