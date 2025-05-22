
##########################################################################################################################
###  exercise Grading  ###

# my version
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding" 
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
        
print(student_grades)

---

# someone's better version
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# using function gives more universal approach, flexibility and function can be reused
def score_to_grade(score):
    if score > 90:
        return "Outstanding"
    elif score > 80:
        return "Exceeds Expectations"
    elif score > 70:
        return "Acceptable"
    else:
        return "Fail"
 
student_grades = {}
 
for key in student_scores:
    student_grades[key] = score_to_grade(student_scores[key])





##########################################################################################################################
###  PROJECT AUCTION  ###

............................................................................................
../my_solution.py

from art import logo

# function to find max bid
def highest_bid(bids):
    max_bid = 0
    max_bid_name = ""
    for name in bidders_list:
        if bidders_list[name] > max_bid:
            max_bid = bidders_list[name]
            max_bid_name = name
    print("\n" * 3)
    print(f"The winner is '{max_bid_name}' with bid of ${bidders_list[max_bid_name]}")


# initial parameters
bidders_list = {}
continue_bidding = True

print(logo)

# loop for bidders
while continue_bidding:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    bidders_list[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': \n").lower()

    if should_continue == 'no':
        continue_bidding = False
        highest_bid(bidders_list)
    else:
        print("\n" * 20)




............................................................................................
../teacher_solution.py

from art import logo
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)




............................................................................................
../art.py

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''




[end]
