from Interfaces.IActionSubclasses.ActionLine import ActionLine


class CSelectError(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        sentence = input('=>')
        if not (self.checkCancellation(sentence)):

            if not(sentence in self.chatbot.listUnresolvedErrors):
                print('La sentencia a resolver no se encuentra entre la lista de errores.')
            else:
                self.chatbot.senteceToSolve = sentence
                print('Se ha seleccionado la sentencia "', sentence, '".')

    def checkCancellation(self, sentence):
        if (sentence.lower()  in self.listKeysWordsCancelRunning):
            print('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False
