'''
Created by Eli Murphy

Date: 6 December 2022


'''
class Matrix:
    def __init__(self, r, c, data):
        self.data = data                                                                               # Defines matrix data
        self.r = r                                                                                     # Defines row count
        self.c = c                                                                                     # Defines column count

    def printMatrix(self):
        for i in self.data: 
            print(i)                                                                                   # Prints each row in the matrix seperatly

    def plusMatrix(self, addmat):
        if addmat.r != self.r or addmat.c != self.c:                                                   # Checks to make sure matrix dimensions match, otherwise cannot be added 
            raise ArithmeticError("Matrix cannot be added to selected matrix.")                        # Raises error
        newmat = Matrix(addmat.r, addmat.c, [[0 for x in range(addmat.c)] for y in range(addmat.r)])   # Generates new matrix class for output
        for i in range(addmat.r):                                                                      
            for j in range(addmat.c):
                newmat.data[i][j] = self.data[i][j] + addmat.data[i][j]                                # For each row and for each columb, the output is the same coordinate of both matricies added
        return newmat
        
    def timesMatrix(self, multmat):                                                                             
        if self.c != multmat.r:
            raise ArithmeticError("Matrix cannot be multiplied to selected matrix.")
        newmat = Matrix(self.r, multmat.c, [[0 for x in range(multmat.c)] for y in range(self.r)])     # Creates a zero array with the amount of rows as the first matrix and the amount of columbs as the second
        for i in range(self.r):                                                                        # For the amount of rows in the first
            for j in range(multmat.c):                                                                 # For the amount of columbs in the second
                x = 0                                                                                  # Multiplication output placeholder 
                for k in range(self.c):                                                                # For the amount of columbs in the first 
                    x += self.data[i][k] * multmat.data[k][j]                                          # placeholder plus the value at the position on the first matrix times the value at the position to be added to it
                newmat.data[i][j] = x                                                                  # Sets the new matrix position with the placeholder
        return newmat

    def scalarTimesRow(self, scalar, rownumber):
        if rownumber > self.r:                                                                         # Checks that the row to be multiplied exists
            raise ArithmeticError("Error: Selected row does not exist.")
        newmat = Matrix(self.r,self.c, self.data)
        for i in range(len(self.data[rownumber])):
            newmat.data[rownumber][i] = newmat.data[rownumber][i] * scalar
        return newmat

    def switchRows(self, row1, row2):                                                                  
        if row1 > self.r or row2 > self.r:                                                             # Checks to see if rows selected exist
            raise ArithmeticError("Error: Selected row/rows does not exist.")
        row1d, row2d = self.data[row1], self.data[row2]                                                # Holds row data
        newmat = Matrix(self.r, self.c, self.data)                                                     # Copies self matrix to new matrix
        newmat.data[row1],newmat.data[row2] = self.data[row2], self.data[row1]                         # Switches rows on new matrix
        return newmat

    def linearCombRows(self, scalar, row1, row2):
        return (self.scalarTimesRow(scalar, row1)).scalarTimesRow(scalar, row2)
    
    def invert_matrix(self):

        det = 0
        for j in range(len(self.data)):
            sign = (-1) ** (1 + j)
            submatrix = [self.data[i][:j] + self.data[i][j+1:] for i in range(1, len(self.data))]
            det += sign * self.data[0][j] * Matrix(len(submatrix), len(submatrix[0]), submatrix).invert_matrix()

        # If the determinant is zero, the matrix is not invertible
        if det == 0:
            return None

        # Calculate the inverse of the matrix by taking the adjoint of the matrix
        # and dividing it by the determinant
        inverse = [[0 for j in range(len(self.data))] for i in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                sign = (-1) ** (i + j)
                submatrix = [self.data[k][:j] + self.data[k][j+1:] for k in range(len(self.data)) if k != i]
                inverse[i][j] = sign * Matrix(len(submatrix), len(submatrix[0]), submatrix).invert_matrix() / det 
        print(inverse)
        return inverse

def main():
    m2 = Matrix(3,3, [[1,2,3],[4,5,6],[7,8,9]])
    m1 = Matrix(3,3, [[1,2,3],[4,5,6],[7,8,9]])
    while True:
        menuOpt = input("Start Code: ")
        if menuOpt == "printM":
            m1.printMatrix()
        elif menuOpt == "plusM":
            out = m1.plusMatrix(m2)
            out.printMatrix()
        elif menuOpt == "timesM":
            put = m1.timesMatrix(m2)
            out.printMatrix()
        elif menuOpt == "STR":
            out = m1.scalarTimesRow(scalar= int(input("Scalar: ")), rownumber=(int(input("Row: "))-1))
            out.printMatrix()
        elif menuOpt == "sR":
            out = m1.switchRows(row1=(int(input("Row 1: "))-1), row2=(int(input("Row 1: "))-1))
            out.printMatrix()
        elif menuOpt == "lCR":
            out = m1.linearCombRows(2, row1=(int(input("Row 1: "))-1), row2=(int(input("Row 1: "))-1))
            out.printMatrix()
        elif menuOpt == "inv":
            out = m1.invert_matrix()
            out.printMatrix()
    #m1.timesMatrix(m2)
    #m1.scalarTimesRow(2,2)
    #m1.switchRows(1,2)
    #m1.plusMatrix(m2)


    # print("Eli Murphy Matrix Calculator\n\nInput matrix (n,n,n/n,n,n/n,n,n):\n")
    # matrixinput = input()
    # matrixinput = matrixinput.split("/")
    # m1 = []
    # for i in matrixinput:
    #     m1.append(i.split(","))
    # print(m1)



if __name__ == '__main__':
    main()