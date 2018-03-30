#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine

#Clases generales
from ChatBot import ChatBot
from Intent import Intent

class CShowObject(ActionNotLine):

    def __init__(self,object):
        self.currentObject = object
        self.name = ''
        self.objectType = ''
        if isinstance(self.currentObject, ChatBot):
            self.name = self.currentObject.name
            self.objectType = 'Chatbot'
        elif isinstance(self.currentObject, Intent):
            self.name = self.currentObject.tag
            self.objectType = 'Intent'

    def exec(self,):
        if self.currentObject is None:
            print('No se ha creado ningun ',self.objectType,'.')
        else:
            print('"',self.name,'"')








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
