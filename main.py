#! /bin/bash
# -*- coding: utf-8 -*-

import os
from ChatBotProcessor import CBProcessor
from Chatbots.MetaChatBot.MetaChatBot import CMetaChatBot

import keras
import sys
import tensorflow as tf
print("pyton: {}, keras: {}".format(sys.version,keras.__version__))

#METACHATBOT
mcb = CMetaChatBot()
cbp = CBProcessor(mcb)
cbp.startModel()
cbp.startPredictor()
cbp.run()

"""
FALTA:
1.- clases INPUT , OUTPUT   - LISTO
2.- metodo para cargar los chatbots creados al MetaChatBot      -   LISTO
3.- metodo para ejecutar un chatbot desde el MetaChatBot
"""






