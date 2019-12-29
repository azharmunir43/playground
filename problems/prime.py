
class PrimeNumberChecker:

    def is_prime(self, number : int = 0) -> bool:

        for d in range(2, number // 2):
             if number % d == 0:
                 print('%d is divisible by %d as ' % (number, d))
                 return False
        return True and number != 0

    def get_primes(self, start : int = 0, end : int = 0) -> list:
        pass

if __name__ == '__main__':
    # primeNumberChecker = PrimeNumberChecker()
    # print(primeNumberChecker.is_prime(0))

    with open('Gradebook RU.sql', 'r') as ru:
        for line in ru.readlines():
            if 'CREATE TABLE ' in line:
                table = line.split('CREATE TABLE')[-1].strip('\n')
                print(table)
