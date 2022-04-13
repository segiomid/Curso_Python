def divisors(num):
    assert num > 0, "El número debe ser positivo"
    divisors = [i for i in range (1, num + 1) if num % i == 0]
    return divisors
    

def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print('---- Terminó programa -----')

if __name__=='__main__':
    run()