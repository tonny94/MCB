class Intent:
    """Grandchild class"""
    def __init__(self):
        self.tag = None
        self.patterns = []
        self.responses = []
        self.context_set = None
        self.context_filter = None
        self.action = None

    def setTag(self, tag):
        if self.tag == None:
            self.tag = tag

    def changeTag(self, tag):
        if self.tag != None:
            self.tag = tag
            """Como vincular el chatbot al que pertenece para cambiar el tag de la intension de ese chatbot"""

    def addPattern(self, pattern):
        self.patterns.append (pattern)

    def removePattern(self, pattern):
        if pattern in self.patterns:
            self.patterns.remove(pattern)

    def addResponse(self, response):
        self.responses.append (response)

    def removeResponse(self, response):
        if response in self.responses:
            self.responses.remove(response)

    def setContextSet(self, context_set):
        self.context_set = context_set

    def setContextFilter(self, context_filter):
        self.context_filter = context_filter

    def setAction(self, action):
        self.action = action




