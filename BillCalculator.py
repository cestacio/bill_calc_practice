

def tip_given(bill_amount,tip_percentage):
    tip = bill_amount * (tip_percentage * .01)
    return tip  

def total_bill(tip_amount,bill_amount):
    total = tip_amount + bill_amount
    return total

def amount_per_person(bill_amount,number_of_people):
    split = float(bill_amount)/number_of_people
    return split

def main():
    choice = int(raw_input("Type 1 to calculate tip or 2 to split the bill")) 
    
    if choice == 1:
        bill_amount = int(raw_input("Enter bill amount")) 
        tip_percentage = int(raw_input("Enter tip percentage"))
        tip = tip_given(bill_amount,tip_percentage)
        print tip
        total = total_bill(tip,bill_amount)
        print total
        split_bill = raw_input("Would you like to split the bill, yes or no?")
        
        if split_bill == 'yes':
            number_of_people = int(raw_input('How many people?'))
            print amount_per_person(total,number_of_people)  

    else:
        print "hi"
        bill_amount = int(raw_input("Enter bill amount")) 
        number_of_people = int(raw_input('How many people are splitting the bill?'))
        print amount_per_person(bill_amount,number_of_people)
    


if __name__ == '__main__':
    main()



# print tip_given(10,10)
# print total_bill(1,10)
# print amount_per_person(10,3)