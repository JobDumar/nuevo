
def ejercicio(input):
    """Uso del fizzbuzz

    Args:
        input (_type_): se inresa un numero entero

    Returns:
        _type_: _description_
    """
    if input % 3 == 0 and input % 5 == 0:
        return "fizzbuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input    
print(ejercicio(15))

    

def numero_mayor(a: int, b: int):
    """numero mayor

    Args:
        a (int): primer numero
        b (int): segundo numero

    Returns:
        _type_: muestra el numero mayor
    """
    if a > b:
        return a
    return b

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
print("El número mayor es:", numero_mayor(numero1, numero2))