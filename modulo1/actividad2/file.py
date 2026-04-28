import math

def calculate_discount(total_amount):
    if(total_amount <= 5000):
        return print(f'Lo sentimos no hay descuento, monto a pagar {total_amount}')
    elif(total_amount > 5000 and total_amount <= 10000):
        discount = math.trunc(total_amount * 0.1)
        return print(f'Se aplicará un descuento de {discount}(10%), el total a pagar es {total_amount - discount}')
    else:
        discount = math.trunc(total_amount * 0.2)
        return print(f'Se aplicará un descuento de {discount}(20%), el total a pagar es {total_amount - discount}')

print('Ingrese monto total de su compra para calcular el descuento\n')
total_amount = float(input('Monto total: '))
calculate_discount(total_amount)