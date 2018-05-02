#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CFinishRunningCB(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        self.chatbot.runChatBot = False
        print('Se ha parado de ejecutar el Chatbot "',self.chatbot.name,'".')
