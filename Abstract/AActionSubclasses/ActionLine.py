from Abstract.AAction import IAction

class ActionLine(IAction):
    listKeysWordsCancelRunning = ['cancelar','abortar','parar','no seguir','cancelar ejecucion','parar ejecucion','dejar de ejecutar','abortar ejecucion','error']

    def exec(self):
        pass

    def checkCancellation(self,sentence):
        pass




#         self.actions = {'saludar': self.saludar, 'despedir': self.despedir, 'saludar1': self.saludar1}
#
#         def exectAction(self, functionName, *args):
#             self.actions[functionName](*args)
#
#         def saludar(self, a, b):
#             print('probando ' + str(a) + ' con ' + str(b))
#
#         def despedir(self):
#             print('adios')
#
#         def saludar1(self, a):
#             print('solo 1' + str(a))
# objAction = Action()
#
# objAction.exectAction('saludar','primero',9)
# objAction.exectAction('despedir')
# objAction.exectAction('saludar1',4)








