import os

# clear = os.system("cls")
from art import logo








print(logo)
#revised secret auction without bugs



dict={}
def char_1():
    end_of_game = False
    while end_of_game==False:
        name=input("what is your name")
        bid = int(input("what is the bid: $"))
        dict[name]=bid
        choice=input("are there any bidders yes or no?").lower()
        if choice =="yes":
            char_1()


            end_of_game=False


        if choice =="no":
            end_of_game=True
            variable = 0
            winner=""
            for n in dict:
                higgest_bidder = dict[n]
                # print(higgest_bidder)
                if higgest_bidder > variable:
                    variable=higgest_bidder
                    winner=n
            print(f"{winner} is the highest with {higgest_bidder}")









char_1()



