arr_1d = [53, 78, 90, 12, 15, 65, 44, 32, 29, 36]

# 1. Print 3rd and 9th element of the array.
# 2. Change  3rd and 9th element to 100.

import numpy as np

a = np.array( [53, 78, 90, 12, 15, 65, 44, 32, 29, 36])
print(a[2])
print(a[8])

a[2] = 100
a[8] = 100
print(a)

# -------------------------------------------------------------------------------------------

#  Given a 3x3 array, change all the diagonal elements of the matrix to 0

arr_2d = np.array([ [1,2,3],
                    [4,5,6],
                    [7,8,9]])

for i in range(3):
    for j in range(3):
        if i == j:
            arr_2d[i][j] = 0
        else:
            pass

print(arr_2d)

# -------------------------------------------------------------------------------------------

# Write a program to find the number of rows and columns present in the matrix given below. Note: Initialize the matrix using NumPy.

A= np.array([[9,5,6,1,-2],
            [3,-8,1,2,0],
            [6,9,3,3,5]])

rows = len(A)
cols = len(A[0])

print('number of rows = ',rows)
print('number of columns = ',cols)


# -------------------------------------------------------------------------------------------

# Print each element of the following matrix. Initialize the matrix using NumPy.
# Also, multiply the matrix with n = 150 and print the matrix after multiplication.

B= np.array([[-8,0,2,4],[5,2,-1,7]])

c = np.zeros([2 , 4])

count = 1

for i in range(2):
    for j in range(4):
        c[i][j] = B[i][j]*150
        
        if count<= 10 :
            print('Element ',count,' is ', B[i][j])
            count+=1


print(c)



