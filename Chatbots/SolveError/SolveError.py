#! /bin/bash
# -*- coding: utf-8 -*-


import os,inspect
from Abstract.AChatBot import CChatBot
from Abstract.AActionSubclasses.NotLineClasses.NotRecognizedSentence import CNotRecognizedSentence
from Chatbots.SolveError.Actions.LineClasses.SelectIntent import CSelectIntent
from Chatbots.SolveError.Actions.LineClasses.SelectError import CSelectError
from Chatbots.SolveError.Actions.NotLineClasses.SaveSolution import CSaveSolution
from Chatbots.SolveError.Actions.NotLineClasses.ListResolvedErrors import CListResolvedErrors
from Chatbots.SolveError.Actions.NotLineClasses.ListUnresolvedErrors import CListUnresolvedErrors
from Chatbots.SolveError.Actions.NotLineClasses.ListIntents import CListIntents
from Chatbots.SolveError.Actions.NotLineClasses.ProcessSolutions import CProcessSolutions




class CSolveError(CChatBot):
    """Father class"""

    def __init__(self,chatbot):
        super(CSolveError, self).__init__()
        self.chatbot = chatbot
        self.listUnresolvedErrors = self.chatbot.errorDict
        self.listResolvedErrors = {}
        self.listIntens = self.chatbot.intents

        self.senteceToSolve = None
        self.intentToSolve = None

        self.actionsCB = {
                            'selectError':CSelectError(self),
                            'selectIntent':CSelectIntent(self),
                            'saveSolution': CSaveSolution(self),
                            'listResolvedErros':CListResolvedErrors(self),
                            'listUnresolvedErros':CListUnresolvedErrors(self),
                            'listIntents':CListIntents(self),
                            'processSolitions':CProcessSolutions(self)
                        }

        self.initializePaths()

    def initializePaths(self):
        strSplit = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))).split(os.path.sep)
        self.name = strSplit[len(strSplit)-1]
        self.generalPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.jsonPath = os.path.join(os.path.sep,self.generalPath,self.name+'.json')

    # def saveUnrecognizedSentence(self,key):
    #     self.errorDict.append(key)

    # def execPrediction(self,sentence):
    #     valorClasificacion = self.TrainerAndPredictor.classify(sentence)
    #     if (not valorClasificacion == []) and valorClasificacion[0][1] >= 0.9:
    #         self.TrainerAndPredictor.predict(sentence)
    #         self.currentAction = self.TrainerAndPredictor.action
    #
    #         if not self.currentAction == '':
    #             # self.updateActionsCBProcessor(self.actionsMetaCB)
    #             self.setCurrentSentence(sentence)
    #             self.setCurrentIntent(self.TrainerAndPredictor.intent)
    #             self.actions[self.currentAction].exec()
    #             self.TrainerAndPredictor.action = ''
    #
    #         # reinicia el atributo
    #         self.setUnrecognizedSentence(None)
    #         self.setUnrecognizedIntent(None)
    #     else:
    #         # guarda la sentencia que no se reconocio
    #         self.setUnrecognizedSentence(sentence)
    #         value = valorClasificacion[0][0] #self.currentRunningChatbot.TrainerAndPredictor.getIntent(valorClasificacion[0][0])
    #         self.setUnrecognizedIntent(value)
    #         CNotRecognizedSentence(self.unrecognizedSentence).exec()

    def printListResolvedErrors(self):
        size = len(self.listResolvedErrors)
        start = 0
        strToPrint = '[ '
        for k in self.listResolvedErrors.keys():

            if start == size:
                strToPrint += k + ' asociado a ' + self.listResolvedErrors[k]
            else:
                strToPrint += k + ' asociado a ' + self.listResolvedErrors[k] + ','

            start += 1

        strToPrint += ' ]'
        self.output.exec(strToPrint)

    def printListUnresolvedErrors(self):
        size = len(self.listResolvedErrors)
        start = 0
        strToPrint = '[ '
        for k in self.listUnresolvedErrors.keys():

            if start == size:
                strToPrint += k + ' asociado a ' + self.listUnresolvedErrors[k]
            else:
                strToPrint += k + ' asociado a ' + self.listUnresolvedErrors[k] + ','
            start += 1
        strToPrint += ' ]'
        self.output.exec(strToPrint)

    def solveSentence(self):
        self.listResolvedErrors[self.senteceToSolve] = self.intentToSolve
        del(self.listUnresolvedErrors[self.senteceToSolve])
        self.output.exec('La sentencia "'+ self.senteceToSolve+ '" se ha asociado al Intent "'+self.intentToSolve+'".')
        self.senteceToSolve = None
        self.intentToSolve = None

    def setNameChabot(self,name):
        self.name = name

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


    """
    para editar json
    
    with open('pruebaEdicionJSON.json','r+') as f:
    data = json.load(f)
    intents = data['chatbotprocessor']        
    intent = intents[0]
    intent['patterns'].append('123asd123')
    f.seek(0)
    json.dump(data,f,indent=4)
    f.truncate() 
    
    """