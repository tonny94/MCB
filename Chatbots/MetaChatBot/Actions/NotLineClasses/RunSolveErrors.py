from Abstract.AActionSubclasses.ActionLine import ActionLine
from Chatbots.SolveError.SolveError import CSolveError
from ChatBotProcessor import CBProcessor


class CRunSolveErrors(ActionLine):

    def __init__(self,chatbot):
        """
        Constructor de la Clase.
        :param chatbot: Es el ChatBot que tiene como acción la instancia de esta clase.
        """
        self.chatbot = chatbot

    def exec(self,):
        """
        Ejecuta un ChatBot para resolver errores
        :return: void
        """
        if self.chatbot.errorDict == {}:
            self.chatbot.output.exec('ERROR: No hay errores que arreglar.')
        else:
            solveError = CSolveError(self.chatbot)
            self.chatbot.output.exec('Cargando modelo del Chatbot "SolveError".')
            cbp = CBProcessor(solveError)
            cbp.startModel()
            cbp.startPredictor()
            cbp.run()






