from Interfaces.IActionSubclasses.ActionLine import ActionLine


class CCreateResponse(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot == {}:
            print('ERROR: No hay un Chatbot actual para crear un Response en un Intent.')
        elif self.chatbot[1].currentIntent is None :
            print('ERROR: No hay un Intent actual para asociarle un Response.')
        else:
            sentence = input('=>')
            if not sentence in self.chatbot[1].currentIntent.responses:
                self.chatbot[1].currentIntent.addResponse(sentence)
            else:
                print('El Response "' + sentence + '" ya existe.')




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








