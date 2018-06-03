#Clases de acciones

from Abstract.AActionSubclasses.ActionLine import ActionLine

#Clases generales


class CChangeChatbot(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        self.chatbot.showRandomResponse()
        sentence = self.chatbot.input.exec()
        if not (self.checkCancellation(sentence)):
            self.chatbot.changeStrunctureCurrentChatbot(sentence)

    def checkCancellation(self, sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False