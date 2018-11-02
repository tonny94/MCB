from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine
class CListarproductos(ActionNotLine):

	def __init__(self,chatbot):
		self.chatbot = chatbot

	def exec(self,):
		if self.chatbot.cesta == []:
			self.chatbot.output.exec("No hay productos en la cesta.")
		else:
			self.chatbot.output.exec("La cesta tiene: " + self.chatbot.listToString(self.chatbot.cesta))