#! /bin/bash
# -*- coding: utf-8 -*-

#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine
from SolveErrorsChatBot.SolveErrors import CSolveError
#Clases generales


class CRunSolveErrors(ActionLine):

    def __init__(self,chatbotName,jsonChatbot,dictErrores):
        self.chatbotName = chatbotName
        self.jsonChatbot = jsonChatbot
        self.dictErrores = dictErrores

    def exec(self,):
        if self.dictErrores == {}:
            print('ERROR: No hay errores que solventar.')
        elif not self.chatbotName in self.dictErrores:
            print('ERROR: No hay errores que solventar para el chatbot "',self.chatbotName,'".')
        else:
            listErrors = self.dictErrores[self.chatbotName][0]
            listSolved = self.dictErrores[self.chatbotName][1]
            solveError = CSolveError(self.chatbotName,self.jsonChatbot,listErrors,listSolved)
            solveError.run()
