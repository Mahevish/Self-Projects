#InternSearch - Day 2

"""
1) How to check if a given number is a power of 2 ?
2) Count the number of ones in the binary representation of the given number.
3) Check if the i th bit is set in the binary form of the given number.

Extra Questions:
4) How to generate all the possible subsets of a set ?
5) Find the largest power of 2 (most significant bit in binary form),
which is less than or equal to the given number N.
"""

#1) How to check if a given number is a power of 2 ?

def checkpower2():
    import math
    print("Check if number is a power of 2")
    x = int(input("Enter a number\n"))
    if math.log2(x) == int(math.log2(x)):
        print("Number is a power of 2")
    else:
        print("Number is not a power of 2")


#2) Count the number of ones in the binary representation of the given number.

def countonesinbinary():
    print("*" * 50)
    print("Count number of 1s in binary number")
    num1 = int(input("Enter a number\n"))
    def converttobinary(num1):
        return bin(num1).replace("0b","")

    x = converttobinary(num1)
    count = 0
    for each in x:
        if each == '1':
            count += 1

    return f"Count of 1s in {num1}'s binary number {x} is {count}"


def main():
    checkpower2()
    x = countonesinbinary()
    print(x)


if __name__ == "__main__":
    main()


