'''
Created by Eli Murphy

Date: 6 December 2022
'''

class Matrix:
    def __init__(self, data):
        '''
        This initiates a class "Matrix"

        :param list data: A 2D array that will be made as a class object
        '''
        self.data = data                                                                               # Defines matrix data
        self.r = len(data)                                                                             # Defines row count
        self.c = len(data[0])                                                                          # Defines column count

    def printMatrix(self):
        '''
        This function prints a matrix in a orderly and a more user friendly way rather than a regular list
        '''
        for i in self.data: 
            print(i)                                                                                   # Prints each row in the matrix seperatly

    def plusMatrix(self, addmat):
        '''
        This function adds a matrix to another matrix

        :param list addmat: The matrix to be added
        '''
        if addmat.r != self.r or addmat.c != self.c:                                                   # Checks to make sure matrix dimensions match, otherwise cannot be added 
            return "Matrix cannot be added to selected matrix."                                        # Returns error
        newmat = Matrix([[0 for x in range(addmat.c)] for y in range(addmat.r)])                       # Generates new matrix class for output
        for i in range(addmat.r):                                                                      
            for j in range(addmat.c):
                newmat.data[i][j] = self.data[i][j] + addmat.data[i][j]                                # For each row and for each columb, the output is the same coordinate of both matricies added
        return newmat
        
    def timesMatrix(self, multmat):    
        '''
        This function multiplies a matrix to another matrix

        :param list multmat: The multiplier matrix
        '''                                                                         
        if self.c != multmat.r:
            return "Matrix cannot be multiplied to selected matrix."
        newmat = Matrix([[0 for x in range(multmat.c)] for y in range(self.r)])                        # Creates a zero array with the amount of rows as the first matrix and the amount of columbs as the second
        for i in range(self.r):                                                                        # For the amount of rows in the first
            for j in range(multmat.c):                                                                 # For the amount of columbs in the second
                x = 0                                                                                  # Multiplication output placeholder 
                for k in range(self.c):                                                                # For the amount of columbs in the first 
                    x += self.data[i][k] * multmat.data[k][j]                                          # placeholder plus the value at the position on the first matrix times the value at the position to be added to it
                newmat.data[i][j] = x                                                                  # Sets the new matrix position with the placeholder
        return newmat

    def scalarTimesRow(self, scalar, rownumber):
        '''
        This function multiplies a float to a specific row of a matrix

        :param float scalar: number to be multiplied to a row
        :param int rownumber: row number that will be multiplied
        '''
        if rownumber > self.r:                                                                         # Checks that the row to be multiplied exists
            raise ArithmeticError("Error: Selected row does not exist.")
        newmat = Matrix(self.data)
        for i in range(len(self.data[rownumber])):
            newmat.data[rownumber][i] = newmat.data[rownumber][i] * scalar
        return newmat

    def switchRows(self, row1, row2):
        '''
        This function switches two selected rows of a given matrix

        :param int row1: row to be swapped with row2
        :param int row2: row to be swaped with row1
        '''                                                                  
        if row1 > self.r or row2 > self.r:                                                             # Checks to see if rows selected exist
            return ArithmeticError("Error: Selected row/rows does not exist.")
        newmat = Matrix(self.data)                                                                     # Copies self matrix to new matrix
        newmat.data[row1],newmat.data[row2] = self.data[row2], self.data[row1]                         # Switches rows on new matrix
        return newmat

    def linearCombRows(self, scalar, row1, row2):
        '''
        This function multiplies two different rows of a matrix by the same multiplier

        :param float scalar: the number that will be multipled to the selected rows
        :param int row1: one of the rows that will be multiplied by the scalar
        :param int row2: one of the rows that will be multiplied by the scalar
        '''
        return (self.scalarTimesRow(scalar, row1)).scalarTimesRow(scalar, row2)                        # Returns the scalartimesrow function done twice

    def ref(self):
        '''
        This function finds the row echelon form of a given matrix
        '''
        #matrix = self.data
        for x in range(min(self.r, self.c)):                                                           # iterates through the rows of the matrix
            for row in range(x, self.r):                                                               # iterates through the columns of the matrix
                if self.data[row][x] == 0:                                                             # checks if the current element is 0. 
                    continue                                                                           # If it is, the function continues to the next iteration of the loop.
                
                self.data[x], self.data[row] = self.data[row], self.data[x]                            # swaps the current row with the row that has the first non-zero element in the current column
                
                varRowCol = self.data[x][x]
                
                for row2 in range(x+1, self.r):                                                        # iterates through the rows of the matrix
                    selectrow = self.data[row2][x]           
                    multiplier = -1 * selectrow / varRowCol                                            # calculates a multiplier for the current row 
                    for col2 in range(x, self.c):                                                      # iterates through the columns of the matrix
                        self.data[row2][col2] += self.data[x][col2] * multiplier                       # adds the current row multiplied by the multiplier to the current row.
                break

        for i in range(self.r):
            for j in range(self.c): 
                self.data[i][j] = round(self.data[i][j],3)                                             # rounds the current element to 3 decimal places

        output = Matrix(self.data)
        return output

    def inverse(self):
        '''
        Finds the inverse of a given matrix
        '''
        if self.r != self.c:                                                                           # Ensures the matrix is square, otherwise the inverse would be impossible
            return "Error: matrix is not square"

        determinant = self.determinant()                                                               # Calls a function to find the matrix's determinant

        if determinant == 0:
            return "Error: matrix does not have an inverse"                                            # Any matrix with a determinant of zero does not have an inverse

        adjugate = self.adjugate()                                                                     # Calls a function to find the adjugate matrix 
        

        inverse = []
        for r in range(self.r):                                                                             # for each row in the adjugate matrix
            inverse_row = []
            for e in r:                                                                                # for each element in the row
                inverse_row.append(e / determinant)                                                    # adds the element divided by the determinant to the row
            inverse.append(inverse_row)                                                                # adds the inverted row to the inverse matrix


        for i in range(len(inverse)):
            for j in range(len(inverse[0])): 
                inverse[i][j] = round(inverse[i][j],3)                                                 # Rounds each element to the inverse to the thousanths place

        return Matrix(inverse)

    def determinant(self):
        '''
        Finds the determinant of a given matrix
        '''        
        if self.r == 1:                                                                                # the determiant of a 1x1 matrix is the only element
            return self.data[0][0]

        if self.r == 2:                                                                                # the determinant of a 2x2 matrix is the difference between the product of the diagonals
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        det = 0                                                                                        
        for i in range(self.r):                                                                        # Iterates through each row
            submatrix = [[self.data[j][k] for k in range(self.r) if k != i] for j in range(1, self.r)] # Create a submatrix by removing the ith row and column
            det += (-1) ** i * self.data[0][i] * Matrix(submatrix).determinant()                       # Use the Laplace expansion formula to compute the determinant

        return det

    def adjugate(self):
        '''
        Finds the adjugate of a matrix 
        '''
        cofactors = []                                                                                 # First thing to do is to find the cofactors
        for i in range(self.r):                                                                        # Iterates through the rows of a matrix
            cofactor_row = []  
            for j in range(self.c):                                                                    # Iterates through the colomns of a matrix
                minor = [row[:j] + row[j+1:] for row in (self.data[:i]+self.data[i+1:])]               # calculate the minor matrix for the element at row i and column j
                minor_det = Matrix(minor).determinant()                                                # calls  the determinant function to find the determinat of the minor matrix
                cofactor = (-1)**(i+j) * minor_det                                                     # calculate the cofactor for the element at row i and column j
                cofactor_row.append(cofactor)
            cofactors.append(cofactor_row)
        
        adj = [[cofactors[j][i] for j in range(len(cofactors))] for i in range(len(cofactors[0]))]     # Calculate the adjugate by taking the transpose of the cofactor matrix

        return adj

