#Clases de acciones
from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CDeleteIntent(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot.currentStructureChatBot is None:
            print('ERROR: No hay ningun chatbot actual para eliminar algun CStructureIntent de su lista.')
        else:
            sentence = input('=>')
            if not(self.checkCancellation(sentence)):
                self.chatbot.currentStructureChatBot.deleteIntent(sentence)


    def checkCancellation(self,sentence):
        if (sentence.lower()  in self.listKeysWordsCancelRunning):
            print('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False