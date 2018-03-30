from Interfaces.IActionSubclasses.ActionLine import ActionLine

from Intent import Intent


class CCreatePattern(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot is None:
            print('No existe ningun Chatbot crear un Pattern en un Intent.')
        elif self.chatbot.currentIntent is None :
            print('No existe ningun Intent para asociarle un Pattern.')
        else:
            sentence = input('=>')
            if not sentence in self.chatbot.currentIntent.patterns:
                self.chatbot.currentIntent.addPattern(sentence)
                print('El Pattern "' + sentence + '" se ha añadido correctamente.')
            else:
                print('El Pattern "' + sentence + '" ya existe.')




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








