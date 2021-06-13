def main():
    largura = int(input('digite a largura: '))
    altura = int(input('digite a altura: '))
    i = j = 0
    while i < altura:
        j = 0
        while j < largura:
            print('#',end='')
            j += 1
        i += 1
        print()
main()