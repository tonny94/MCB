#Clases de acciones
from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CDeleteChatbot(ActionLine):

    def __init__(self,currentCB,diccCB):
        self.currentCB = currentCB
        self.diccChatbots = diccCB

    def exec(self,):
        sentence = input('=>')
        if sentence in self.diccChatbots:
            # myChatBot = self.dicChatBots[nameChatBot]
            del self.diccChatbots[sentence]

            if sentence is self.currentCB[1].name:
                self.currentCB = {}
            print('El ChatBot "' + sentence + '" se ha eliminado correctamente .')
        else:
            print('El ChatBot "' + sentence + '" no existe .')

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
