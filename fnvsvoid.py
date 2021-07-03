def celsius_to_fah(celsius):
    return ( celsius *9/5) + 32


def temperature_table(): #void function in C, JAVA
    for c in range(0, 101, 5):
        f = celsius_to_fah(c)
        print("{}c = {}F" .format(c,f) )
        
#f = celsius_to_fah(100)
#print(f)
#temperature_table()

def menu():
    print('1.convert Celsius to Fahrenheit')
    print('2. display temperature table')
    n = input('Enter choice')
    if n == 1 :
        celsius = float(input("Enter degree in celsius"))
        print("{}c = {}F" .format(celsius,celsius_to_fah(celsius)) )
    elif n == 2 :
        temperature_table()

menu()