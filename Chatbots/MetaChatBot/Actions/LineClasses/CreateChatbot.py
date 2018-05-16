#Clases de acciones
from Abstract.AActionSubclasses.ActionLine import ActionLine



class CCreateChatbot(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        sentence = self.chatbot.input.exec()
        if not (self.checkCancellation(sentence)):
            self.chatbot.addStructureChatbotDict(sentence)


    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            self.chatbot.unrecognizeIntent = self.chatbot.currentIntent
            return True
        else:
            return False