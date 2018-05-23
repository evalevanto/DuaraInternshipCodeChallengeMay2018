
def division(dividend, divider):
    QUOTIENT = 0
    while (dividend >= divider):
        QUOTIENT += 1
        dividend -= divider
        
    print QUOTIENT
    print ("Remainder: %d"%(dividend))
    


if __name__ == "__main__":
    DIVIDEND = int(input("Enter your number: "))
    DIVIDER = int(input("Divide your number by: "))
    division(DIVIDEND, DIVIDER)