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




class CSolveError(CChatBot):
    """Father class"""

    def __init__(self):
        super(CSolveError, self).__init__()
        self.listUnresolvedErrors = {}
        self.listResolvedErrors = {}
        self.listIntens = []

        self.senteceToSolve = None
        self.intentToSolve = None

        self.actionsCB = {
                            'selectChatbot':CSelectChatbot(self),
                            'selectError':CSelectError(self),
                            'selectIntent':CSelectIntent(self),
                            'saveSolution': CSaveSolution(self),
                            'listResolvedErros':CListResolvedErrors(self),
                            'listUnresolvedErros':CListUnresolvedErrors(self),
                            'listIntents':CListIntents(self),
                            'processSolutions':CProcessSolutions(self)
                        }

        self.initializePaths()

    def initializePaths(self):
        strSplit = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))).split(os.path.sep)
        self.name = strSplit[len(strSplit)-1]
        self.generalPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.jsonPath = os.path.join(os.path.sep,self.generalPath,self.name+'.json')
        self.errorFilePath = os.path.join(os.path.sep, self.generalPath, self.name + '_ErrorFile.json')
        self.errorSolvedFilePath = os.path.join(os.path.sep, self.generalPath, self.name + '_ErrorSolvedFile.json')

        if not os.path.isfile(self.errorFilePath):
            with open(self.errorFilePath, 'w', encoding='utf-8') as f:
                json.dump({}, f)

        if not os.path.isfile(self.errorSolvedFilePath):
            with open(self.errorSolvedFilePath, 'w', encoding='utf-8') as f:
                json.dump({}, f)

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
        result = ", ".join('"'+str(key)+'" resuelto con el intent "'+str(value)+'"'  for key, value in self.listResolvedErrors.items())
        self.output.exec(self.listResolvedErrors)

    def printListUnresolvedErrors(self):
        result = ", ".join('"'+str(key)+'" mal asociado con el intent "'+str(value)+'"' for key, value in self.listUnresolvedErrors.items())
        self.output.exec(self.listUnresolvedErrors)

    def solveSentence(self):
        self.listResolvedErrors[self.senteceToSolve] = self.intentToSolve
        del(self.listUnresolvedErrors[self.senteceToSolve])
        # self.listUnresolvedErrors.remove(self.senteceToSolve)
        with open(self.chatbot.errorFilePath, 'r+', encoding='utf-8') as f:
            json_data = json.load(f)
            del(json_data[self.senteceToSolve])
            f.seek(0)
            json.dump(json_data, f, ensure_ascii=False, indent=4)
            f.truncate()
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