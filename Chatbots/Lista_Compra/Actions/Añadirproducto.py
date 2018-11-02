#! /bin/bash
# -*- coding: utf-8 -*-

from Abstract.AActionSubclasses.ActionLine import ActionLine
class CAnadirproducto(ActionLine):

	def __init__(self,chatbot):
		self.chatbot = chatbot

	def exec(self,):
		self.chatbot.showRandomResponse()
		sentence = self.chatbot.input.exec()  # se espera la entrada del usuario.
		if not (self.checkCancellation(sentence)):
			if not self.chatbot.isEmpty(sentence):
				self.chatbot.cesta.append(sentence)
				self.chatbot.output.exec('Se ha instroducido el producto '+sentence)
			else:
				self.chatbot.output.exec('No se admiten valores vacíos.')