# This file contains codes from the first hundred days of Python.
# Up to this point, 10 percent of the videos have been watched. Despite the 90 percent resting ahead, I guess I've made it far enough. 
# This is the final project which is Blind Auction:
other = True
while other == True:
    name = str(input("What is your name? "))
    bid = int(input("What's your bid? $"))
    other_participant = input(
        str("Are there any other bidders? Type 'yes' or 'no'."))

    if other_participant == "yes":
        other == True
    if other_participant == "no":
        other == False


auction = []
bidder = {name: bid}
auction.append(bidder)

bidprice = 0

for candidate in auction:

    if bid > bidprice:
        bidprice == bid

print(f"The winnder is {auction[name]} with bid of {bid}$")
