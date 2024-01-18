def calcuate(numbers):
    """we calculate pi and show {numbers} after the point"""
    if (numbers <= 0):
        print("3")
        return
    
    up = 22
    base = 7
    reset = 0
    count = 0
    while count < numbers:
        print (up / base)
        rest = up % base
        print (rest)
        count += 1

if __name__ == "__main__":
    """read user input"""
    numbers = input("how many digit after the point you want")
    calcuate(int(numbers))