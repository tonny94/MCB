from Abstract.AActionSubclasses.ActionLine import ActionLine


class CCreateResponse(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No hay un Chatbot actual para crear un Response en una Intención.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None :
            self.chatbot.output.exec('ERROR: No hay una Intención actual para asociarle una Respuesta.')
        else:
            self.chatbot.showRandomResponse()
            sentence = self.chatbot.input.exec()
            if not(self.checkCancellation(sentence)):
                if not self.chatbot.isEmpty(sentence):
                    state = self.chatbot.currentStructureChatBot.currentIntent.addResponse(sentence)
                    if state:
                        self.chatbot.output.exec('Se ha añadido la Respuesta "'+sentence+'" correctamente.')
                else:
                    self.chatbot.output.exec('No se admiten valores vacíos.')

    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operación.')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False