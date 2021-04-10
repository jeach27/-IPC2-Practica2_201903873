import funciones
import sys

def menu():
    agenda = funciones.ListaDoble()
    while True:
        print('\n-----------Menu principal---------------')
        print('\n> Elija una opcion')
        print('\n1.Ingresar Contacto\n2.Buscar Contacto\n3.Visualizar Agenda\n4.Salir')
        n=input('\n> Ingrese valor\n')
        if n == '1':
            print('--------------------Ingresar Contacto-----------------------\n')
            nombre = input('Ingrese Nombre\n')
            apellido = input('Ingrese Apellido\n')
            telefono = input('Ingrese Telefono\n')
            validacion = agenda.buscar(telefono)
            if validacion == -1:
                agenda.insertar(nombre, apellido, telefono)
                print('El contacto se ha agregado con exito\n')
            else:
                print('El contacto ya existe\n')

        elif n == '2':
            print('---------------------Buscar Contacto----------------------\n')
            telefono = input('Ingrese telefono por buscar\n')
            validacion = agenda.buscar(telefono)
            if validacion == -1:
                print('El numero no existe, desea agregarlo\n')
                print('1.SI\n2.NO\n')
                opcion = input('Elija una opcion\n')
                if opcion == '1':
                    nombre = input('Ingrese Nombre\n')
                    apellido = input('Ingrese Apellido\n')
                    agenda.insertar(nombre, apellido, telefono)
            else:
                print('\nNombre: '+validacion.nombre)
                print('Apellido: '+validacion.apellido)
                print('Telefono: '+validacion.telefono+'\n')
        elif n == '3':
            print('------------------Visualizar Agenda-------------------------\n')
            agenda.graficar()
        elif n == '4':
            sys.exit()
        else:
            print ("No has pulsado una opción correcta")