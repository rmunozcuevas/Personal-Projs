import random


def eight_ball():
    responses = ("Yes", "No", "Try Again", "Ask Again Later", "Outlook Good", "Cannot Predict Now", "Don't Count On It", "Yes, definitely", "My Sources Say No")
    while(True):
        user = input("Enter in a response for the grand 8 - ball: ")
        if user == "Q": 
            print("ok you don't want to roll")
            break
        else:
            r = random.choice(responses)  
            print(r)




# eight_ball()


def ABC():
    for i in range(65,90):
        print(chr(i))

# ABC()



# unit_circle should test me on whether I know my (sin, cos values and radians and degrees)
#def unit_circle():


def user_auth():
    my_dict = {"90210":"Travis Scott", "2900":"Playboi Carti", "1600":"Lil Uzi Vert", "1400":"Trippie Redd"}
    while True:
        u = input("Enter in a in the password to see who you are:")
        if u in my_dict:
            print("Password was correct, Welcome back",my_dict[u])
            break
        else:
            print("Key was not found please try again")

user_auth()
