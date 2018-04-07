#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales
from ChatBot import ChatBot
from Intent import  Intent


class CChangeObject(ActionLine):

    def __init__(self,currentObject,dict:dict,name):
        self.currentObject = currentObject
        self.dict = dict
        self.name = name

    def exec(self,):
        sentence = input('=>')
        if sentence in self.dict:
            self.currentObject = self.dict[sentence]
            print('Se ha cambiado "',self.name,'" por "', sentence, '".')
        else:
            print('El nombre "' + sentence + '" no existe .')








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
