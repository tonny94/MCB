#Clases de acciones
from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CDeleteIntent(ActionLine):

    def __init__(self,currentCB):
        self.currentCB = currentCB

    def exec(self,):
        if self.currentCB is None:
            print('No hay ningun chatbot actual para eliminar algun Intent de su lista.')
        else:
            sentence = input('=>')
            if sentence in self.currentCB.dicIntents:
                del self.currentCB.dicIntents[sentence]
                if sentence is self.currentCB.currentIntent:
                    self.currentCB.currentIntent = None
                print('El Intent "' + sentence + '" se ha eliminado correctamente .')
            else:
                print('El Intent "' + sentence + '" no existe .')

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
