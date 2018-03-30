from Interfaces.IActionSubclasses.ActionLine import ActionLine

from Intent import Intent


class CCreateIntent(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot is None:
            print('No existe ningun chatbot para asociarle un Intent.')
        else:
            sentence = input('=>')
            if not sentence in self.chatbot.dicIntents:
                myIntent = Intent()
                myIntent.setTag(sentence)
                self.chatbot.dicIntents[sentence] = myIntent
                self.chatbot.currentIntent = myIntent
                print('El Intent "' + sentence + '" se ha añadido correctamente.')
            else:
                print('El Intent "' + sentence + '" ya existe.')

    def createExitIntent(self,chatbot):
        # crea la intencion
        intent = Intent()
        intent.setTag('salirChatbot')
        intent.setAction('salirChatbot')
        intent.addPattern('Salir del chatbot')
        intent.addPattern('Finalizar chatbot')
        intent.addPattern('Salir del chatbot')
        intent.addPattern('Dejar de ejecutar chatbot')
        intent.responses = []

        chatbot.dicIntents['salirChatbot'] = intent

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








