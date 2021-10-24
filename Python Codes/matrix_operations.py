class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.l = [[0 for i in range(n)] for j in range(m)]
        self.chck = 0

    def getmat(self):
        print("Enter the matrix: ")
        for i in range(self.m):
            x = True
            while x:
                l1 = list(map(int, input().split()))
                if len(l1) != self.n:
                    print("Invalid Input!! Enter the row again.")
                    continue
                else:
                    x = False
                    for j in range(self.n):
                        self.l[i][j] = l1[j]

    def write(self):
        if self.chck != 0:
            print("Invalid operation!")
        else:
            for i in range(self.m):
                for j in range(self.n):
                    print(self.l[i][j], end=" ")
                print()

    def addmat(self, m1):
        mx = Matrix(self.m, self.n)
        if m1.m != self.m and m1.n != self.n:
            mx.chck = 1
            return mx
        for i in range(self.m):
            for j in range(self.n):
                mx.l[i][j] = self.l[i][j] + m1.l[i][j]
        return mx

    def submat(self, m1):
        mx = Matrix(self.m, self.n)
        if m1.m != self.m and m1.n != self.n:
            mx.chck = 1
            return mx
        for i in range(self.m):
            for j in range(self.n):
                mx.l[i][j] = self.l[i][j] - m1.l[i][j]
        return mx

    def mulmat(self, m1):
        mx = Matrix(self.m, m1.n)
        if self.n != m1.m:
            mx.chck = 1
            return mx
        for i in range(mx.m):
            for j in range(mx.n):
                for k in range(self.n):
                    mx.l[i][j] += self.l[i][k] * m1.l[k][j]
        return mx

    def transpose(self):
        mx = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                mx.l[i][j] = self.l[j][i]
        return mx


m, n = map(int, input("Enter the dimensions of the first Matrix separated by whitespace: ").split())
m1 = Matrix(m, n)
m1.getmat()
x, y = map(int, input("Enter the dimensions of the second Matrix separated by whitespace: ").split())
m2 = Matrix(x, y)
m2.getmat()
while True:
    print("-" * 150)
    print("Enter your choice number from the following")
    print("1. Addition of two matrices\n2. Subtraction of two matrices\n3. Multiplication of two matrices\n4. "
          "Transpose of a matrix\n5. Re-enter the matrices.\n6. Exit.")
    ch = int(input(">>"))
    if ch == 1:
        m1.addmat(m2).write()
    elif ch == 2:
        m1.submat(m2).write()
    elif ch == 3:
        m1.mulmat(m2).write()
    elif ch == 4:
        print("Transpose of first Matrix: ")
        m1.transpose().write()
        print("Transpose of second Matrix: ")
        m2.transpose().write()
    elif ch == 5:
        m, n = map(int, input("Enter the dimensions of the Matrix separated by whitespace: ").split())
        m1 = Matrix(m, n)
        m1.getmat()
        x, y = map(int, input("Enter the dimensions of the second Matrix separated by whitespace: ").split())
        m2 = Matrix(x, y)
        m2.getmat()
    elif ch == 6:
        break
    else:
        print("Invalid Input")
