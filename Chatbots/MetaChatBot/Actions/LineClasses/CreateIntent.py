from Abstract.AActionSubclasses.ActionLine import ActionLine

from StructureChatBot.StructureIntent import CStructureIntent


class CCreateIntent(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No hay un chatbot actual para asociarle un Intent.')
        else:
            self.chatbot.showRandomResponse()
            sentence = self.chatbot.input.exec()
            if not(self.checkCancellation(sentence)):
                state = self.chatbot.currentStructureChatBot.addIntent(sentence)
                if state:
                    self.chatbot.output.exec('El Intent "' + sentence + '" se ha añadido correctamente.')

                # if not sentence in self.chatbot[1].dicIntents:
                #     myIntent = CStructureIntent()
                #     myIntent.setTag(sentence)
                #     self.chatbot[1].dicIntents[sentence] = myIntent
                #     self.chatbot[1].currentIntent = myIntent
                #     print('El CStructureIntent "' + sentence + '" se ha añadido correctamente.')
                # else:
                #     print('El CStructureIntent "' + sentence + '" ya existe.')

    def createExitIntent(self,chatbot):
        # crea la intencion
        intent = CStructureIntent()
        intent.setTag('finishRunningChatbot')
        intent.setAction('finishRunningChatbot')
        intent.addPattern('salir')
        intent.addPattern('salir del chatbot')
        intent.addPattern('parar chatbot')
        intent.addPattern('terminar de ejecutar chatbot')
        intent.addPattern('parar')
        intent.responses = []
        chatbot.dicIntents['finishRunningChatbot'] = intent

    def createSaveSentenceIntent(self,chatbot):
        # crea la intencion
        intent = CStructureIntent()
        intent.setTag('saveSentence')
        intent.setAction('saveSentence')
        intent.addListPatterns(["@Guardar",
                "@Salvar"])
        intent.responses = []
        chatbot.dicIntents['saveSentence'] = intent

    def createDontSaveSentenceIntent(self,chatbot):
        # crea la intencion
        intent = CStructureIntent()
        intent.setTag('dontSaveSentence')
        intent.setAction('dontSaveSentence')
        intent.addListPatterns(["@No guardar",
                "@No salvar"])
        intent.responses = []
        chatbot.dicIntents['dontSaveSentence'] = intent

    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False