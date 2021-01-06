import matplotlib.pyplot as plt
x_min = float(input("Enter x min: ")) 
while True:
        x_max = float(input("Enter x max: "))
        if x_max <= x_min:
            print('Please input correct value')
        elif x_max > x_min:
            break
print('----------------------')
y_min = float(input("Enter y min: ")) 
while True:
        y_max = float(input("Enter y max: ")) 
        if y_max <= y_min:
             print('Please input correct value')
        elif y_max > y_min:
            break
print('----------------------')
print('[1] BVA')
print('[2] Worst Case')
print('[3] Robustness')
print('[4] Worst Case Robustness')
x_check = x_max - x_min
y_check = y_max - y_min
if (x_check <= 10) :
    x_diff = 0.1
elif (x_check > 10 and x_check <= 100 ):
    x_diff = 1
elif (x_check > 100 and x_check <= 1000):
    x_diff = 10
if (y_check <= 10) :
    y_diff = 0.1
elif (y_check > 10 and y_check <= 100 ):
    y_diff = 1
elif (y_check > 100 and y_check <= 1000):
    y_diff = 10

while True: 
    type = int(input("Please select type of test case: ")) 
    if type == 1 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid, x_mid , x_mid , x_mid , x_max-x_diff, x_max]
        list_y = [ y_mid, y_mid, y_mid, y_max-y_diff, y_max,y_min+y_diff, y_min , y_mid, y_mid]
        break
    if type == 2 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid    , x_mid     , x_mid   , x_mid , x_max-x_diff, x_max   , x_min-x_diff , x_mid ,x_mid , x_max+x_diff]
        list_y = [ y_mid, y_mid    , y_mid, y_max-y_diff, y_max ,y_min+y_diff, y_min , y_mid    , y_mid    ,y_mid, y_max+y_diff , y_min-y_diff, y_mid]
        break
    if type == 3 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid, x_mid , x_mid , x_mid , x_max-x_diff, x_max, x_min, x_min, x_min,x_min, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff,x_max, x_max,x_max,x_max]
        list_y = [ y_mid, y_mid, y_mid, y_max-y_diff, y_max,y_min+y_diff, y_min , y_mid, y_mid, y_max,y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff, y_min,y_max,y_max-y_diff,y_min+y_diff,y_min]
        break
    if type == 4 :
        y_mid = (y_max+y_min)/2
        x_mid = (x_min+x_max)/2
        list_x = [ x_min, x_min+x_diff, x_mid, x_mid, x_mid , x_mid , x_mid , x_max-x_diff, x_max, x_min, x_min, x_min,x_min, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_min+x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff, x_max-x_diff,x_max, x_max,x_max,x_max, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min-x_diff, x_min, x_min, x_min+x_diff, x_min+x_diff, x_mid ,x_mid ,x_max-x_diff, x_max-x_diff, x_max ,x_max, x_max+x_diff , x_max+x_diff, x_max+x_diff, x_max+x_diff, x_max+x_diff, x_max+x_diff, x_max+x_diff]
        list_y = [ y_mid, y_mid, y_mid, y_max-y_diff, y_max,y_min+y_diff, y_min , y_mid, y_mid, y_max,y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff,y_min,y_max, y_max-y_diff, y_min+y_diff, y_min,y_max,y_max-y_diff,y_min+y_diff,y_min,y_max+y_diff, y_max, y_max-y_diff , y_mid, y_min+y_diff , y_min, y_min-y_diff, y_max+y_diff, y_min-y_diff, y_max+y_diff, y_min-y_diff,y_max+y_diff, y_min-y_diff, y_max+y_diff, y_min-y_diff, y_max+y_diff, y_min-y_diff,y_max+y_diff,y_max,y_max-y_diff, y_mid, y_min+y_diff, y_min, y_min-y_diff]
        break

plt.scatter(list_x,list_y)
plt.ylabel('Y value')
plt.xlabel('X value')
plt.show()