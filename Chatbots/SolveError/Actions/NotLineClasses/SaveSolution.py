from Abstract.AActionSubclasses.ActionLine import ActionLine

class CSaveSolution(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot.senteceToSolve is None and self.chatbot.intentToSolve is None:
            self.chatbot.output.exec('No hay una sentencia ni un Intent seleccionados.')
        elif self.chatbot.senteceToSolve is None:
            self.chatbot.output.exec('No hay una sentencia de error seleccionada.')
        elif self.chatbot.intentToSolve is None:
            self.chatbot.output.exec('No hay una intención a la que vincular la sentencia.')

        else:
            self.chatbot.solveSentence()
