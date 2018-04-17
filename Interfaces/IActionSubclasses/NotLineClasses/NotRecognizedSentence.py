#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CNotRecognizedSentence(ActionLine):

    def __init__(self,sentence):
        self.sentence = sentence

    def exec(self,):
        print('No se ha reconocido la sentencia "',self.sentence,'".')
