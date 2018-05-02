
from Interfaces.IActionSubclasses.NotLineClasses.FinishRunningCB import CFinishRunningCB
import TrainerPredictor
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



    def initializePaths(self):
        pass

    def saveUnrecognizedSentence(self,key,value):
        pass

    def initializate(self):
        if self.TrainerAndPredictor is None:
            print('No se puede inicializar porque no existe el modelo.')
        else:
            self.intents = self.TrainerAndPredictor.classes
            self.currentIntent = self.TrainerAndPredictor.intent
            self.name = self.TrainerAndPredictor.chatbotName

    def existModel(self,path):
        return os.path.exists(os.path.join(os.path.sep,path,'training_data'))

    def startModel(self):
        if not (os.path.exists(self.jsonPath)):
            print('No existe el fichero JSON "',self.jsonPath,".")
        else:
            if not self.existModel(self.generalPath):
                print('running Trainer')
                self.TrainerAndPredictor = TrainerPredictor.CTrainerPredictor()
                self.TrainerAndPredictor.readJSON(self.jsonPath,self.name)
                self.TrainerAndPredictor.createElementsToModel()
                self.TrainerAndPredictor.trainingModel(self.generalPath)
                self.TrainerAndPredictor.doPickle()
                # self.TrainerAndPredictor.closeResource()
                print('end to train')
            else:
                print('El modelo ya existe')

    def startPredictor(self):
        if not (os.path.exists(self.jsonPath)):
            print('No existe el fichero JSON "',self.jsonPath,".")
        else:
            print('running Predictor')
            if self.TrainerAndPredictor is None:
                self.TrainerAndPredictor = TrainerPredictor.CTrainerPredictor()
                self.TrainerAndPredictor.loadArrays(self.generalPath)
                self.TrainerAndPredictor.readJSON(self.jsonPath,self.name)
                self.TrainerAndPredictor.buildNetwork()
                self.TrainerAndPredictor.loadModel()
            # self.TrainerAndPredictor.closeResource()
            self.setIntentsList()
            print('end to predict')

    def setIntentsList(self):
        self.intents = self.TrainerAndPredictor.classes