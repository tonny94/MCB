#Clases de acciones
from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine

#Clases generales
import os,json

from TrainerPredictor import CTrainerPredictor


class CBuildChatbot(ActionNotLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot
        self.structureChatbot = None
        self.generalPath = os.path.join(os.path.sep,os.getcwd(),'Chatbots')
        self.structureChatbotPath = ''
        self.structureDirJsonFile = ''
        self.structureDirCodeFile = ''
        self.structureActionsPath = ''

    def exec(self,):
        self.structureChatbot = self.chatbot.currentStructureChatBot
        if self.structureChatbot is None:
            self.chatbot.output.exec('ERROR: No hay un Chatbot actual para construir.')
        else:

            #inicializa las variables
            self.structureChatbotPath = os.path.join(os.path.sep,self.generalPath,self.structureChatbot.name)
            self.structureDirJsonFile = os.path.join(os.path.sep,self.structureChatbotPath,self.structureChatbot.name+'.json')
            self.structureDirCodeFile = os.path.join(os.path.sep,self.structureChatbotPath,self.structureChatbot.name+'.py')
            self.structureActionsPath = os.path.join(os.path.sep,self.structureChatbotPath,'Actions')

            if not (os.path.isdir(self.generalPath)):
                self.chatbot.output.exec('ERROR: No existe la ruta general "',self.generalPath,'".')
            else:
                if not os.path.isdir(self.structureChatbotPath):
                    os.makedirs(self.structureChatbotPath)
                if not os.path.isdir(self.structureActionsPath):
                    os.makedirs(self.structureActionsPath)
                self.createJSON()
                self.createCodeFile()
                self.chatbot.output.exec('Se ha construido el chatbot "'+self.structureChatbot.name+ '" correctamente.')

    def createJSON(self):
        with open(self.structureDirJsonFile, 'w', encoding='utf-8') as f:
            json.dump(self.chatbotToJson(), f)


        # jsonFile = open(self.structureDirJsonFile, 'w')
        # jsonFile.write(self.chatbotToJson())
        # jsonFile.close()
        self.startTrainer()

    def chatbotToJson(self):
        strJSON = self.structureChatbot.toJSON()
        return strJSON

    def createCodeFile(self):
        codeFile = open(self.structureDirCodeFile, 'w')
        codeFile.write(self.chatbotToCode())
        codeFile.close()

    def chatbotToCode(self):
        strCode = self.structureChatbot.toCode(self.chatbot.listGeneralActions,self.structureActionsPath)
        return strCode

    def startTrainer(self):
        VTrainer = CTrainerPredictor()
        VTrainer.readJSON(self.structureDirJsonFile,self.structureChatbot.name)
        VTrainer.createElementsToModel()
        value = VTrainer.trainingModel(self.structureChatbotPath)
        if not value:
            self.chatbot.output.exec('No se ha podido generar el Modelo porque se necesita más de 1 Intent con Patterns creados.')
        else:
            VTrainer.doPickle()
            self.chatbot.output.exec('Modelo de "'+self.structureChatbot.name+'" creado.')
