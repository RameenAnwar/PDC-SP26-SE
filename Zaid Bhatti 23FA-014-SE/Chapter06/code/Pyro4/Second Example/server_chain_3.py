from __future__ import print_function
import sys
import Pyro5.api
import Pyro5.errors
import chainTopology

current_server = "3"
next_server = "1"

servername = "example.chainTopology." + current_server

daemon = Pyro5.api.Daemon()
obj = chainTopology.Chain(current_server, next_server)
uri = daemon.register(obj)

try:
    ns = Pyro5.api.locate_ns()
except Pyro5.errors.NamingError:
    print("\n[ERROR] Pyro5 Name Server not found!")
    print("Please start the Name Server in another terminal first:")
    print("    python -m Pyro5.nameserver\n")
    sys.exit(1)

ns.register(servername, uri)

# enter the service loop.
print("server_%s started " % current_server)
daemon.requestLoop()


