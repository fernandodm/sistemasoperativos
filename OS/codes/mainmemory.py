from firstsetting import FirstSetting
from lastsetting import LastSetting
from badwaysetting import BadWaySetting

class MainMemory():
    def __init__(self):
        self.cells = {}
        self.setting = FirstSetting()

    def getCells(self):
        return self.cells

    def getSetting(self):
        return self.setting

    def putDateInCell(self,date,cell):
        #si la celda existe la suscribe
        self.cells[cell] = date

    def setLastSetting(self):
        self.setting = LastSetting()

    def setBadWaySetting(self):
        self.setting = BadWaySetting()

    def nextDateFrom(self, adress):
        #empiezo por la direccion que me pasan
        it = adress
        #mientras este adentro de la memoria
        while(it < len(self.getCells().keys())):
            #asi la informacion de la direccion
            #actual no esta vacia entonces..
            if(self.getCells()[it] != None):
                #retorno la direccion y el dato como proximo espacio con informacion valida
                return (it, self.getCells()[it])
            #si esta vacia sigo recorriendo hasta encontrar alguna celda con informacion
            it +=1
        #si no encontre ninguna celda proxima con informacion no retorno nada
        return None

    def compress(self,adress,rest):
        #agarro la clave del proximo elemento que no sea vacio y su informacion
        (keyNext,date) = self.nextDateFrom(adress+1)
        #si la informacion no es vacia
        if(date != None):
            #las celdas intercambian su informacion (swap)
            self.getCells()[keyNext] = None
            self.getCells()[adress] = date
            return True
        #su la informacion es vacia significa que no hay mas que comprimir
        else:
            return False


    def compact(self):
        #direccion hasta donde se encuentra comprimida
        adressComp = 0
        #las celdas que estan vacias inmediatamente despues del adressComp
        rest = 0
        #las claves de las celdas
        keys = self.getCells().keys()
        #empieza con la primer clave
        currKey = keys[0]
        #mientras este adentro de la memoria
        while(currKey<len(keys)):
            #si la celda de clave actual esta vacia..
            if(self.getCells()[currKey] == None):
            #sumo celda vacia
                rest +=1
            #si no esta vacia pero ya habia contado vacias entonces
            elif(rest != 0):
                if(self.compress(adressComp,rest)):
                    adressComp += 1
                    currKey = adressComp
                #si al comprimir devuelve false se debe terminar porque ya se hizo
                #la mayor compresion posible
                else:
                    break;
            #si no esta vacia ni se habia contado vacias sumo uno
            #a las direcciones comprimidas
            else:
                adressComp +=1
            currKey +=1



    def deleteDatesForPcb(self,pcb):
        
        for currCell in range(pcb.getBasePointer(),(pcb.getBasePointer()+pcb.getSize())):
            self.cells[currCell] = None
            

    def getFreeCellWithSize(self,size):
        #si no encuentro una celda libre entonces..
        if(self.getSetting().getFreeCellWithSize(self.cells,size)== None)
            #compacto la informacion
            self.compact()
        #retorno un valor que tiene mas chances a ser distinto de None
        #porque se compacto previamente en el caso que no entre de primera
        return self.getSetting().getFreeCellWithSize(self.cells,size)
