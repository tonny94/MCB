#! /bin/bash
# -*- coding: utf-8 -*-


import os,inspect,json
from Abstract.AChatBot import CChatBot
from Abstract.AActionSubclasses.NotLineClasses.NotRecognizedSentence import CNotRecognizedSentence
from Chatbots.SolveError.Actions.LineClasses.SelectIntent import CSelectIntent
from Chatbots.SolveError.Actions.LineClasses.SelectError import CSelectError
from Chatbots.SolveError.Actions.NotLineClasses.SaveSolution import CSaveSolution
from Chatbots.SolveError.Actions.NotLineClasses.ListResolvedErrors import CListResolvedErrors
from Chatbots.SolveError.Actions.NotLineClasses.ListUnresolvedErrors import CListUnresolvedErrors
from Chatbots.SolveError.Actions.NotLineClasses.ListIntents import CListIntents
from Chatbots.SolveError.Actions.NotLineClasses.ProcessSolutions import CProcessSolutions

from Chatbots.SolveError.Actions.NotLineClasses.ShowCurrentSolution import CShowCurrentSolution
from Chatbots.SolveError.Actions.LineClasses.SelectChatbot import CSelectChatbot
from Chatbots.SolveError.Actions.NotLineClasses.ListChatbots import CListChatbots

class CSolveError(CChatBot):
    """Father class"""

    def __init__(self):
        super(CSolveError, self).__init__()

        #variables para cargar las soluciones resueltas o por resolver
        self.listUnresolvedErrors = {}
        self.listResolvedErrors = {}
        self.listIntens = []
        self.currentSolution = {}

        #variables para las rutas del chatbot a resolver
        self.generalPathChatbotToSolve = ''
        self.nameChatbotToSolve=''
        self.pathErrorFileChatbotToSolve = ''
        self.pathJSONChatbotToSolve = ''

        #variables de la solucion dada por el usuario
        self.senteceToSolve = None
        self.intentToSolve = None

        #acciones propias del SolveError
        self.actionsCB = {
                            'selectChatbot': CSelectChatbot(self),
                            'listChatbot': CListChatbots(self),
                            'selectError': CSelectError(self),
                            'selectIntent': CSelectIntent(self),
                            'saveSolution': CSaveSolution(self),
                            'listResolvedErros': CListResolvedErrors(self),
                            'listUnresolvedErros': CListUnresolvedErrors(self),
                            'listIntents': CListIntents(self),
                            'showCurrentSolution':CShowCurrentSolution(self),
                            'processSolutions': CProcessSolutions(self)
                        }

        #Metodos para inicializar variables de ruta y lista de chatbots
        self.initializePaths()
        self.listChatbots = self.getChatbots()

    # ------------------------------------------------------------------------------------------------------------------------ #
    # ------------------------------------------------------------------------------------------------------------------------ #

    """
        Inicializa las rutas del SolveError para saver dónde está el fichero de 
        errores, la ruta donde guardar el modelo, etc...
    """
    def initializePaths(self):
        strSplit = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))).split(os.path.sep)
        self.name = strSplit[len(strSplit)-1]
        self.generalPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.jsonPath = os.path.join(os.path.sep,self.generalPath,self.name+'.json')
        self.errorFilePath = os.path.join(os.path.sep, self.generalPath, self.name + '_ErrorFile.json')
        # self.errorSolvedFilePath = os.path.join(os.path.sep, self.generalPath, self.name + '_ErrorSolvedFile.json')

        if not os.path.isfile(self.errorFilePath):
            with open(self.errorFilePath, 'w', encoding='utf-8') as f:
                json.dump({}, f)

        # if not os.path.isfile(self.errorSolvedFilePath):
        #     with open(self.errorSolvedFilePath, 'w', encoding='utf-8') as f:
        #         json.dump({}, f)

    def getChatbots(self):
        self.generalPathChatbotToSolve = os.path.dirname(self.generalPath)
        return os.listdir(self.generalPathChatbotToSolve)

    def printListResolvedErrors(self):
        result = ", ".join('"'+str(key)+'" resuelto con el intent "'+str(value)+'"' for key, value in self.listResolvedErrors.items())
        self.output.exec(result)

    def printListUnresolvedErrors(self):
        result = ", ".join('"'+str(key)+'" que se asoció con el intent "'+str(value)+'"' for key, value in self.listUnresolvedErrors.items())
        self.output.exec(result)

    def printCurrentSolution(self):
        result = "".join('"' + str(key) + '" asociado a la intención "' + str(value) + '"' for key, value in self.currentSolution.items())
        self.output.exec(result)

    def saveSolution(self):
        self.listResolvedErrors[self.senteceToSolve] = self.intentToSolve
        self.currentSolution[self.senteceToSolve] = self.intentToSolve
        del(self.listUnresolvedErrors[self.senteceToSolve])

        self.output.exec('La sentencia "'+ self.senteceToSolve+ '" se ha asociado al Intent "'+self.intentToSolve+'".')
        self.senteceToSolve = None
        self.intentToSolve = None

    def setNameChabot(self,name):
        self.name = name

    def printChatbots(self):
        self.output.exec(self.listChatbots)

    def printIntents(self):
        self.output.exec(self.listIntens)

    def getErrorList(self):
        return self.errorDict

    def setCurrentSentence(self, sentence):
        self.currentSentence = sentence

    def setCurrentIntent(self, intent):
        self.currentIntent = intent

    def setUnrecognizedSentence(self, sentence):
        self.unrecognizedSentence = sentence

    def setUnrecognizedIntent(self, intent):
        self.unrecognizeIntent = intent
