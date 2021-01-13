import matplotlib.pyplot as plt

x_min = ''
x_max = ''
y_min = ''
y_max = ''
type_ = ''

fig = plt.figure()
ax = fig.add_subplot(111)

while True:
    while x_min is not int:
        try:
            x_min = float(input('Enter x min: '))
            break
        except ValueError:
            print('Please enter a valid number ')
    
    if x_min < 0:
        print('Please enter a positive number ')
    elif x_min >= 5000:
        print("x min should less than maximun number (Maximum number: 5000)")
    else:
        break

while True:
    while x_max is not int:
        try:
            x_max = float(input('Enter x max: '))
            break
        except ValueError:
            print('Please enter a valid number: ')

    if x_max <= x_min and x_max >= 0:
        print('Please input correct value')
    elif x_max > 5000 :
        print("Please input correct value (Maximum number: 5000)")
    elif x_max < 0:
        print('Please enter a positive number')
    elif x_max > x_min:
        break
print('----------------------')

# ---------------------------------------------------

while True:
    while y_min is not int:
        try:
            y_min = float(input('Enter y min: '))
            break
        except ValueError:
            print('Please enter a valid number')
    
    if y_min < 0:
        print('Please enter a positive number')
    elif y_min >= 5000:
        print("y min should less than maximun number")
    else:
        break

while True:
    while y_max is not int:
        try:
            y_max = float(input('Enter y max: '))
            break
        except ValueError:
            print('Please enter a valid number')

    if y_max <= y_min:
        print('Please input correct value')
    elif y_max > 5000 :
        print("Please input correct value (Maximun number: 5000)")
    elif y_max > y_min:
        break

# ---------------------------------------------------
print('----------------------')
print('[1] BVA')
print('[2] Worst Case')
print('[3] Robustness')
print('[4] Worst Case Robustness')

x_diff =  ((x_max - x_min)/100*10)
y_diff = ((y_max - y_min)/100*10)

while True: 
    while type_ is not int:
        try:
            type_ = int(input("Please select type of test case: "))
            break
        except ValueError:
            print('Please select correct type')
    if type_ == 1 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid, x_mid , x_mid , x_mid , x_max-x_diff, x_max]
        list_y = [ y_mid, y_mid, y_mid, y_max-y_diff, y_max,y_min+y_diff, y_min , y_mid, y_mid]
        plt.suptitle('BVA')
        break
    if type_ == 2 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid, x_mid , x_mid , x_mid , x_max-x_diff, x_max, x_min, x_min, x_min,x_min, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff,x_max, x_max,x_max,x_max]
        list_y = [ y_mid, y_mid, y_mid, y_max-y_diff, y_max,y_min+y_diff, y_min , y_mid, y_mid, y_max,y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff, y_min,y_max,y_max-y_diff,y_min+y_diff,y_min]
        plt.suptitle('Worst Case')
        break
    if type_ == 3 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid    , x_mid     , x_mid   , x_mid , x_max-x_diff, x_max   , x_min-x_diff , x_mid ,x_mid , x_max+x_diff]
        list_y = [ y_mid, y_mid    , y_mid, y_max-y_diff, y_max ,y_min+y_diff, y_min , y_mid    , y_mid    ,y_mid, y_max+y_diff , y_min-y_diff, y_mid]
        plt.suptitle('Robustness')
        break
    
    if type_ == 4 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid, x_mid , x_mid , x_mid , x_max-x_diff, x_max, x_min, x_min, x_min,x_min, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff,x_max, x_max,x_max,x_max, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min, x_min, x_min+x_diff, x_min+x_diff, x_mid ,x_mid ,x_max-x_diff, x_max-x_diff, x_max ,x_max, x_max+x_diff , x_max+x_diff, x_max+x_diff, x_max+x_diff, x_max+x_diff, x_max+x_diff, x_max+x_diff]
        list_y = [ y_mid, y_mid, y_mid, y_max-y_diff, y_max,y_min+y_diff, y_min , y_mid, y_mid, y_max,y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff, y_min,y_max,y_max-y_diff,y_min+y_diff,y_min,y_max+y_diff, y_max, y_max-y_diff , y_mid, y_min+y_diff , y_min, y_min-y_diff, y_max+y_diff, y_min-y_diff, y_max+y_diff, y_min-y_diff,y_max+y_diff, y_min-y_diff, y_max+y_diff, y_min-y_diff, y_max+y_diff, y_min-y_diff,y_max+y_diff,y_max,y_max-y_diff, y_mid, y_min+y_diff, y_min, y_min-y_diff]
        plt.suptitle('Worst Case Robustness')
        break
    else: 
        print('Please select correct type')

plt.scatter(list_x,list_y)
plt.ylabel('Y value')
plt.xlabel('X value')

for i,j in zip(list_x,list_y):
    ax.annotate('%s)' %j, xy=(i,j), xytext=(30,0), textcoords='offset points')
    ax.annotate('(%s,' %i, xy=(i,j))

plt.grid()
plt.show()