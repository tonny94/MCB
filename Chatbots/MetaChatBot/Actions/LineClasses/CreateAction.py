from Abstract.AActionSubclasses.ActionLine import ActionLine


class CCreateAction(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No hay ningun Chatbot actual para crear un Action en un Intent.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None :
            self.chatbot.output.exec('ERROR: No hay ningun Intent actual para asociarle un Action.')
        else:
            self.chatbot.showRandomResponse()
            sentence = self.chatbot.input.exec()
            if not(self.checkCancellation(sentence)):
                self.chatbot.currentStructureChatBot.currentIntent.setAction(sentence)
                self.chatbot.output.exec('Se ha guardado la accion "'+sentence+'".')
    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False