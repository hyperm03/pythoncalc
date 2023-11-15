# calcolatrice.py

def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b != 0:
        return a / b
    else:
        return "Impossibile dividere per zero"

def calcolatrice():
    print("Seleziona un'operazione:")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")

    scelta = input("Inserisci il numero corrispondente all'operazione desiderata: ")

    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))

    if scelta == '1':
        print(num1, "+", num2, "=", somma(num1, num2))
    elif scelta == '2':
        print(num1, "-", num2, "=", sottrazione(num1, num2))
    elif scelta == '3':
        print(num1, "*", num2, "=", moltiplicazione(num1, num2))
    elif scelta == '4':
        print(num1, "/", num2, "=", divisione(num1, num2))
    else:
        print("Operazione non valida")

if __name__ == "__main__":
    calcolatrice()
