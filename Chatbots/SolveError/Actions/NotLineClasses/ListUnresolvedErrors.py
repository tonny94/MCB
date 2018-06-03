from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine

class CListUnresolvedErrors(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self, ):
        if self.chatbot.nameChatbotToSolve == '':
            self.chatbot.output.exec('No hay un chatbot seleccionado.')
        elif not (self.chatbot.nameChatbotToSolve == '') and self.chatbot.listUnresolvedErrors == {}:
            self.chatbot.output.exec('El chatbot "'+self.chatbot.nameChatbotToSolve+'" no tiene errores.')
        else:
            self.chatbot.printListUnresolvedErrors()