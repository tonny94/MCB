from Abstract.AActionSubclasses.ActionLine import ActionLine


class CDeleteAction(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot.currentStructureChatBot is None:
            self.chatbot.output.exec('ERROR: No hay ningun Chatbot actual para borrar un Action en un Intent.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None :
            self.chatbot.output.exec('ERROR: No hay ningun Intent actual para asociarle un Action.')
        else:
            self.chatbot.currentStructureChatBot.currentIntent.setAction('')
