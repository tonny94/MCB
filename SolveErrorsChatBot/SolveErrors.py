#! /bin/bash
# -*- coding: utf-8 -*-


import os
from ChatBotProcessor import CBProcessor

class CSolveError(CBProcessor):
    """Father class"""

    def __init__(self,chatbotName='',jsonPath='',listErrors=[],listSolved=[]):

        self.listErrors = listErrors
        self.listSolved = listSolved
        self.jsonPath = jsonPath
        self.chatbotName = chatbotName
        self.actionSolveError = {'salirChatbot': self.salirChatbot,
                             'listarErrores':self.listarErrores,'listarErroresProcesados':self.listarErrorProcesados
                             }

        #super().__init__()

    def startTrainerClass(self,chatbotName='solveErrors', jsonFile=os.path.join(os.sep, os.getcwd(), 'SolveErrorsChatBot','solveerrors.json'), pathModel=os.path.join(os.sep, os.getcwd(), 'SolveErrorsChatBot')):
        CBProcessor.__init__(self)
        self.preparateModel(chatbotName, jsonFile, pathModel)

    def startResponseClass(self, chatbotName='solveErrors', jsonFile=os.path.join(os.sep, os.getcwd(), 'SolveErrorsChatBot','solveerrors.json'), pathModel=os.path.join(os.sep, os.getcwd(), 'SolveErrorsChatBot')):
        CBProcessor.__init__(self)
        self.preparateResponse(chatbotName, jsonFile, pathModel)



    def run(self):
        self.startTrainerClass()
        # self.startResponseClass()
        # while not self.runChatBot is False:
        #
        #     sentence = ''
        #     sentence = input('=>')
        #     if not (sentence is 's'):
        #         print(self.classify(sentence))
        #         self.execResponse(sentence)



    def execResponse(self,sentence):

        self.response(sentence)
        self.currentAction = self.chatbotResponse.action
        if not self.currentAction == '':
            self.updateActionsCBProcessor(self.actionSolveError)
            self.actions[self.chatbotResponse.action]()

        # reinicia el atributo
        self.chatbotResponse.action = ''
        self.errorSentence = ''


    def setParametters(self,chatbotName,dicionario):
        self.chatbotName = chatbotName
        #self.intents = intents
        self.listaSentenciasNoReconocidas = dicionario[chatbotName][0]
        self.listaSentenciasYaReconocidas = dicionario[chatbotName][1]

    def salirChatbot(self):
        #cancelar ejecucion del chatbot
        self.runChatBot = True

    def listarErrores(self):
        print(self.listErrors)

    def listarErrorProcesados(self):
        print(self.listSolved)

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