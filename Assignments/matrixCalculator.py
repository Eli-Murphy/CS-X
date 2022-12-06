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
        newmat.printMatrix()
        
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
        newmat.printMatrix()

    def scalarTimesRow(self, scalar, rownumber):
        if rownumber > self.r:                                                                         # Checks that the row to be multiplied exists
            raise ArithmeticError("Error: Selected row does not exist.")
        newmat = Matrix(self.r,self.c, self.data)
        for i in range(len(self.data[rownumber])):
            newmat.data[rownumber][i] = newmat.data[rownumber][i] * scalar
        newmat.printMatrix()

    def switchRows(self, row1, row2):                                                                  
        if row1 > self.r or row2 > self.r:                                                             # Checks to see if rows selected exist
            raise ArithmeticError("Error: Selected row/rows does not exist.")
        row1d, row2d = self.data[row1], self.data[row2]                                                # Holds row data
        newmat = Matrix(self.r, self.c, self.data)                                                     # Copies self matrix to new matrix
        newmat.data[row1],newmat.data[row2] = self.data[row2], self.data[row1]                         # Switches rows on new matrix
        newmat.printMatrix()

def main():
    m2 = Matrix(3,3, [[1,2,3],[4,5,6],[7,8,9]])
    m1 = Matrix(3,3, [[1,2,3],[4,5,6],[7,8,9]])
    while True:
        menuOpt = input("Start Code: ")
        if menuOpt == "printM":
            m1.printMatrix()
        elif menuOpt == "plusM":
            m1.plusMatrix(m2)
        elif menuOpt == "timesM":
            m1.timesMatrix(m2)
        elif menuOpt == "STR":
            m1.scalarTimesRow(scalar= int(input("Scalar: ")), rownumber=(int(input("Row: "))-1))
        elif menuOpt == "sR":
            m1.switchRows(row1=(int(input("Row 1: "))-1), row2=(int(input("Row 1: "))-1))
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