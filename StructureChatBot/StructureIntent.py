from Abstract.AOutputSubclasses.Screen import CScreen

class CStructureIntent:

    def __init__(self):
        self.tag = ''
        self.patterns = []
        self.responses = []
        self.action = ''
        self.ouput = CScreen()

    #inicializa el atributo 'Tag'
    def setTag(self, tag):
        self.tag = tag

    #añade un 'patter' a la lista, devuelve un estado según cómo haya ido la insercion
    def addPattern(self, pattern):
        if pattern in self.patterns:
            self.ouput.exec('Ya existe "'+pattern+'" en la lista de Patterns de la intencion "'+self.tag+'".')
            return False
        else:
            self.patterns.append(pattern)
            return True
    def addListPatterns(self,listPatterns):
        self.patterns = listPatterns

    #si exite el pattern en la lista lo borra, se encarga de imprimir el estado
    def deletePattern(self, pattern):
        if pattern in self.patterns:
            self.patterns.remove(pattern)
            self.ouput.exec('Se ha eliminado "'+pattern+'" de la lista de Patterns de la intencion "'+self.tag+'".')
        else:
            self.ouput.exec('No existe  "'+pattern+'" en la lista de Patterns de la intencion"'+self.tag+'".')

    #añade un 'predict' a la lista, devuelve un estado según cómo haya ido la insercion
    def addResponse(self, response):
        if response in self.responses:
            self.ouput.exec('Ya existe "'+ response+ '" en la lista de Responses de la intencion "'+self.tag+ '".')
            return False
        else:
            self.responses.append (response)
            return True

    def addListResponse(self,listResponse):
        self.responses = listResponse

    # si exite el 'predict' en la lista lo borra, se encarga de imprimir el estado
    def deleteResponse(self, response):
        if response in self.responses:
            self.responses.remove(response)
            self.ouput.exec('Se ha eliminado "'+response+ '" de la lista de Responses de la intencion "'+self.tag+ '".')
        else:
            self.ouput.exec('No existe  "'+response+ '" en la lista de Responses de la intencion"'+self.tag+ '".')

    #inicializa el atributo 'action'
    def setAction(self, action):
        if action == '':
            self.ouput.exec('Se ha borrado la accion para el Intent "'+self.tag+'". ')
        self.action = action

    def printPatterns(self):
        result = ", ".join(pattern for pattern in self.patterns)
        self.ouput.exec('Los patterns para el Intent "'+self.tag+'" son:'+result)

    def printResponses(self):
        result = ", ".join(pattern for pattern in self.responses)
        self.ouput.exec('Los responses para el Intent "'+self.tag+'" son:'+result)

    def printAction(self):
        self.ouput.exec('La accion del Intent "'+self.tag+'" es:'+self.action)

    #pasa a JSON una lista
    def listToJSON(self, lista):
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
        return self.tag

    # pasa a JSON el atributo 'action'
    def actionToJSON(self):
        return self.action

    # pasa el objeto CStructureIntent a formato JSON
    def toJSON(self):
        strJson = '{"tag":"'+self.tagToJSON()+'",\n\t\t\t'
        strJson += '"patterns":' + self.listToJSON(self.patterns) + ',\n\t\t\t'
        strJson += '"responses":' + self.listToJSON(self.responses) + ',\n\t\t\t'
        strJson += '"action":"' + self.actionToJSON() + '"\n\t\t\t'
        strJson += '}'
        return strJson

    def codeToStructureIntent(self,structure):
        self.setTag(structure['tag'])
        self.addListPatterns(structure['patterns'])
        self.addListResponse(structure['responses'])
        self.setAction(structure['action'])


