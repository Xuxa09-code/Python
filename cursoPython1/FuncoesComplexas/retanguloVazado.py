def main():
    largura = int(input('digite a largura: '))
    altura = int(input('digite a altura: '))
    i = j = 0
    while i < altura:
        j = 0
        while j < largura:
            if i == 0 or i == altura - 1:
                print('#',end='')
            else:
                if j == 0 or j == largura - 1:
                    print('#',end='')
                else:
                    print(' ', end='')
            j += 1
        i += 1
        print()
main()