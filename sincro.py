import concurrent.futures

def funcion1():
    # Código de la función 1
    print("Función 1 ejecutándose...")
    return "Resultado de función 1"

def funcion2():
    # Código de la función 2
    print("Función 2 ejecutándose...")
    return "Resultado de función 2"

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futuro1 = executor.submit(funcion1)
        futuro2 = executor.submit(funcion2)
    
    resultado1 = futuro1.result()
    resultado2 = futuro2.result()
    
    print(resultado1)
    print(resultado2)