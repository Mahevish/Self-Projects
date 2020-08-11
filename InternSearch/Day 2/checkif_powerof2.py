#1) How to check if a given number is a power of 2 ?

def checkpower2():
    print("Check if number is a power of 2")
    n = int(input("Enter a number\n"))
    if (n&(n-1)) == 0:
        print(f"{n} is a power of 2.")
    else:
        print(f"{n} is not a power of 2.")
        
def main():
   checkpower2()        

if __name__ =="__main__":
    main()
    
    
    