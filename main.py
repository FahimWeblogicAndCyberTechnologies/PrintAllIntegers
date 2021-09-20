print("Integers not divisible by 2 and 3, that lie between 1 and 50 are : ")
n = 1
while n <= 51:
   if n % 2 != 0 and n % 3 != 0:
      print(n)
   n = n+1