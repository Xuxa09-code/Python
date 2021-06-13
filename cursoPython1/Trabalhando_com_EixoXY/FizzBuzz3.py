def main():
    number = int(input('Entre com um numero: '))
    if number%5 == 0 and number%3 == 0:
        print('FizzBuzz')
    else:
        print(number)
main()