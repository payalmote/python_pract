class calculator:
    def __init__(self, n):
        self.n = n
    def sq(self):
        print(f"the square of number: {self.n ** 2}")
    def cube(self):
        print(f"The cube of number: {self.n ** 3}")
    def sqrt(self):
        print(f"Square root of number: {self.n ** 0.5}")

n = int(input("Enter the number: "))
num = calculator(n)
num.sq()
num.cube()
num.sqrt()