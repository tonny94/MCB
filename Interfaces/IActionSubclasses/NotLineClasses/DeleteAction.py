from Interfaces.IActionSubclasses.ActionLine import ActionLine


class CDeleteAction(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self):
        if self.chatbot.currentStructureChatBot is None:
            print('ERROR: No hay ningun Chatbot actual para borrar un Action en un Intent.')
        elif self.chatbot.currentStructureChatBot.currentIntent is None :
            print('ERROR: No hay ningun Intent actual para asociarle un Action.')
        else:
            self.chatbot.currentStructureChatBot.currentIntent.setAction('')
