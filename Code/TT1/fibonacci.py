def fibonacci(n, second_last, last):
    if n-1 == 0:
        return second_last
    else:
        new_last = second_last + last
        second_last = last
        return fibonacci(n-1, second_last, new_last)
# Driver Program

def tester():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    try:
      print("The fibonacci series of", num, "is", fibonacci(num,0,1))
    except ValueError:
      print("Not a number")
    except RecursionError: 
      if num < 0:
        print("Sorry, the fibonacci series does not exist for negative numbers")
      else:
        print("Out of range")
        
      
if __name__ == "__main__":
    tester()