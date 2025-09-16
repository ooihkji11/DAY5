payment_method = input("payment method? (card/cash):").strip().lower()
if payment_method =="card" :
    print("processing..")
else :
    print ("cash accepted")