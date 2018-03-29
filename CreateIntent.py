from ActionLine import ActionLine

from Intent import Intent


class CCreateIntent(ActionLine):

    def __init__(self,chatbot,sentence):
        self.chatbot = chatbot
        self.sentence = sentence

    def exec(self):
        # self.addChatBot(sentence)
        if not self.sentence in self.chatbot.dicIntents:
            myIntent = Intent()
            myIntent.setTag(self.sentence)
            self.chatbot.dicIntents[self.sentence] = myIntent
            self.chatbot.currentIntent = myIntent
            print('El Intent ' + self.sentence + ' se ha añadido correctamente.')
        else:
            print('El Intent ' + self.sentence + ' ya existe.')

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








