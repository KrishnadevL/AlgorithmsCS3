class Factorial:
    def __init__(self):
      # defines the self, so it can be called again
        self.factor = [0, 1]
    def __call__(self, n):
        num = 1
        # conducts factorial formula multiplying previous value 
        for item in range(1,n+1):
        	num = num * item

        return num #recursive 
      
def main():
  user_num = int(input("Choose a number:"))
  fact_num = Factorial() # object instantiation and run __init__ method
  print(fact_num(user_num)) # object running __call__ method

if __name__ == "__main__":
  main()