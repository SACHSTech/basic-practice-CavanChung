oz= float(input("Enter the amount of ounces:"))
people = float(input("Enter the number of people to serve:"))
oz_to_ml= ((oz*29.57)*people)/4
print("You will need this much ml:" + str(oz_to_ml)) 