user_name = input(" Name?").strip()
mood = input("Payment method? (card/cash):".lower().strip())
if mood == "card" :
    print("processing..")
else :
    print("cash accepted")