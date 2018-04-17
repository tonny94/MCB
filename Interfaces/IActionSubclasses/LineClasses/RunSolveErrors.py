#! /bin/bash
# -*- coding: utf-8 -*-

#Clases de acciones

from Interfaces.IActionSubclasses.ActionLine import ActionLine
from Chatbots.SolveErrorsChatBot.SolveErrors import CSolveError
# from ChatBotProcessor import CBProcessor
#Clases generales


class CRunSolveErrors(ActionLine):

    def __init__(self,chatbotProcessor):
        self.chatbotProcessor = chatbotProcessor

    def exec(self,):
        if self.chatbotProcessor.currentRunningChatbot.getErrorList() == {}:
            print('ERROR: No hay errores que arreglar.')
        else:
            solveError = CSolveError()

            # cbp = CBProcessor()






