def number_sort(num1,num2):
  temp = ""
  if num2 > num1:
    temp = num1
    num1 = num2
    num2 = temp 
  print(num1,num2)


user_num1 = input("What is your first number? ")
user_num2 = input("What is your second number? ")

number_sort(user_num1,user_num2)