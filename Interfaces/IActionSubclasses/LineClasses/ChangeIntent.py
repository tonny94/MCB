#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CChangeIntent(ActionLine):

    def __init__(self,currentChatbot):
        self.currentChatbot = currentChatbot

    def exec(self,):
        if self.currentChatbot == {}:
            print('ERROR: No se puede cambiar de Intent porque no hay un Chatbot actual.')
        else:
            sentence = input('=>')
            intentList = self.currentChatbot[1].dicIntents
            if not sentence in intentList:
                print('No existe ese Intent.')
            else:
                self.currentChatbot[1].currentIntent = self.currentChatbot[1].dicIntents[sentence]
                if not self.currentChatbot[1].currentIntent == None:
                    nameIntent = self.currentChatbot[1].currentIntent.tag
                    print('Se ha cambiado "', nameIntent, '" por "', sentence, '".')
                else:
                    print('Ahora "', sentence, '" es el actual Intent.')



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
