from Intent import Intent

class ChatBot:
    """Son class"""
    def __init__(self):
        self.name = None
        self.dicIntents = {}
        self.currentIntent = None

    def setName(self, name):
        if self.name == None:
            self.name = name

    def changeName(self, name):
        if self.name != None:
            self.name = name

    def addIntent(self, nameIntent):
        myIntent = Intent()
        myIntent.setTag(nameIntent)
        self.dicIntents[nameIntent] = myIntent
        self.currentIntent = nameIntent
        return myIntent

    def removeIntent(self, nameIntent):
        myIntent = None

        if nameIntent in self.dicIntents:
            myIntent = self.dicIntents[nameIntent]
            del self.dicIntents[nameIntent]

        if nameIntent is self.currentIntent:
            self.currentIntent = None

        return myIntent


    def selectIntent(self, nameIntent):
        if nameIntent in self.dicIntents:
            self.currentIntent = nameIntent
            return self.dicIntents[nameIntent]

        return None

    def setCurrentIntent(self, nameIntent):
        if nameIntent in self.dicIntents:
            self.currentIntent = nameIntent
        elif nameIntent is None:
            self.currentIntent = None
