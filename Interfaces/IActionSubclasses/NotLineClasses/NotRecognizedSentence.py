#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales


class CNotRecognizedSentence(ActionLine):

    def __init__(self,sentence):
        self.sentence = sentence

    def exec(self,):
        if self.sentence == '':
            print('No hay una sentencia que guardar.')
        else:
            print('No se ha reconocido la sentencia "',self.sentence,'".')
