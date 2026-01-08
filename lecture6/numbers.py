import math
class Computation:
    def factorial(self, number):
        return math.factorial(number)
    def sum(self, number):
        return sum(range(1, number + 1))
    def tableMult(self, number):
        table = []
        for i in range(1, 11):
            table.append(f"{i} x {number} = {number * i}")
        return table
    def listDiv(self, number):
        divisors = []
        for i in range(1, number + 1):
            if number % i == 0:
                divisors.append(i)
        return divisors

Compute = Computation()
print(Compute.factorial(5))
print(Compute.sum(5))
print(Compute.tableMult(5))
print(Compute.listDiv(5))