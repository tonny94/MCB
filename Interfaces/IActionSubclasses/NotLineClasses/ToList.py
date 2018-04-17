#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine
#Clases generales

class CToList(ActionNotLine):

    def __init__(self,iterableObject,message,type=None):
        self.iterableObject = iterableObject
        self.mesaage = message
        self.objectType = type

    def exec(self,):
        #lista
        if isinstance(self.iterableObject,list):
            print(self.mesaage,self.iterableObject)
        #diccionario
        elif isinstance(self.iterableObject,dict):
            result = ''
            if self.objectType == 'Intent':
                result = ", ".join(str(value.tag) for key, value in self.iterableObject.items())
            elif self.objectType == 'ChatBot':
                result = ", ".join(str(value.name) for key, value in self.iterableObject.items())
            print(self.mesaage,' [',result,']')
