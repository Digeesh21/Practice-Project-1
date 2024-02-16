a=int(input("Enter the Number : "))
if a%2==0:
     print("The number is divisible by 2")
     print("It is a even number")
else:
    print("The number is odd ")
    
num = a


if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")