
while True:
    x_min = float(input('Enter x min: ')) 
    if x_min < 0:
        print('Please enter a positive number ')
    elif x_min <= -1 :
        print('Please enter a positive number')
    elif x_min >= 5000:
        print("x min should less than maximum number (Maximum number: 5000)") 
    else:
        break
while True:
    x_max = float(input('Enter x max: '))
    if x_max <= x_min and x_max >= 0:
        print('Please input correct value')
    elif x_max > 5000 :
        print("Please input correct value (Maximum number: 5000)")
    elif x_max < 0:
        print('Please enter a positive number')
    elif x_max > x_min:
        break
while True:
    y_min = float(input('Enter y min: ')) 
    if y_min < 0:
        print('Please enter a positive number')
    elif y_min >= 5000:
        print("y min should less than maximun number")
    else:
        break
while True:
    y_max = float(input('Enter y max: '))      
    if y_max <= y_min:
        print('Please input correct value')
    elif y_max > 5000 :
        print("Please input correct value (Maximun number: 5000)")
    elif y_max > y_min:
        break

print('type of test case')
while True: 
    type_ = int(input("Please select type of test case: "))     
    if type_ == 1 :
        print("BVA mapping")
        break
    if type_ == 2 :
        print("Worst Case")
        break
    if type_ == 3 :
        print("Robustness")
        break  
    if type_ == 4 :
        print("Worst Case Robustness")
        break
    else: 
        print('Please select correct type')

print("show graph")