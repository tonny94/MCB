#Clases de acciones
from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CDeletePattern(ActionLine):

    def __init__(self, chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot == {}:
            print('ERROR: No hay ningun chatbot actual para eliminar algun Pattern de uno de sus Intents.')
        elif self.chatbot[1].currentIntent is None:
            print('ERROR: No hay ningun Intent para eliminar algun Pattern')
        else:
            sentence = input('=>')
            if sentence in self.chatbot[1].currentIntent.patterns:
                del self.chatbot[1].currentIntent.patterns[sentence]
                print('El Pattern "' + sentence + '" se ha eliminado correctamente .')
            else:
                print('El Pattern "' + sentence + '" no existe .')





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
