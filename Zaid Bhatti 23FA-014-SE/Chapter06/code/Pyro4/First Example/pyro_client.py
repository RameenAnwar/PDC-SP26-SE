import Pyro5.api
import Pyro5.errors

name = input("What is your name? ").strip()
try:
    server = Pyro5.api.Proxy("PYRONAME:server")    
    print(server.welcomeMessage(name))
except Pyro5.errors.NamingError:
    print("\n[ERROR] Pyro5 Name Server not found!")
    print("Please make sure the Name Server is running:")
    print("    python -m Pyro5.nameserver\n")
except Pyro5.errors.CommunicationError:
    print("\n[ERROR] Connection to welcome server failed!")
    print("Please ensure the welcome server is running first:")
    print("    python pyro_server.py\n")






