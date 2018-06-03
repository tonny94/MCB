#Clases de acciones
from Abstract.AActionSubclasses.ActionLine import ActionLine

#Clases generales


class CDeletePattern(ActionLine):

    def __init__(self, chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No hay ningun chatbot actual para eliminar algun Pattern de uno de sus Intents.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None:
            self.chatbot.output.exec('ERROR: No hay ningun Intent para eliminar algun Pattern')
        else:
            self.chatbot.showRandomResponse()
            sentence = self.chatbot.input.exec()
            if not(self.checkCancellation(sentence)):
                self.chatbot.currentStructureChatBot.currentIntent.deletePattern(sentence)

    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False