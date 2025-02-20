import matplotlib.pyplot as plt

def dist(a, b, c, d) : #function to calculate the distance
    d = (((a-b)**2+(c-d)**2)**0.5) # idiot me used wrong distance formula
    return (d)

def closest(x, y) : #function to find the closest point to each point
    
    xc = []
    yc = []
    
    for i in range (n) :
        d1 = [] # this was moved here, so that it resets after each point (x,y)
        for j in range (n) :
            d1.append(dist(x[i], x[j], y[i], y[j]))
        d_temp = d1.copy() # using .copy() so that d_temp doesnt get modified when d1 gets modified
        d_temp.sort()
        flag = 0
        for k in range (n) :
            if(d_temp[1] != d1[k]) : 
                flag = flag + 1
            else :
                break
        xc.append(x[k])
        yc.append(y[k])
                  
    return(xc, yc)
    

#taking the number of points
n = int(input("Enter the number of points : "))

x = []
y = []

#taking the points
for i in range (n) :
    x.append(int(input(f"Enter x{i+1} : ")))    
    y.append(int(input(f"Enter y{i+1} : ")))  
    
x_close, y_close = closest(x, y)  # idiot me called this before populating x and y

#ploting the points
plt.scatter(x, y)

for i in range (n) :
    plt.plot([x[i], x_close[i]], [y[i], y_close[i]], 'r-') 

plt.show()