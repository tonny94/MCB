from Abstract.AActionSubclasses.ActionLine import ActionLine


class CCreateAction(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No hay ningún Chatbot actual para crear una Acción en una Intención.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None :
            self.chatbot.output.exec('ERROR: No hay Intención actual para asociarle una Acción.')
        else:
            self.chatbot.showRandomResponse()
            sentence = self.chatbot.input.exec()
            if not(self.checkCancellation(sentence)):
                if not self.chatbot.isEmpty(sentence):
                    self.chatbot.currentStructureChatBot.currentIntent.setAction(sentence)
                    self.chatbot.output.exec('Se ha guardado la acción "'+sentence+'".')
                else:
                    self.chatbot.output.exec('No se admiten valores vacíos.')

    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operación.')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False