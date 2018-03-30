#Clases de acciones
from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CDeleteResponse(ActionLine):

    def __init__(self, chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot is None:
            print('No hay ningun chatbot actual para eliminar algun Response de uno de sus Intents.')
        elif self.chatbot.currentIntent is None:
            print('No hay ningun Intent para eliminar algun Response')
        else:
            sentence = input('=>')
            if sentence in self.chatbot.currentIntent.responses:
                del self.chatbot.currentIntent.responses[sentence]
                print('El Response "' + sentence + '" se ha eliminado correctamente .')
            else:
                print('El Response "' + sentence + '" no existe .')





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
