#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CChangeChatbot(ActionLine):

    def __init__(self,currentChatbot,dictChatbot):
        self.currentChatbot = currentChatbot
        self.dictChatbot = dictChatbot

    def exec(self,):
        sentence = input('=>')
        if not sentence in self.dictChatbot:
            print('No existe ese Chatbot.')
        else:
            if not self.currentChatbot == {}:
                nameCB = self.currentChatbot[1].name
                self.currentChatbot[1] = self.dictChatbot[sentence]
                print('Se ha cambiado "', nameCB, '" por "', sentence, '".')
            else:
                self.currentChatbot[1] = self.dictChatbot[sentence]
                print('Ahora "', sentence, '" es el actual Chatbot.')



        # if self.type == 'Intent':
        #     intent = self.currentChatbot[1].currentIntent
        #     if intent == None or not sentence in self.currentChatbot[1].dicIntents:
        #         print('No existe la Intencion.')
        #     else:
        #         self.currentChatbot[1].currentIntent = self.currentChatbot[1].dicIntents[sentence]
        #         print('Se ha cambiado "', intent.tag, '" por "', sentence, '".')
        # else:





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
