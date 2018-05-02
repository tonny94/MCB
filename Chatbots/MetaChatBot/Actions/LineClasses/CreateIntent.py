from Interfaces.IActionSubclasses.ActionLine import ActionLine

from StructureChatBot.StructureIntent import CStructureIntent


class CCreateIntent(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot.currentStructureChatBot is None:
            print('ERROR: No hay un chatbot actual para asociarle un Intent.')
        else:
            sentence = input('=>')
            if not(self.checkCancellation(sentence)):
                state = self.chatbot.currentStructureChatBot.addIntent(sentence)
                if state:
                    print('El Intent "' + sentence + '" se ha añadido correctamente.')

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

    def checkCancellation(self,sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            print('Se ha cancelado la operacion')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False