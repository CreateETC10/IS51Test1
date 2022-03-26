"""

The program is trying to detemine which payment option is better (more money). 
The first option is 100 dolars per day for 10 days. 
The second option is 1 dollar a day with it being doubled each day for 10 days. 
There will be two functions to calculate the pay rate function
Function1 will calculate the amount for the first option 
Function2 willcalculate the amount for the second option 

Function1 will output $100 * 10 days  
Functions2 will loop 10 times with each time doubling the amount and add the amount to the total

If the amount is eqal, we ouptut to the user "Option 1 and Option 2 pays the same"
If the option 1 is better, we output to the user "Option 1 is better"
If the option 2 is better, we output to the user "Option 2 is better"

"""

"""

# Option1 
    return 100 * 10
# Option2 
    amount=1 
    list1=[]
    loop 10 times 
        add amount to list1
        amount *= 2
        return amount 
    sum = sum of all items in loop 
    return sum
# Main
    var1=option1 
    var2=option2 

    if var1=var2
        "Option 1 and Option 2 pays the same"
    if var1<var2
        "Option 2 is better"
    else 
        "Option 1 is better"

main

"""

def option1():
    return 100*10

def option2():
    amount=1 
    list1=[]
    for i in range(0,10):
        list1.append(amount)
        amount*=2
    total=sum(list1)
    return total 

def main():
    answer=""
    var1=option1()
    var2=option2()
    if var1==var2:
        answer="Option 1 and Option 2 pays the same"
    elif var1<var2:
        answer="Option 2 is better"
    else:
        answer="Option 1 is better"
    print(answer)

main()