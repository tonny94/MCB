from Abstract.AActionSubclasses.ActionLine import ActionLine


class CSelectError(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot.nameChatbotToSolve == '':
            self.chatbot.output.exec('No hay un chatbot seleccionado.')
        elif not (self.chatbot.nameChatbotToSolve == '') and self.chatbot.listUnresolvedErrors == {}:
            self.chatbot.output.exec('El chatbot "' + self.chatbot.nameChatbotToSolve + '" no tiene errores.')
        else:
            self.chatbot.showRandomResponse()
            sentence = self.chatbot.input.exec()
            if not (self.checkCancellation(sentence)):
                if not(sentence in self.chatbot.listUnresolvedErrors):
                    self.chatbot.output.exec('La sentencia a resolver no se encuentra entre la lista de errores.')
                else:
                    self.chatbot.senteceToSolve = sentence
                    self.chatbot.output.exec('Se ha seleccionado el error "'+ sentence+ '".')

    def checkCancellation(self, sentence):
        if (sentence.lower()  in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False
