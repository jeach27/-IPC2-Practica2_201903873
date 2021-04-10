import os

class Nodo:
    def __init__(self,nombre,apellido,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.head = None
    
    def insertar(self,nombre,apellido,telefono):
        nuevo = Nodo(nombre, apellido, telefono)
        if self.head == None:
            self.head = nuevo
            return
        aux = self.head
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = nuevo
        nuevo.anterior = aux

    def buscar(self, telefono):
        aux = self.head
        while aux:
            if aux.telefono == telefono:
                return aux
            aux = aux.siguiente
        return -1
    
    def imprimir(self):
        aux = self.head
        while aux:
            print(aux.nombre+'  '+aux.telefono)
            aux = aux.siguiente

    def graficar(self):
        file = open('Agenda.dot','w')
        file.write('digraph G{\n')
        aux = self.head
        while aux:
            file.write(str(aux)+'[label="{ Nombre: '+aux.nombre+' | Apellido: '+aux.apellido+' | Telefono: '+aux.telefono+' }",shape=Mrecord]\n')
            aux = aux.siguiente

        aux = self.head
        while aux:
            if aux.siguiente != None:
                file.write(str(aux)+'->'+str(aux.siguiente)+'\n')
                file.write(str(aux.siguiente)+'->'+str(aux)+'\n')
            aux = aux.siguiente
        
        
        file.write('}')
        file.close()
        os.system('dot -Tpng Agenda.dot -o Agenda.png')
        os.startfile('Agenda.png')
   
