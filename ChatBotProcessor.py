#! /bin/bash
# -*- coding: utf-8 -*-




import os
import TrainerPredictor

#Clase para ejecutar ChatbotResolutor
from Interfaces.IActionSubclasses.NotLineClasses.NotRecognizedSentence import CNotRecognizedSentence
from Interfaces.IActionSubclasses.NotLineClasses.SaveSentence import CSaveSentence
from Interfaces.IActionSubclasses.NotLineClasses.DontSaveSentence import CDontSaveSentence
from Interfaces.IActionSubclasses.NotLineClasses.FinishRunningCB import CFinishRunningCB
from Interfaces.IActionSubclasses.NotLineClasses.StartRunningCB import CStartRunningCB
from Interfaces.IActionSubclasses.LineClasses.RunSolveErrors import CRunSolveErrors

class CBProcessor(object):

    def __init__(self,chatbot):
        # variable que cancela la ejecucion de un chatbot
        self.runChatBot = False

        self.currentRunningChatbot = chatbot
        self.currentAction = ''
        # self.currentIntent = ''
        self.actions = {
            'saveSentence': CSaveSentence(self),
            'dontSaveSentence': CDontSaveSentence(self),
            'runSolveErrors': CRunSolveErrors(self),
            #'finishRunningChatbot': self.finishRunningChatbot, 'startRunningChatbot': self.startRunningChatbot
            }

        self.updateActionsCBProcessor()
        self.TrainerAndPredictor = None

    def startTrainerAndPredictorClass(self):
        if not (os.path.exists(self.currentRunningChatbot.jsonPath)):
            print('No existe el fichero JSON "',self.currentRunningChatbot.jsonPath,".")
        else:
            print('running Trainer')
            self.TrainerAndPredictor = TrainerPredictor.CTrainerPredictor()
            self.TrainerAndPredictor.readJSON(self.currentRunningChatbot.jsonPath,self.currentRunningChatbot.chatbotName)
            self.TrainerAndPredictor.createElementsToModel()
            self.TrainerAndPredictor.trainingModel(self.currentRunningChatbot.generalPath)
            self.TrainerAndPredictor.doPickle()
            # self.TrainerAndPredictor.closeResource()
            print('end to train')

    def initializeCurrentChatbot(self):
        if self.TrainerAndPredictor is None:
            print('No se puede inicializar porque no existe el modelo.')
        else:
            self.currentRunningChatbot.setListIntents(self.TrainerAndPredictor.intents)
            self.currentRunningChatbot.setCurrentIntent(self.TrainerAndPredictor.intent)
            self.currentRunningChatbot.setNameChabot(self.TrainerAndPredictor.chatbotName)

    ## Encuentra las posibles respuestas ##
    def doClassification(self, sentence):
        return self.TrainerAndPredictor.classify(sentence)

    def doPrediction(self, sentence):
        self.TrainerAndPredictor.predict(sentence)

    def run(self):
        sentence = ''
        while not self.runChatBot:
            sentence = input('=>')
            if not (sentence is 's'):
                print(self.doClassification(sentence))
                self.execPrediction(sentence)

    def execPrediction(self, sentence):
        valorClasificacion = self.doClassification(sentence)
        if (not valorClasificacion == []) and valorClasificacion[0][1] >= 0.9:
            self.doPrediction(sentence)
            self.currentAction = self.TrainerAndPredictor.action
            # self.currentIntent = self.TrainerAndPredictor.intent
            # comprueba que tenga una accion para ejecutar
            if not self.currentAction == '':
                # self.updateActionsCBProcessor(self.actionsMetaCB)
                self.currentRunningChatbot.setCurrentSentence(sentence)
                self.currentRunningChatbot.setCurrentIntent(self.TrainerAndPredictor.intent)
                self.actions[self.currentAction].exec()
                self.TrainerAndPredictor.action = ''

            # reinicia el atributo
            self.currentRunningChatbot.setUnrecognizedSentence(None)
        else:
            # guarda la sentencia que no se reconocio
            self.currentRunningChatbot.setUnrecognizedSentence(sentence)
            value = self.TrainerAndPredictor.getIntent(valorClasificacion[0][0])
            self.currentRunningChatbot.setUnrecognizedIntent(value)
            self.notSentenceRecognized()

    def updateActionsCBProcessor(self):
        self.actions.update(self.currentRunningChatbot.actions)

    def notSentenceRecognized(self):
        CNotRecognizedSentence(self.currentRunningChatbot.unrecognizedSentence).exec()



    """
        Metodo para ejecutar el Chatbot Resolutor
    """
    # def runResolutorCB(self):
    #     CRunSolveErrors(self.currentChatbotFather,self.dictSentences,self.jsonFileCurrentChatbot)

    """
        Metodos para guardar las sentencias no reconocidas
    """
    def saveSentence(self):
        CSaveSentence(self.currentChatbotFather, self.errorSentence, self.dictSentences).exec()

    def dontSaveSentence(self):
        CDontSaveSentence(self.errorSentence).exec()




    """
        Metodos para terminar/empezar la ejecucion de un chatbot
    """
    def finishRunningChatbot(self):
        CFinishRunningCB(self.runChatBot,self.currentChatbotChild)

    def startRunningChatbot(self):
        CStartRunningCB(self.currentChatbotChild,self.pathChildrenChatbots)


