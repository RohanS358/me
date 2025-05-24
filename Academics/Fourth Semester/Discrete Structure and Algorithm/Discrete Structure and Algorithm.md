---
tags: MOCs
---
```folder-index-content
```# LAB 1
Rohan Singh
<br>KCE080BCT033
Basics of python programming
import numpy as np
>Basic Input Output
b = 2
print(b)
string1 = "Hi I am Rohan Singh"
print(string1[1:3])
n = input("Enter the number: ")
print(n)
>Tuples
These are not mutable. Once set its set.
tup = ("Hello", 1, 2, 3,"mic check")
tup
>List
These are mutable ie. their values can be changed when necessary. The onyl difference is their brackets {}
l1 = {1, 2, "Hello"}
l1
>Dictionary
sets the definition of one with another. And are immutable.

dict1 = {"a":1, 2:"Hi"}
dict1
>Set
A set is a built-in data type that stores an unordered collection of unique elements. Sets are mutable.
s1 = set({1, 2, 1, "Hello"})
s1
>Control flow
#if else
a = 10
b = 20
if(a>b):
    print("a is greater")
else:
    print("b is greater")
#switch cases
cmd = "start"
match cmd:
    case "start":
        print("Start the game.")
    case "stop":
        print("Stop the game.")
#for loop
for i in range(10):
    print(i)
>Functions and Modules
def hello():
    print("Hello")

hello()
a = np.array([1,2,3,4])
a
from cmath import sin

a = sin(10)
print(a)
import math
a = math.sqrt(18)
print(a)
>Error handling
a = -2
try:
    if a<0:
        raise ValueError("Cannot find the squareroot of negative number")

    b = math.sqrt(a)
    print(b)

except ValueError as e:
    print(e)

try:
    c = 10/0
    raise ValueError("Cannot divide by zero")

except ZeroDivisionError as e:
    print("Caught a ZeroDivisionError: ", e)
except ValueError as e:
    print("Caught a ValueError: ", e)
finally:
    print("The error is of another source or handle compeltely.")
>Numerical and scientific computations
a = np.array([[1,2,3], [5,6,7]])

b = np.array([[23,7,3], [8,6,9]])

c = np.array([[4,5],[6,7],[9,0]])
d = np.dot(a,c)
d
e = a@c
e
f = a+b
f
g = a * 2
g
h = a+c.T
h
a = np.array([1,2,3])
b = 5

result = a + b
print(result)
a = np.array([[1,2,3], [4,5,6]])
b = np.array([10, 20, 30])

result = a+b
print(result)
a = np.array([[1,2,3], [4,5,6]])
b = np.array([[10], [20]])

result = a+b
print(result)
>Visualization and plotting
%matplotlib inline
import matplotlib.pyplot as plt

x = [0, 1, 2 ,3]
y = [0, 1, 4, 9]

plt.plot(x, y)
plt.show()
>Make a plot of the function f(x) = x^2 for -5 <= x <= 5
%matplotlib inline
x = np.linspace(-5, 5, 100)
plt.plot(x, x**2)
plt.show()
>Make a plot of the function f(x)=x^2 and g(x)=x^3 for -5 <= x <= 5. Use different colors and markers for each function.
x = np.linspace(-5, 5, 20)
plt.plot(x, x**2, "ko")
plt.plot(x, x**3, "r*")
plt.show()
plt.figure(figsize = (10,6))
x = np.linspace(-5,5,100)
plt.plot(x, x**2, "ko", label = "quadratic")
plt.plot(x, x**3, "r*", label = "cubic")
plt.title(f"Plot of Various Polynomials from {x[0]} to {x[-1]}")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend(loc = 2)
plt.xlim(-6.6)
plt.ylim(-10,10)
plt.grid()
plt.show()
>Given the lists x = np.arange(11) and y = x**2, create a 2 × 3 subplot where each subplot plots x versus y using plot, scatter, bar, loglog, semilogx, and semilogy. Title and label each plot appropriately. Use gird, but a legend is not necessary here.
x = np.arange(11)
y = x**2
plt.figure(figsize = (14, 8))
plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.subplot(2, 3, 2)
plt.scatter(x, y)
plt.title("scatter")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.subplot(2, 3, 3)
plt.bar(x, y)
plt.title("bar")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.subplot(2, 3, 4)
plt.loglog(x, y)
plt.title("loglog")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.subplot(2, 3, 5)
plt.semilogx(x, y)
plt.title("semilogx")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(which="both")
plt.subplot(2, 3, 6)
plt.semilogy(x, y)
plt.title("semilogy")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.tight_layout()
plt.show()

>3D plotting
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-poster")
fig = plt.figure(figsize = (10, 10))

