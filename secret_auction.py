from replit import clear
#HINT: You can call clear() to clear the output in the console.
from secret_auction_art import logo
print(logo)

bids = {}
biding_finished = False

def find_higest_bidder(bidding_record):
    highest_bid  = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}") 
        
while not biding_finished:
    name = input("What is your name: ")
    price = int(input("What is your bid? $"))
    bids[name] = price 
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if choice == "no":
        biding_finished = True
        find_higest_bidder(bids)
    elif choice == "yes":
        clear()
    
    
