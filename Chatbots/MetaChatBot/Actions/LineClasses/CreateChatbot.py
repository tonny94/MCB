#Clases de acciones
from Abstract.AActionSubclasses.ActionLine import ActionLine



class CCreateChatbot(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        self.chatbot.showRandomResponse()
        sentence = self.chatbot.input.exec()
        if not (self.checkCancellation(sentence)):
            if not self.chatbot.isEmpty(sentence):
                self.chatbot.addStructureChatbotDict(sentence)
            else:
                self.chatbot.output.exec('No se admiten valores vacíos.')


    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operación.')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            self.chatbot.unrecognizeIntent = self.chatbot.currentIntent
            return True
        else:
            return False