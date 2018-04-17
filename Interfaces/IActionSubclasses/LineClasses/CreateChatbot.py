#Clases de acciones
from Interfaces.IActionSubclasses.ActionLine import ActionLine
from Interfaces.IActionSubclasses.LineClasses.CreateIntent import CCreateIntent

#Clases generales
from StructureChatBot.StructureChatBot import CStructureChatBot


class CCreateChatbot(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        sentence = input('=>')
        if not (self.checkCancellation(sentence)):
            self.chatbot.addStructureChatbotDict(sentence)


    def checkCancellation(self,sentence):
        if any(sentence.lower() == word.lower() for word in self.listKeysWordsCancelRunning):
            print('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            self.chatbot.unrecognizeIntent = self.chatbot.currentIntent
            return True
        else:
            return False