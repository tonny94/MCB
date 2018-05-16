#Clases de acciones

from Abstract.AActionSubclasses.ActionLine import ActionLine

#Clases generales


class CFinishRunningCB(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        self.chatbot.runChatBot = False
        self.chatbot.output.exec('Se ha parado de ejecutar el Chatbot "'+self.chatbot.name+'".')
