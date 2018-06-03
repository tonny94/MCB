#! /bin/bash
# -*- coding: utf-8 -*-

#Clases de acciones

from Abstract.AActionSubclasses.ActionLine import ActionLine
from Chatbots.SolveError.SolveError import CSolveError
from ChatBotProcessor import CBProcessor
#Clases generales


class CRunSolveErrors(ActionLine):

    def __init__(self,chatbot):
        self.chatbot = chatbot

    def exec(self,):
        if self.chatbot.errorDict == {}:
            self.chatbot.output.exec('ERROR: No hay errores que arreglar.')
        else:

            #metodo para actualizar los patterns de la intencion de "saveInIntent"

            solveError = CSolveError(self.chatbot)
            self.chatbot.output.exec('Cargando modelo del Chatbot "SolveError".')
            cbp = CBProcessor(solveError)
            cbp.startModel()
            cbp.startPredictor()
            # self.chatbot.output.exec('Ejecutáncose el Chatbot "SolveError".')
            cbp.run()
            # self.chatbot.output.exec('Se terminó de ejecutar el Chatbot "SolveError".')
            # cbp = CBProcessor()






