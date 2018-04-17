from Interfaces.IActionSubclasses.ActionLine import ActionLine


class CCreateAction(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot.currentStructureChatBot is None:
            print('ERROR: No hay ningun Chatbot actual para crear un Action en un Intent.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None :
            print('ERROR: No hay ningun Intent actual para asociarle un Action.')
        else:
            sentence = input('=>')
            if not(self.checkCancellation(sentence)):
                state = self.chatbot.currentStructureChatBot.currentIntent.setAction(sentence)

    def checkCancellation(self,sentence):
        if (sentence.lower() == word.lower() for word in self.listKeysWordsCancelRunning):
            print('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False