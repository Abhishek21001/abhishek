import shutil
path = "C:\Python34"
stat = shutil.disk_usage(path)
print("disk usage statics:", stat)

import time
start = time.time()

def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n-1)

num = int(input("Enter a number: "))

if num < 0:
    print("soorry, factorial does not exist for negetive numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The time complexity  of program is : ",num,"is",
          recur_factorial(num))

end = time.time()
print("The time complexity of program is :", end-start)
