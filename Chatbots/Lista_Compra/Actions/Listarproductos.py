from Abstract.AActionSubclasses.ActionNotLine import ActionNotLine
class CListarproductos(ActionNotLine):

	def __init__(self,chatbot):
		self.chatbot = chatbot

	def exec(self,):

		print("La cesta tiene: ", self.chatbot.cesta)