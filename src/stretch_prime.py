

def find_prime():
    '''
    function will determine if a number, given on the command line, is prime using The Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one of the oldest algorithms known (ca. 200 BC).
    '''
    # create a list of numbers from 2 to the input (example: 30)
    # 2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

    # take first number in list (example: 2)
    # i = 2

    # remove every 2nd number in the list after 2 by counting by increments of 2 (all of its multiples)
    # 4 6 8 10 12 14 16 18 20 22 24 26 28 30
    # left over: 2 3 5 7 911 13 15 17 19 21 23 25 27 29

    # go to the next number
    # i = 3

    # remove every 3rd number in the list after 3 by counting by increments of 3 (all of its multiples)
    # 9 15 21 27
    # left over: 2 3 5 7 11 13 17 19 23 25 29

    # go to the next number
    # i = 5

    # remove every 5th number in the list after 5 by counting by increments of 5 (all of its multiples)
    # 25
    # left over: 2 3 5 7 11 13 17 19 23 29

    # go to the next number 
    # i = 7

    # 7 * 7 > 30 
    # stop

    cmd = input('What number would you like to check? --> ')
    n = int(cmd)
    numbers = [i for i in range(2, n + 1)]

    index = 0
    current = numbers[index]

    if current ** 2 > n:
        return numbers
    while current ** 2 < n:
        if index != len(numbers):
            for i in range(index + current, len(numbers)):
                if i >= len(numbers):
                    break
                if numbers[i] % current == 0:
                    numbers.pop(i)
            index += 1
            current = numbers[index]
    print(numbers)
    return find_prime()

print(find_prime())