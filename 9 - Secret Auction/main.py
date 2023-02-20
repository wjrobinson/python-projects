import os
from art import logo

bids = {}
bidding_finished = False

print(logo)

# Each loop compares against previous loops to determine highest bid.
def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of the bid is {winner} with a bid of {highest_bid}.")

# Gathers name and bids, stores in bids dictionary.
# To be used in find_highest_bidder function.
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif more_bidders == "yes":
        os.system('clear')
