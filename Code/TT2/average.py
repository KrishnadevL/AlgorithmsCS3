class Average:
    def __call__(self, n):
        total = 0
        # conducts factorial formula multiplying previous value 
        for item in n:
        	total = total + item

        return total #recursive 

def main():
  user_ans = int(input("How many numbers are you taking the average of? "))
  number_bank = []
  while user_ans > 0:
    user_num = int(input("Enter a number: "))
    number_bank.append(user_num)
    user_ans = user_ans-1
  print(Average(number_bank))

if __name__ == "__main__":
  main()