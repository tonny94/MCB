#! /bin/bash
# -*- coding: utf-8 -*-
from Abstract.AOutputSubclasses.Screen import CScreen

from Abstract.AInputSubclasses.Keyboard import CKeyboard

class CBProcessor(object):

    def __init__(self,chatbot):
        self.currentRunningChatbot = chatbot
        self.currentAction = ''
        self.updateActionsCBProcessor()
        self.ouput = chatbot.output
        self.input = chatbot.input

    def startModel(self):
        self.currentRunningChatbot.startModel()

    def startPredictor(self):
        self.currentRunningChatbot.startPredictor()

    ## Encuentra las posibles respuestas ##
    def doClassification(self, sentence):
        return self.currentRunningChatbot.TrainerAndPredictor.classify(sentence)

    def doPrediction(self, sentence):
        self.currentRunningChatbot.TrainerAndPredictor.predict(sentence)

    def run(self):
        sentence = ''
        while self.currentRunningChatbot.runChatBot:
            sentence = self.input.exec()
            if not (sentence is 's'):
                print(self.doClassification(sentence))
                self.currentRunningChatbot.execPrediction(sentence)
        self.ouput.exec('Se ha terminado de ejecutar el chatbot "'+self.currentRunningChatbot.name+'".')

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


