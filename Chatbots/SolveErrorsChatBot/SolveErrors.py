#! /bin/bash
# -*- coding: utf-8 -*-


import os,inspect
from Interfaces.IChatBot import CChatBot

class CSolveError(CChatBot):
    """Father class"""

    def __init__(self):
        self.currentStructureChatBot = None
        self.actionSolveError = {'salirChatbot': self.salirChatbot,
                             'listarErrores':self.listarErrores,
                                 'listarErroresProcesados':self.listarErrorProcesados
                             }

        self.initializePaths(self.name)

    def initializePaths(self,chatbotName):
        self.chatbotName = chatbotName
        self.generalPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.jsonPath = os.path.join(os.path.sep,self.generalPath,chatbotName+'.json')

    def saveUnrecognizedSentence(self,key,value):
        newDict = {key:value}
        self.errorDict.update(newDict)

    def salirChatbot(self):
        print('salir chatbot')
        #cancelar ejecucion del chatbot
        self.runChatBot = True

    def listarErrores(self):
        # print(self.listErrors)
        print('listarErrores')

    def listarErrorProcesados(self):
        print('listarErrorProcesados')
        # print(self.listSolved)


    # def startTrainerClass(self,chatbotName='solveErrors', jsonFile=os.path.join(os.sep, os.getcwd(), 'SolveErrorsChatBot','solveerrors.json'), pathModel=os.path.join(os.sep, os.getcwd(), 'SolveErrorsChatBot')):
    #     CBProcessor.__init__(self)
    #     self.preparateModel(chatbotName, jsonFile, pathModel)
    #
    # def startResponseClass(self, chatbotName='solveErrors', jsonFile=os.path.join(os.sep, os.getcwd(), 'SolveErrorsChatBot','solveerrors.json'), pathModel=os.path.join(os.sep, os.getcwd(), 'SolveErrorsChatBot')):
    #     CBProcessor.__init__(self)
    #     self.preparePredictor(chatbotName, jsonFile, pathModel)
    #
    #
    #
    # def run(self):
    #     self.startTrainerClass()
    #     # self.startResponseClass()
    #     # while not self.runChatBot is False:
    #     #
    #     #     sentence = ''
    #     #     sentence = input('=>')
    #     #     if not (sentence is 's'):
    #     #         print(self.doClassification(sentence))
    #     #         self.execPrediction(sentence)
    #
    #
    #
    # def execPrediction(self, sentence):
    #
    #     self.doPrediction(sentence)
    #     self.currentAction = self.chatbotResponse.action
    #     if not self.currentAction == '':
    #         self.updateActionsCBProcessor(self.actionSolveError)
    #         self.actions[self.chatbotResponse.action]()
    #
    #     # reinicia el atributo
    #     self.chatbotResponse.action = ''
    #     self.errorSentence = ''
    #
    #
    # def setParametters(self,chatbotName,dicionario):
    #     self.chatbotName = chatbotName
    #     #self.intents = intents
    #     self.listaSentenciasNoReconocidas = dicionario[chatbotName][0]
    #     self.listaSentenciasYaReconocidas = dicionario[chatbotName][1]



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