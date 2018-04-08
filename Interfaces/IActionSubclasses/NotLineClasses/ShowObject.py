#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine

#Clases generales

class CShowObject(ActionNotLine):

    def __init__(self,object,type = None):
        self.currentChatbot = object
        self.objectType = type

    def exec(self,):
        if self.objectType == 'Intent':
            if self.currentChatbot == {}:
                print('ERROR: No se hay ningun ChatBot actual por lo que no se puede mostrar ningun Intent.')
            else:
                chatbot = self.currentChatbot[1]
                if chatbot.currentIntent == None:
                    print('No hay ningun ', self.objectType, ' actual.')
                else:
                    print('"', chatbot.currentIntent.tag, '"')
        else:
            if self.currentChatbot == {}:
                print('No hay ningun ChatBot actual.')
            else:
                print('"', self.currentChatbot[1].name, '"')












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
