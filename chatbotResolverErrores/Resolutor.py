from ChatBot import ChatBot
from ChatBotProcessor import CBProcessor
from Intent import Intent
import os
import curses


class Resolutor(CBProcessor):
    """Father class"""

    def __init__(self):
        self.listaSentenciasNoReconocidas = []
        self.listaSentenciasYaReconocidas = []
        self.intents = []
        self.chatbotName = ''

    def iniciarTRainerClass(self, chatbotName='resolutor', jsonFile=os.getcwd()+'\\chatbotResolverErrores\\chatbotresolvererrores.json', pathModel=os.getcwd()+'\\chatbotResolverErrores\\tmp'):
        CBProcessor.__init__(self)
        self.preparateModel(chatbotName, jsonFile, pathModel)

    def iniciarResponseClass(self, chatbotName='resolutor', jsonFile=os.getcwd()+'\\chatbotResolverErrores\\chatbotresolvererrores.json', pathModel=os.getcwd()+'\\chatbotResolverErrores\\tmp'):
        CBProcessor.__init__(self)
        self.preparateResponse(chatbotName, jsonFile, pathModel)
        self.actions.update({'salirChatbot': self.salirChatbot,
                             'listarErrores':self.listarErrores,'listarErroresProcesados':self.listarErrorProcesados
                             }
                            )
    def setParametters(self,chatbotName,dicionario):
        self.chatbotName = chatbotName
        #self.intents = intents
        self.listaSentenciasNoReconocidas = dicionario[chatbotName][0]
        self.listaSentenciasYaReconocidas = dicionario[chatbotName][1]

    def salirChatbot(self):
        #cancelar ejecucion del chatbot
        print('chatbot cancelado')

    def listarErrores(self):
        print(self.listaSentenciasNoReconocidas)

    def listarErrorProcesados(self):
        print(self.listaSentenciasYaReconocidas)