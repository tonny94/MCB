#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine

#Clases generales

class CShowIntent(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot= chatbot

    def exec(self,):
        if self.chatbot.currentStructureChatBot is None:
            print('ERROR: No hay Chatbot actual para mostrar su Intent actual.')
        else:
            self.chatbot.currentStructureChatBot.printCurrentIntent()



        # if self.objectType == 'CStructureIntent':
        #     if self.currentChatbot == None:
        #         print('ERROR: No se hay ningun CStructureChatBot actual por lo que no se puede mostrar ningun CStructureIntent.')
        #     else:
        #         chatbot = self.currentChatbot
        #         if chatbot.currentIntent == None:
        #             print('No hay ningun ', self.objectType, ' actual.')
        #         else:
        #             print('"', chatbot.currentIntent.tag, '"')








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
