#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine

#Clases generales
from ChatBot import ChatBot
from Intent import Intent

class CShowObject(ActionNotLine):

    def __init__(self,object,type = None):
        self.currentObject = object
        self.objectType = type

    def exec(self,):
        if self.currentObject is None:
            print('No se ha creado ningun ',self.objectType,'.')
        else:
            if self.objectType == 'ChatBot':
                print('"',self.currentObject.name,'"')
            elif self.objectType == 'Intent':
                print('"',self.currentObject.tag,'"')








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
