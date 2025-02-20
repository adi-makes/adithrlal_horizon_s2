import matplotlib.pyplot as plt

n = int(input("Enter the number of points : "))

x = []
y = []

print("Enter the x values : ")

for i in range (n) :
    x.append(int(input(f"x{i+1} = ")))
    
print("Enter the y values : ")

for i in range(n) :
    y.append(int(input(f"y{i+1} = ")))


plt.scatter(x,y)
plt.show()