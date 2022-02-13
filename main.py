import os

# clear = os.system("cls")
from art import logo








print(logo)
bid_1 = {}
end_of_game=False
while end_of_game==False:
    name=input("your name\n")
    price=int(input("price\n"))


    name_1=""

    def bid(name,price):
        bid_1[name]=price

    bid(name,price)

    c=input("are there more ppl?yes or no\n")


    print ("\n" * 100)
    # print(bid_1)


    if c =="no":
        end_of_game=True
        highest_bid=0

        for zeta in bid_1:
            bid_amount = bid_1[name]
            if bid_amount>highest_bid:
                highest_bid+=bid_amount
                winner=zeta
        print(f"{zeta} with a bid of {highest_bid} is the winner")
        # print(bid_1)
        # a= max(bid_1, key=bid_1.get)
        # print(a)




