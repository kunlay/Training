from Function import nextPrime

def startPrime(number):
    next_prime_number = nextPrime(number)
    print(next_prime_number)
    while True:
        user_ques = input('do u want to continue, y/n')
        if user_ques == 'n':
            return 'Thank You'
        else:
            next_prime_number = nextPrime(next_prime_number)
            print(next_prime_number)
    print(next_prime_number)