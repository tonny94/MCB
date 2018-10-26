import os,inspect,json 
from Abstract.AChatBot import CChatBot
from Abstract.AActionSubclasses.NotLineClasses.NotRecognizedSentence import CNotRecognizedSentence
from Chatbots.Lista_Compra.Actions.Añadirproducto import CAnadirproducto
from Chatbots.Lista_Compra.Actions.Eliminarproducto import CEliminarproducto
from Chatbots.Lista_Compra.Actions.Listarproductos import CListarproductos
from Chatbots.Lista_Compra.Actions.Realizarcompra import CRealizarcompra
from Chatbots.Lista_Compra.Actions.Modopago import CModopago
from Chatbots.Lista_Compra.Actions.Cancelarcompra import CCancelarcompra

class CLista_Compra(CChatBot):
	def __init__(self):
		super(CLista_Compra, self).__init__()
		self.cesta =[]
		self.actionsCB = {'añadirProducto':CAnadirproducto(self), 'eliminarProducto':CEliminarproducto(self), 'listarProductos':CListarproductos(self), 'realizarCompra':CRealizarcompra(self), 'modoPago':CModopago(self), 'cancelarCompra':CCancelarcompra(self) }
		self.initializePaths()

	def initializePaths(self):
		strSplit = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))).split(os.path.sep)
		self.name = strSplit[len(strSplit)-1]
		self.generalPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		self.jsonPath = os.path.join(os.path.sep,self.generalPath,self.name+'.json')
		self.errorFilePath = os.path.join(os.path.sep, self.generalPath, self.name + '_ErrorFile.json')
		if not os.path.isfile(self.errorFilePath):
			with open(self.errorFilePath, 'w', encoding='utf-8') as f:
				json.dump({}, f)

	def saveUnrecognizedSentence(self,key,value):
		self.errorDict[key] = value

