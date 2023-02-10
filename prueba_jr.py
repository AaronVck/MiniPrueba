import random
class Cuenta_Bancaria:
    def __init__(self):
        self.Nombre_titular = None
        self.Numero_cuenta = None
        self.Saldo = 0

    def crear(self):
        if self.Nombre_titular is None:
            self.Nombre_titular = input('Empecemos por su nombre ¿Cómo se llama?: ')
            print('De acuerdo {}, Continuemos'.format(self.Nombre_titular))
            self.Numero_cuenta = random.randint(100,1000)
            print('Su numero de cuenta es {}, por favor guardelo para mas adelante'.format(self.Numero_cuenta))
            print('Bienvenido/a {}, Ahora podrá acceder a las acciones de nuestro banco'.format(self.Nombre_titular))
        else:
            print('{}, Usted ya creó una cuenta'.format(self.Nombre_titular))
    def deposito(self):
        try:
            numero = int(input('Necesitamos su numero de cuenta para permitirle un deposito: '))
        except ValueError:
            print('Favor de ingresar una opcion valida')
            numero = 0
            print('------------------------------------------------')


        if self.Numero_cuenta == numero:
            Deposito_Retiro = int(input('¿Cuánto desea depositar?'))
            self.Saldo = Deposito_Retiro + self.Saldo
            print('Ha DEPOSITADO {}, Usted actualmente tiene {} de saldo'.format(Deposito_Retiro,self.Saldo))
        else:
            print('Numero de cuenta equivocado o aun no posee una cuenta')

    def retirar(self):
        try:
            numero = int(input('Necesitamos su numero de cuenta para permitirle un retiro: '))
        except ValueError:
            print('Favor de ingresar una opcion valida')
            numero = 0
            print('------------------------------------------------')
        if self.Numero_cuenta == numero:
            Deposito_Retiro = int(input('¿Cuánto desea depositar?'))
            self.Saldo = self.Saldo - Deposito_Retiro
            print('Ha RETIRADO {}, Usted actualmente tiene {} de saldo'.format(Deposito_Retiro,self.Saldo))
        else:
            print('Numero de cuenta equivocado o aun no posee una cuenta')


class Cuenta_Ahorros(Cuenta_Bancaria):
    def __init__(self):
        super().__init__()
        self.Tasa_interes = 14

    def interes_ganado(self):
        try:
            numero = int(input('Necesitamos su numero de cuenta para permitirle ver sus intereses ganados: '))
        except ValueError:
            print('Favor de ingresar una opcion valida')
            numero = 0
            print('------------------------------------------------')
        if self.Numero_cuenta == numero:
            Saldo_pasado = self.Saldo
            self.Saldo = (self.Saldo / 100 * self.Tasa_interes) + self.Saldo
            print("El interés del banco es del {}% usted tenía en su saldo {} y ahora tiene {}".format(self.Tasa_interes,
                                                                                                    Saldo_pasado,
                                                                                                    self.Saldo))
        else:
            print('Numero de cuenta equivocado o aun no posee una cuenta')
class Cuenta_Corriente(Cuenta_Ahorros):
    def __init__(self):
        super().__init__()
        self.Limite_credito = 500000
    def comprar(self):
        try:
            numero = int(input('Necesitamos su numero de cuenta para permitirle una compra con credito: '))
        except ValueError:
            print('Favor de ingresar una opcion valida')
            numero = 0
            print('------------------------------------------------')
        if self.Numero_cuenta == numero:
            compra = int(input('¿De cuanto es lo que desea comprar?'))
            if self.Saldo + self.Limite_credito < compra:
                print('Usted excede el limite de credito para comprar su producto/servicio')
            else:
                print('De acuerdo, compra realizada con éxito')
        else:
            print('Numero de cuenta equivocado o aun no posee una cuenta')

cuenta = Cuenta_Corriente()
menu = """¿Qué acción desea Realizar?
0)Crear Cuenta
1)Depositar
2)Retirar
3)Verificar el interés ganado
4)Comprar
5)Salir"""
while True:
    print(menu)
    try:
        opcion = int(input(":"))
    except ValueError:
        print('Favor de ingresar una opcion valida')
        opcion = 7
    if opcion == 1:
        cuenta.deposito()
    elif opcion == 2:
        cuenta.retirar()
    elif opcion == 3:
        cuenta.interes_ganado()
    elif opcion == 5:
        print('Adios')
        break
    elif opcion == 4:
        cuenta.comprar()
    elif opcion == 0:
        cuenta.crear()
    else:
        print('Ingrese una opción válida')




