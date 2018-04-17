#Clases de acciones
from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CDeleteChatbot(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        sentence = input('=>')
        if not (self.checkCancellation(sentence)):
            self.chatbot.deleteStructureChatbotDict(sentence)

    def checkCancellation(self,sentence):
        if (sentence.lower() == word.lower() for word in self.listKeysWordsCancelRunning):
            print('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False
