def multiply(a, b):
    return float(a) * float(b)
    
def main():
    a = input('Inserte primer numero ')
    b = input('Inserte segundo numero ')
    res = multiply(a, b)
    print(f'El resultado multiplicado es {res}')

if __name__ == '__main__':
    main()
