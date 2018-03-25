class Intent:
    """Grandchild class"""
    def __init__(self):
        self.tag = None
        self.patterns = []
        self.responses = []
        self.action = None


    #inicializa el atributo 'Tag'
    def setTag(self, tag):
        if self.tag == None:
            self.tag = tag

    #cambia el 'tag' de la intencion que llama al metodo
    def changeTag(self, tag):
        if self.tag != None:
            self.tag = tag

    #añade un 'patter' a la lista
    def addPattern(self, pattern):
        self.patterns.append (pattern)

    #si exite el pattern en la lista lo borra
    def removePattern(self, pattern):
        if pattern in self.patterns:
            self.patterns.remove(pattern)

    #añade un 'response' a la lista
    def addResponse(self, response):
        self.responses.append (response)

    # si exite el 'response' en la lista lo borra
    def removeResponse(self, response):
        if response in self.responses:
            self.responses.remove(response)

    #inicializa el atributo 'action'
    def setAction(self, action):
        self.action = action

    #pasa a JSON una lista
    def listaToJSON(self,lista):
        if len(lista)>0:
            length = 0
            strJSON = '['
            for elem in lista:
                if length == len(lista)-1:
                    strJSON += '"' + elem + '"]'
                else:
                    strJSON += '"'+elem+'",'
                length +=1

            return strJSON
        else:
            return '[]'

    #pasa a JSON el atributo 'tag'
    def tagToJSON(self):
        if self.tag == None:
            return ''
        else:
            return self.tag

    # pasa a JSON el atributo 'action'
    def actionToJSON(self):
        if self.action == None:
            return ''
        else:
            return self.action

    # pasa el objeto Intent a formato JSON
    def toJSON(self):
        strJson = '{"tag":"'+self.tagToJSON()+'",\n\t\t\t'
        strJson += '"patterns":'+self.listaToJSON(self.patterns)+',\n\t\t\t'
        strJson += '"responses":' + self.listaToJSON(self.responses) + ',\n\t\t\t'
        strJson += '"action":"' + self.actionToJSON() + '"\n\t\t\t'
        strJson += '}'
        return strJson


