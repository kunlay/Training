# getting the next Prime Number after a given number
# number = int(input('enter a number? \n'))
def isPrime(number):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                return False
        else:
            return True
def nextPrime(number):
    while True:
        number+=1
        if isPrime(number):
            return number