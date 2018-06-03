from Abstract.AInput import IInput
import threading
from xmlrpc.server import SimpleXMLRPCServer


class CKeyboard(IInput):
    # def __init__(self):
    #     self.iString=""
    #     thread = threading.Thread(target=self.xmlsvr, args=())
    #     thread.daemon = True                            # Daemonize thread
    #     thread.start()                                  # Start the execution
    #
    # def xmlsvr(self):
    #     server = SimpleXMLRPCServer(("", 8000))
    #     print("Listening on port 8000...")
    #     server.register_instance(self)
    #     server.serve_forever()
    #
    # def asr(self,s):
    #     print("REcibido",s)
    #     self.iString=s
    #     return "ok-from MetaChatBot"
    
    def exec(self):
        value = input('=> ')
        # while self.iString=="":
        #     pass
        # value=self.iString
        # self.iString=""
        return value













