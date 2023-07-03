def calc_age():
  current_year = 2023
  try:
        year = int(input("Please enter the year of birth: "))
        age = current_year - year
        print("Your age is:", age)
  except TypeError:
        print("Please enter an integer")

def helloWorld():
  print("Hello World")

helloWorld()
calc_age()


  