def userMain():
    matrix1 = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]
    matrix2 = [[1,2,0],[-1,1,1],[1,2,3]]
    
    print("""Here are the options:
1) Print Matrix
2) Add Matrix to another Matrix
3) Multiply Matrix by a Matrix
4) Multiply Specific Matrix Row by A Number
5) Switch Two Rows on a Matrix
6) Multiply Two Specific Matrix Rows by A Number
7) Row Echelon Form of a Matrix
8) Inverse of a Matrix
    """)
    while True:
        opt = input("\nMenu Option (1-8): ")
        md = input("Which matrix would you like to work on? (1 or 2): ")
        print("\n")
        if md == "1": 
            mpri = Matrix(matrix1)
            msec = Matrix(matrix2)
        elif md == "2":
            mpri = Matrix(matrix2)
            msec = Matrix(matrix1)
        if opt == "1": #print
            mpri.printMatrix()
        elif opt == "2": #plus
            out = mpri.plusMatrix(msec)
            if type(out) == str:
                print(out)
            else:
                out.printMatrix()
        elif opt == "3": #multiply
            out = mpri.timesMatrix(msec)
            if type(out) == str:
                print(out)
            else:
                out.printMatrix()
        elif opt == "4": #RowScalar
            out = mpri.scalarTimesRow(scalar= float(input("Scalar: ")), rownumber=(int(input("Row: "))-1))
            out.printMatrix()
        elif opt == "5": #switchrow
            out = mpri.switchRows(row1=(int(input("Row 1: "))-1), row2=(int(input("Row 2: "))-1))
            if type(out) == str:
                print(out)
            else:
                out.printMatrix()
        elif opt == "6": #2rowscalar
            out = mpri.linearCombRows(scalar= float(input("Scalar: ")), row1=(int(input("Row 1: "))-1), row2=(int(input("Row 2: "))-1))
            out.printMatrix()
        elif opt == "7": #ref
            out = mpri.ref()
            out.printMatrix()
        elif opt == "8": #inverse
            out = mpri.inverse()
            if type(out) == str:
                print(out)
            else:
                out.printMatrix()
        

if __name__ == '__main__':
    print("Eli Murphy Matrix Calculator\n\n")
    userMain()


# Copyright (c) 2022 Elijah A. Murphy
# Distributed under the terms of the MIT License. 
# SPDX-License-Identifier: MIT
# This code is part of the Battleship project (https://github.com/Eli-Murphy/CS-X)