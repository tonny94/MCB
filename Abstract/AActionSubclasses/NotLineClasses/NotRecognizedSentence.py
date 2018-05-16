#Clases de acciones

from Abstract.AActionSubclasses.ActionLine import ActionLine

from Abstract.AOutputSubclasses.Screen import CScreen
#Clases generales


class CNotRecognizedSentence(ActionLine):

    def __init__(self,sentence):
        self.sentence = sentence
        self.output = CScreen()
    def exec(self,):
        self.output.exec('No se ha reconocido la sentencia "'+self.sentence+'".')
