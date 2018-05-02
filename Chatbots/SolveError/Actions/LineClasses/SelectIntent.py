from Interfaces.IActionSubclasses.ActionLine import ActionLine


class CSelectIntent(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        sentence = input('=>')
        if not (self.checkCancellation(sentence)):

            if not(sentence in self.chatbot.listIntens):
                print('El Intent no existe en la lista.')
            else:
                self.chatbot.intentToSolve = sentence
                print('Se ha seleccionado el Intent "',sentence,'".')

    def checkCancellation(self, sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            print('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False
