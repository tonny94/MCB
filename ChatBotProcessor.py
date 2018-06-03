#! /bin/bash
# -*- coding: utf-8 -*-
from Abstract.AOutputSubclasses.Screen import CScreen

from Abstract.AInputSubclasses.Keyboard import CKeyboard

from Abstract.AInteractor import IInteractor

class CBProcessor(object):

    def __init__(self,chatbot):
        self.currentRunningChatbot = chatbot
        self.currentAction = ''
        self.updateActionsCBProcessor()
        self.ouput = IInteractor.output
        self.input = IInteractor.input

    def startModel(self):
        self.currentRunningChatbot.startModel()

    # def rebuildModel(self):
    #     self.currentRunningChatbot.rebuildModel()

    def startPredictor(self):
        self.currentRunningChatbot.startPredictor()

    ## Encuentra las posibles respuestas ##
    def doClassification(self, sentence):
        return self.currentRunningChatbot.TrainerAndPredictor.classify(sentence)

    def doPrediction(self, sentence):
        self.currentRunningChatbot.TrainerAndPredictor.predict(sentence)

    def run(self):
        self.ouput.exec('Se está ejecutando el ChatBot "'+self.currentRunningChatbot.name+'".')
        while self.currentRunningChatbot.runChatBot:
            sentence = self.input.exec()
            # if not (sentence is 's'):
            print(self.doClassification(sentence))
            self.currentRunningChatbot.execPrediction(sentence)

    def updateActionsCBProcessor(self):
        self.currentRunningChatbot.actions.update(self.currentRunningChatbot.actionsCB)


    """
        Metodos para terminar/empezar la ejecucion de un chatbot
    """
    # def finishRunningChatbot(self):
    #     CFinishRunningCB(self.runChatBot,self.currentChatbotChild)
    #
    # def startRunningChatbot(self):
    #     CStartRunningCB(self.currentChatbotChild,self.pathChildrenChatbots)


