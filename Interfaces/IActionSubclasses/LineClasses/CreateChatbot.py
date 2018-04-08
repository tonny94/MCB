#Clases de acciones
from Interfaces.IActionSubclasses.ActionLine import ActionLine
from Interfaces.IActionSubclasses.LineClasses.CreateIntent import CCreateIntent

#Clases generales
from MetaChatBot.ChatBot import ChatBot


class CCreateChatbot(ActionLine):

    def __init__(self,currentChatBotB,diccCB):
        self.currentCB = currentChatBotB
        self.diccChatbots = diccCB

    def exec(self,):
        sentence = input('=>')
        # self.addChatBot(sentence)
        if not sentence in self.diccChatbots:
            myChatBot = ChatBot.ChatBot()
            myChatBot.setName(sentence)

            # crea la intencion de salir para cada chatbot que se cree
            CCreateIntent(myChatBot).createExitIntent(myChatBot)

            self.diccChatbots[sentence] = myChatBot
            self.currentCB[1] = myChatBot
            print('El ChatBot "' + sentence + '" se ha añadido correctamente.')
        else:
            print('El ChatBot "' + sentence + '" ya existe.')

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
