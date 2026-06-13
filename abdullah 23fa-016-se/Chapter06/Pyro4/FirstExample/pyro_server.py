import Pyro5.api
import Pyro5.errors

class Server(object):
    @Pyro5.api.expose
    def welcomeMessage(self, name):
        return ("Hi welcome " + str (name))

def startServer():
    server = Server()
    # make a Pyro daemon
    daemon = Pyro5.api.Daemon()             
    # locate the name server running
    try:
        ns = Pyro5.api.locate_ns()
    except Pyro5.errors.NamingError:
        print("\n[ERROR] Pyro5 Name Server not found!")
        print("To run this recipe, you must first start the Name Server in another terminal:")
        print("    python -m Pyro5.nameserver")
        print("Then, run this script again.\n")
        return
    # register the server as a Pyro object
    uri = daemon.register(server)  
    # register the object with a name in the name server
    ns.register("server", uri)   
    # print the uri so we can use it in the client later
    print("Ready. Object uri =", uri)
    # start the event loop of the server to wait for calls
    daemon.requestLoop()                   


if __name__ == "__main__":
    startServer()


