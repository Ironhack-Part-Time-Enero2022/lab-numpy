#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)
print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a1 = np.random.random_sample((2,3,5)) #floats entre el 0 y el 1 (excluido el 1 entero)
a2 = np.random.randint(0,100, (2,3,5)) #numeros enteros en un rango dado
a3 = np.random.rand(2,3,5) #igual que el primero pero incluye el 1 entero

#4. Print a.

print(a1)
print(a2)
print(a3)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3), dtype=int)

#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

(a1.shape) == (b.shape)

#8. Are you able to add a and b? Why or why not?

#a1 + b or np.add(a1, b)
#not possible to add a1, b because they have different size/shape
#ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3)

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b, (1,2,0))

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a1, c) #it works because both shapes match

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a1, d) #decimals of elements for each array are the same, difference is that integrer of d is 1 and a1 has no integrer (zero)

#12. Multiply a and c. Assign the result to e.

e = np.multiply(a1, c) #or a1 * c

#13. Does e equal to a? Why or why not?

e == a1 #they are arrays with the same values, because e is the result of multiply a1 * c (where c is an array with the same shape but all elements are 1)

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for arrays in range(d.shape[0]):
    for rows in range(d.shape[1]):
        for columns in range(d.shape[2]):
            if d[arrays][rows][columns] > d_min and d[arrays][rows][columns] < d_mean:
                f[arrays][rows][columns] = 25
            elif d[arrays][rows][columns] > d_mean and d[arrays][rows][columns] < d_max:
                f[arrays][rows][columns] = 75
            elif d[arrays][rows][columns] == d_mean:
                f[arrays][rows][columns] = 50
            elif d[arrays][rows][columns] == d_min:
                f[arrays][rows][columns] = 0
            elif d[arrays][rows][columns] == d_max:
                f[arrays][rows][columns] = 100

"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print(d)
print(f)

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

listas_ejemplo = [[["x","x","x","x","x"],["x","x","x","x","x"],["x","x","x","x","x"]],[["x","x","x","x","x"],["x","x","x","x","x"],["x","x","x","x","x"]]]
g = np.array(listas_ejemplo)

for arrays in range(d.shape[0]):
    for rows in range(d.shape[1]):
        for columns in range(d.shape[2]):
            if d[arrays][rows][columns] > d_min and d[arrays][rows][columns] < d_mean:
                g[arrays][rows][columns] = "B"
            elif d[arrays][rows][columns] > d_mean and d[arrays][rows][columns] < d_max:
                g[arrays][rows][columns] = "D"
            elif d[arrays][rows][columns] == d_mean:
                g[arrays][rows][columns] = "C"
            elif d[arrays][rows][columns] == d_min:
                g[arrays][rows][columns] = "A"
            elif d[arrays][rows][columns] == d_max:
                g[arrays][rows][columns] = "E"

print(g)