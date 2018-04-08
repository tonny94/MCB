#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine
#Clases generales
from Interfaces.IActionSubclasses.NotLineClasses.ToList import CToList

class CListIntents(ActionNotLine):

    def __init__(self,chatbot,message):
        self.chatbot = chatbot
        self.mesaage = message

    def exec(self,):
        if self.chatbot == {}:
            print('No hay ningun ChatBot actual para listar sus Intents.')
        else:
            toList = CToList(self.chatbot.dicIntents,self.mesaage,'Intent')
            toList.exec()





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
