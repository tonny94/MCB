from Abstract.AActionSubclasses.ActionLine import ActionLine


class CSelectIntent(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        sentence = self.chatbot.input.exec()
        if not (self.checkCancellation(sentence)):

            if not(sentence in self.chatbot.listIntens):
                self.chatbot.output.exec('El Intent no existe en la lista.')
            else:
                self.chatbot.intentToSolve = sentence
                self.chatbot.output.exec('Se ha seleccionado el Intent "'+sentence+'".')

    def checkCancellation(self, sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False
