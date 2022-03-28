class Factorial:
    def __call__(self, n):
        num = 1
        # conducts factorial formula multiplying previous value 
        for item in range(1,n+1):
        	num = num * item

        return num #recursive 
      
      
def main():
  user_ans = input("Choose a number:")
  user_num = int(user_ans)
  fact_num = Factorial() # object instantiation and run __init__ method
  print("The factorial for the number "+user_ans+" is:")
  print(fact_num(user_num)) # object running __call__ method

if __name__ == "__main__":
  main()