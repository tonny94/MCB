from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine

class CListIntents(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self, ):
        self.chatbot.printIntents()
