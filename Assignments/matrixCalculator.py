'''
Created by Eli Murphy

Date: 6 December 2022


'''
from cv2 import determinant


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
            return ArithmeticError("Matrix cannot be added to selected matrix.")                       # Raises error
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
            return ArithmeticError("Matrix cannot be multiplied to selected matrix.")
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
        matrix = self.data
        for x in range(min(len(matrix), len(matrix[0]))):                                              # iterates through the rows of the matrix
            for row in range(x, len(matrix)):                                                          # iterates through the columns of the matrix
                if matrix[row][x] == 0:                                                                # checks if the current element is 0. 
                    continue                                                                           # If it is, the function continues to the next iteration of the loop.
                
                matrix[x], matrix[row] = matrix[row], matrix[x]                                        # swaps the current row with the row that has the first non-zero element in the current column
                
                varRowCol = matrix[x][x]
                
                for row2 in range(x+1, len(matrix)):                                                   # iterates through the rows of the matrix
                    selectrow = matrix[row2][x]           
                    multiplier = -1 * selectrow / varRowCol                                            # calculates a multiplier for the current row 
                    for col2 in range(x, len(matrix[0])):                                              # iterates through the columns of the matrix
                        matrix[row2][col2] += matrix[x][col2] * multiplier                             # adds the current row multiplied by the multiplier to the current row.
                break

        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                matrix[i][j] = round(matrix[i][j],3)                                                   # rounds the current element to 3 decimal places

        output = Matrix(matrix)
        return output

    def inverse(self):
        if self.r != self.c:
            return "Error: matrix is not square"

        determinant = self.determinant()
        # ... (code to calculate determinant)

        print(determinant)

        if determinant == 0:
            return "Error: matrix does not have an inverse"

        adjoint = []
        # ... (code to calculate adjoint)

        inverse = []
        for row in adjoint:
            inverse_row = []
            for element in row:
                inverse_row.append(element / determinant)
            inverse.append(inverse_row)

        return inverse
    def determinant(self):
        # Check if the matrix is square
        
        # Check if the matrix has a size of 1x1
        if self.r == 1:
            return self.data[0][0]

        # Check if the matrix has a size of 2x2
        if self.r == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        # For matrices larger than 2x2, we use Laplace expansion
        det = 0
        for i in range(self.r):
            # Create a submatrix by removing the ith row and column
            submatrix = [[self.data[j][k] for k in range(self.r) if k != i] for j in range(1, self.r)]
            # Use the Laplace expansion formula to compute the determinant
            det += (-1) ** i * self.data[0][i] * Matrix(submatrix).determinant()

        return det



def main():
    m2 = Matrix([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
    m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    while True:
        menuOpt = input("Start Code: ")
        if menuOpt == "printM":
            m1.printMatrix()
        elif menuOpt == "plusM":
            out = m1.plusMatrix(m2)
            if str(type(out)) == "<class 'ArithmeticError'>":
                print(out)
            else:
                out.printMatrix()
        elif menuOpt == "timesM":
            out = m1.timesMatrix(m2)
            if str(type(out)) == "<class 'ArithmeticError'>":
                print(out)
            else:
                out.printMatrix()
        elif menuOpt == "STR":
            out = m1.scalarTimesRow(scalar= float(input("Scalar: ")), rownumber=(int(input("Row: "))-1))
            out.printMatrix()
        elif menuOpt == "sR":
            out = m1.switchRows(row1=(int(input("Row 1: "))-1), row2=(int(input("Row 1: "))-1))
            if str(type(out)) == "<class 'ArithmeticError'>":
                print(out)
            else:
                out.printMatrix()
        elif menuOpt == "lCR":
            out = m1.linearCombRows(2, row1=(int(input("Row 1: "))-1), row2=(int(input("Row 1: "))-1))
            out.printMatrix()
        elif menuOpt == "ref":
            out = m2.ref()
            out.printMatrix()
        elif menuOpt == "inv":
            out = m1.inverse()
            if type(out) == str:
                print(out)
            else:
                out.printMatrix()

if __name__ == '__main__':
    main()