#Clases de acciones
from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine
#Clases generales

class CListChatBots(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        self.chatbot.printStructureChatbotDict()

