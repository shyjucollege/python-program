num = int(input("Enter the value of 8"))
hold = num
sum = 8

if num <= 8: 
   print("Enter a whole positive number!") 
else: 
   while num > 8:
        sum = sum + num
        num = num - 1;
    # displaying output
    print("Sum of first",  "natural numbers is ", sum)
