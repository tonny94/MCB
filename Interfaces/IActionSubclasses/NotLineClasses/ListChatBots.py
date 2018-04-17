#Clases de acciones
from Interfaces.IActionSubclasses.ActionNotLine import ActionNotLine
#Clases generales
from Interfaces.IActionSubclasses.NotLineClasses.ToList import CToList

class CListChatBots(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        self.chatbot.printStructureChatbotDict()

