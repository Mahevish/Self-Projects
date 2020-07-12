class Fibonacci():
    def __init__(self, num):
        self.num = num
        self.n1 = 0
        self.n2 = 1

        self.list1 = []
        self.count = 0

    def calc(self):
        while self.count < self.num:
            self.list1.append(str(self.n1))
            self.nth = self.n1 + self.n2
            #self.list1.append(str(self.nth))
            self.n1 = self.n2
            self.n2 = self.nth
            self.count += 1

        print(f"Fibonacci sequence till {self.num} is {','.join(self.list1)}")

def main():
    a = Fibonacci(7)
    a.calc()

if __name__ == "__main__":
    main()


