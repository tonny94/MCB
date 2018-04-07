#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine

#Clases generales
from ChatBot import ChatBot
from Intent import  Intent


class CDontSaveSentence(ActionLine):

    def __init__(self,sentence):
        self.sentence = sentence

    def exec(self,):
        if self.sentence == '':
            print('No hay una sentencia.')
        else:
            print('No se ha guardado la sentencia "',self.sentence,'".')