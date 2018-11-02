from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine
class CListarproductos(ActionNotLine):

	def __init__(self,chatbot):
		self.chatbot = chatbot

	def exec(self,):
		self.chatbot.output.exec("La cesta tiene: " + str(self.chatbot.cesta))