ax = plt.axes(projection = "3d")

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X,Y = np.meshgrid(x,y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap='viridis')

plt.show()# LAB 1
Rohan Singh
<br>KCE080BCT033
Basics of python programming
import numpy as np
>Basic Input Output
b = 2
print(b)
string1 = "Hi I am Rohan Singh"
print(string1[1:3])
n = input("Enter the number: ")
print(n)
>Tuples
These are not mutable. Once set its set.
tup = ("Hello", 1, 2, 3,"mic check")
tup
>List
These are mutable ie. their values can be changed when necessary. The onyl difference is their brackets {}
l1 = {1, 2, "Hello"}
l1
>Dictionary
sets the definition of one with another. And are immutable.

dict1 = {"a":1, 2:"Hi"}
dict1
>Set
A set is a built-in data type that stores an unordered collection of unique elements. Sets are mutable.
s1 = set({1, 2, 1, "Hello"})
s1
>Control flow
#if else
a = 10
b = 20
if(a>b):
    print("a is greater")
else:
    print("b is greater")
#switch cases
cmd = "start"
match cmd:
    case "start":
        print("Start the game.")
    case "stop":
        print("Stop the game.")
#for loop
for i in range(10):
    print(i)
>Functions and Modules
def hello():
    print("Hello")

hello()
a = np.array([1,2,3,4])
a
from cmath import sin

a = sin(10)
print(a)
import math
a = math.sqrt(18)
print(a)
>Error handling
a = -2
try:
    if a<0:
        raise ValueError("Cannot find the squareroot of negative number")

    b = math.sqrt(a)
    print(b)

except ValueError as e:
    print(e)

try:
    c = 10/0
    raise ValueError("Cannot divide by zero")

except ZeroDivisionError as e:
    print("Caught a ZeroDivisionError: ", e)
except ValueError as e:
    print("Caught a ValueError: ", e)
finally:
    print("The error is of another source or handle compeltely.")
>Numerical and scientific computations
a = np.array([[1,2,3], [5,6,7]])

b = np.array([[23,7,3], [8,6,9]])

c = np.array([[4,5],[6,7],[9,0]])
d = np.dot(a,c)
d
e = a@c
e
f = a+b
f
g = a * 2
g
h = a+c.T
h
a = np.array([1,2,3])
b = 5

result = a + b
print(result)
a = np.array([[1,2,3], [4,5,6]])
b = np.array([10, 20, 30])

result = a+b
print(result)
a = np.array([[1,2,3], [4,5,6]])
b = np.array([[10], [20]])

result = a+b
print(result)
>Visualization and plotting
%matplotlib inline
import matplotlib.pyplot as plt

x = [0, 1, 2 ,3]
y = [0, 1, 4, 9]

plt.plot(x, y)
plt.show()
>Make a plot of the function f(x) = x^2 for -5 <= x <= 5
%matplotlib inline
x = np.linspace(-5, 5, 100)
plt.plot(x, x**2)
plt.show()
>Make a plot of the function f(x)=x^2 and g(x)=x^3 for -5 <= x <= 5. Use different colors and markers for each function.
x = np.linspace(-5, 5, 20)
plt.plot(x, x**2, "ko")
plt.plot(x, x**3, "r*")
plt.show()
plt.figure(figsize = (10,6))
x = np.linspace(-5,5,100)
plt.plot(x, x**2, "ko", label = "quadratic")
plt.plot(x, x**3, "r*", label = "cubic")
plt.title(f"Plot of Various Polynomials from {x[0]} to {x[-1]}")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend(loc = 2)
plt.xlim(-6.6)
plt.ylim(-10,10)
plt.grid()
plt.show()
>Given the lists x = np.arange(11) and y = x**2, create a 2 × 3 subplot where each subplot plots x versus y using plot, scatter, bar, loglog, semilogx, and semilogy. Title and label each plot appropriately. Use gird, but a legend is not necessary here.
x = np.arange(11)
y = x**2
plt.figure(figsize = (14, 8))
plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.subplot(2, 3, 2)
plt.scatter(x, y)
plt.title("scatter")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.subplot(2, 3, 3)
plt.bar(x, y)
plt.title("bar")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.subplot(2, 3, 4)
plt.loglog(x, y)
plt.title("loglog")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.subplot(2, 3, 5)
plt.semilogx(x, y)
plt.title("semilogx")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(which="both")
plt.subplot(2, 3, 6)
plt.semilogy(x, y)
plt.title("semilogy")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.tight_layout()
plt.show()

>3D plotting
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-poster")
fig = plt.figure(figsize = (10, 10))

ax = plt.axes(projection = "3d")

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X,Y = np.meshgrid(x,y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap='viridis')

plt.show()