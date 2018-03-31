#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales
from ChatBot import ChatBot
from Intent import  Intent


class CSaveSentenceAfirmative(ActionLine):

    def __init__(self,chatbotName,sentence,dict):
        self.chatbotName = chatbotName
        self.sentence = sentence
        self.dictionary = dict

    def exec(self,):
        if self.dictionary == {}:
            self.dictionary = {self.chatbotName: [[],[]]} # por cada chatbot se tiene: [listaNoReconocidos,listaYaReconocidos]
        elif not self.chatbotName in self.dictionary:
            self.dictionary[self.chatbotName] = [[],[]]
            self.addNoReconocido(self.chatbotName)

    def addNoReconocido(self, nombChatbot):
        self.dictionary[nombChatbot][0].append(self.sentence)
        print('Se ha anhadido la sentencia a la lista de error.')

    # def addYaReconocido(self, nombChatbot):
    #     self.dictionary[nombChatbot][0].remove(self.sentence)
    #     self.dictionary[nombChatbot][1].append(self.sentence)
    #     print('Se ha corregido la sentencia a la lista de error.')




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
