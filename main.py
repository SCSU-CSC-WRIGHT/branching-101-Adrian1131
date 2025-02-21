"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""

def findTotal():
    total = 0
    for i in range(5):
        number = int(input("Enter a number: "))
        total += number
    return total

def main():
    total =  findTotal()
    print("The running total is: ", total)
    
    
main()