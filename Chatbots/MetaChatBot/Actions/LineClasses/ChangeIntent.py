#Clases de acciones

from Abstract.AActionSubclasses.ActionLine import ActionLine

#Clases generales


class CChangeIntent(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No se puede cambiar de Intención porque no hay un Chatbot actual.')
        else:
            self.chatbot.showRandomResponse()
            sentence = self.chatbot.input.exec()
            if not(self.checkCancellation(sentence)):
                if not self.chatbot.isEmpty(sentence):
                    self.chatbot.currentStructureChatBot.setCurrentIntent(sentence)
                else:
                    self.chatbot.output.exec('No se admiten valores vacíos.')

    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operación.')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False