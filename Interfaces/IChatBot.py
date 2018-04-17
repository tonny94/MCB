class CChatBot(object):

    def __init__(self):
        self.name = ''
        self.intents = []


        self.jsonPath = ''
        self.generalPath = ''
        self.actionsPath = ''

        self.errorDict = {}

        self.currentSentence = None
        self.currentIntent = None

        self.unrecognizedSentence = None
        self.unrecognizeIntent = None

    def initializePaths(self,chatbotName):
        pass

    def saveUnrecognizedSentence(self,key,value):
        pass