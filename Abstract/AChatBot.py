
from Abstract.AActionSubclasses.NotLineClasses.FinishRunningCB import CFinishRunningCB
import TrainerPredictor

from Abstract.AOutputSubclasses.Screen import CScreen
from Abstract.AInputSubclasses.Keyboard import CKeyboard
import os


class CChatBot(object):

    def __init__(self):
        self.name = ''
        self.intents = []

        # variable que cancela la ejecucion de un chatbot
        self.runChatBot = True

        self.jsonPath = ''
        self.generalPath = ''
        self.actionsPath = ''

        self.errorDict = {}

        self.currentSentence = None
        self.currentIntent = None

        self.unrecognizedSentence = None
        self.unrecognizeIntent = None

        self.listGeneralActions = ['finishRunningChatbot']
        self.actions = {
            'finishRunningChatbot': CFinishRunningCB(self)
        }
        self.TrainerAndPredictor = None
        
        self.input = CKeyboard()
        self.output = CScreen()


    def initializePaths(self):
        pass

    def saveUnrecognizedSentence(self,key,value):
        pass

    def initializate(self):
        if self.TrainerAndPredictor is None:
            self.output.exec('No se puede inicializar porque no existe el modelo.')
        else:
            self.intents = self.TrainerAndPredictor.classes
            self.currentIntent = self.TrainerAndPredictor.intent
            self.name = self.TrainerAndPredictor.chatbotName

    def existModel(self,path):
        return os.path.exists(os.path.join(os.path.sep,path,'model.h5'))

    def startModel(self):
        if not (os.path.exists(self.jsonPath)):
            self.output.exec('No existe el fichero JSON "'+self.jsonPath+'".')
        else:
            if not self.existModel(self.generalPath):
                self.output.exec('running Trainer')
                self.TrainerAndPredictor = TrainerPredictor.CTrainerPredictor()
                self.TrainerAndPredictor.readJSON(self.jsonPath,self.name)
                self.TrainerAndPredictor.createElementsToModel()
                value = self.TrainerAndPredictor.trainingModel(self.generalPath)
                if not value:
                    self.output.exec('No se ha podido generar el Modelo porque se necesita más de 1 Intent con Patterns creados.')
                else:
                    self.TrainerAndPredictor.doPickle()
                    # self.TrainerAndPredictor.closeResource()
                self.output.exec('end to train')
            else:
                self.output.exec('El modelo ya existe')

    def startPredictor(self):
        if not (os.path.exists(self.jsonPath)):
            self.output.exec('No existe el fichero JSON "'+self.jsonPath+'".')
        else:
            self.output.exec('running Predictor')
            if self.TrainerAndPredictor is None:
                self.TrainerAndPredictor = TrainerPredictor.CTrainerPredictor()
                self.TrainerAndPredictor.loadArrays(self.generalPath)
                self.TrainerAndPredictor.readJSON(self.jsonPath,self.name)
                self.TrainerAndPredictor.buildNetwork()
                self.TrainerAndPredictor.loadModel()
            # self.TrainerAndPredictor.closeResource()
            self.setIntentsList()
            self.output.exec('end to predict')

    def setIntentsList(self):
        self.intents = self.TrainerAndPredictor.classes