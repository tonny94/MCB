from Abstract.AActionSubclasses.ActionLine import ActionLine


class CCreatePattern(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No hay ningun Chatbot actual para crear un Pattern en un Intent.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None :
            self.chatbot.output.exec('ERROR: No hay ningun Intent actual para asociarle un Pattern.')
        else:
            sentence = self.chatbot.input.exec()
            if not(self.checkCancellation(sentence)):
                state = self.chatbot.currentStructureChatBot.currentIntent.addPattern(sentence)
                if state:
                    self.chatbot.output.exec('Se ha añadido el Pattern "',sentence,'" correctamente.')

    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False