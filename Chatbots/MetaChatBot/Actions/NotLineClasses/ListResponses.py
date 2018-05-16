#Clases de acciones
from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine

class CListResponses(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot is None:
            self.chatbot.output.exec('ERROR: No hay ningun ChatBot actual para listar los Responses de su Intent actual.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None:
            self.chatbot.output.exec('ERROR: No hay ningun Intent actual para listar sus Responses')
        else:
            self.chatbot.currentStructureChatBot.currentIntent.printResponses()
