#Clases de acciones

from Abstract.AActionSubclasses.ActionLine import ActionLine
import os
#Clases generales

from ChatBotProcessor import CBProcessor

class CStartRunningChatbot(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        self.chatbot.showRandomResponse()
        sentence = self.chatbot.input.exec()
        if not (self.checkCancellation(sentence)):
            if not self.chatbot.isEmpty(sentence):
                if not sentence in self.chatbot.dictChatBots.keys():
                    self.chatbot.output.exec('No se ha encontrado el Chatbot "'+sentence+'".')
                else:
                    self.executeChatbot(sentence)
            else:
                self.chatbot.output.exec('No se admiten valores vacíos.')

    def checkCancellation(self, sentence):
        if (sentence.lower() in self.listKeysWordsCancelRunning):
            self.chatbot.output.exec('Se ha cancelado la operación.')
            self.chatbot.unrecognizedSentence = self.chatbot.currentSentence
            return True
        else:
            return False

    def executeChatbot(self,nameChatbot):
        stringToImport = 'Chatbots.'+nameChatbot+'.'+nameChatbot
        pathChatbot = __import__(stringToImport)#.Lista_Compra.Lista_Compra
        pathDirectory = getattr(pathChatbot,nameChatbot)
        pathFile = getattr(pathDirectory,nameChatbot)
        classChatbot = getattr(pathFile,'C'+nameChatbot)

        chatbotInstance = classChatbot()
        self.chatbot.output.exec('Cargando modelo del Chatbot "'+nameChatbot+'".')
        cbp = CBProcessor(chatbotInstance)
        cbp.startModel()
        cbp.startPredictor()
        # self.chatbot.output.exec('Ejecutáncose el Chatbot "'+nameChatbot+'".')
        cbp.run()
        # self.chatbot.output.exec('Se terminó de ejecutar el Chatbot "'+nameChatbot+'".')