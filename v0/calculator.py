class Calculator: 
   def add(x, y):
      return x + y 

   def subtract(x, y): 
      return x - y 

   def multiply(x, y): 
      return x * y 

   def divide(x, y): 
      return x / y

   def pow(x, y):
      res = 1
      for i in range(2,y):
         res = res*i
