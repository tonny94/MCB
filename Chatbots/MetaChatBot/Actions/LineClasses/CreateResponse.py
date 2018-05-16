from Abstract.AActionSubclasses.ActionLine import ActionLine


class CCreateResponse(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No hay un Chatbot actual para crear un Response en un Intent.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None :
            self.chatbot.output.exec('ERROR: No hay un Intent actual para asociarle un Response.')
        else:
            sentence = self.chatbot.input.exec()
            if not(self.checkCancellation(sentence)):
                state = self.chatbot.currentStructureChatBot.currentIntent.addResponse(sentence)
                if state:
                    self.chatbot.output.exec('Se ha añadido el Response "'+sentence+'" correctamente.')

    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False