#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine
#Clases generales
import ChatBot
import Intent

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
            if self.objectType is 'Intent':
                result = ", ".join(str(value.tag) for key, value in self.iterableObject.items())
            elif self.objectType is 'ChatBot':
                result = ", ".join(str(value.name) for key, value in self.iterableObject.items())
            print(self.mesaage,' [',result,']')






    # def setChatbot(self,chatbot,dicc):
    #     self.chatbot = chatbot
    #     self.diccChatbots = dicc
    #     self.exec()
    #
    # def getChatbot(self,chatbot):
    #     self.chatbot = chatbot

#         self.actions = {'saludar': self.saludar, 'despedir': self.despedir, 'saludar1': self.saludar1}
#
#         def exectAction(self, functionName, *args):
#             self.actions[functionName](*args)
#
#         def saludar(self, a, b):
#             print('probando ' + str(a) + ' con ' + str(b))
#
#         def despedir(self):
#             print('adios')
#
#         def saludar1(self, a):
#             print('solo 1' + str(a))
# objAction = Action()
#
# objAction.exectAction('saludar','primero',9)
# objAction.exectAction('despedir')
# objAction.exectAction('saludar1',4)
