#Taking input
num1=int(input("Enter an integer : "))
num2=float(input("Enter a float number : "))

#Printing the type of the input values
print("The type of num1 is : ",type(num1));
print("The type of num2 is : ",type(num2));


print("Some basic operations : ")

z=float(num1+num2);    #using variable z to calculate sum     
print("Sum : ",z);     #printing sum

z=float(num1/num2);    #Performing division
print("Remainder : ",z);

z=float(num1-num2);    #Performing subtraction
print("Subtraction : ",z);

z=float(num1*num2);    #Performing multiplication
print("Product : ",z);
