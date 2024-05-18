the_bill =float(input("How much the bill cost?: ").replace(",","."))
the_tip =int(input("How much tip do you want to leave: 10% / 12& / 15%? "))
percent = float(the_bill / 100)
total_bill = the_bill + percent 
costumers = float(input("How many costumers are you?: "))
total_bill_per_costumer = total_bill / costumers
total_bill_per_costumer = "{:.2f}".format(total_bill_per_costumer)

print(f"Each costumer should pay: {total_bill_per_costumer}€")
print("Each costumer should pay: " + total_bill_per_costumer + "€")
