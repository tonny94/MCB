#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales
from ChatBot import ChatBot
from Intent import  Intent


class CSaveSentence(ActionLine):

    def __init__(self,chatbotName,sentence,dict):
        self.chatbotName = chatbotName
        self.sentence = sentence
        self.dictionary = dict

    def exec(self,):
        # if self.dictionary is {}:
        #     self.dictionary = {self.chatbotName: [[],[]]} # por cada chatbot se tiene: [listaNoReconocidos,listaYaReconocidos]
        # el
        if self.sentence == '':
            print('No hay sentencia que guardar.')
        else:
            if not self.chatbotName in self.dictionary:
               self.dictionary[self.chatbotName] = [[],[]]
            self.addNoReconocido(self.chatbotName)

    def addNoReconocido(self, nombChatbot):
        self.dictionary[nombChatbot][0].append(self.sentence)
        print('Se ha anhadido la sentencia a la lista de error.')
