from __future__ import print_function
import Pyro5.api
import Pyro5.errors

try:
    obj = Pyro5.api.Proxy("PYRONAME:example.chainTopology.1")
    # Call process to trigger execution and network connection
    result = obj.process(["hello"])
    print("Result=%s" % result)
except Pyro5.errors.NamingError:
    print("\n[ERROR] Pyro5 Name Server not found!")
    print("Please make sure the Name Server is running:")
    print("    python -m Pyro5.nameserver\n")
except Pyro5.errors.CommunicationError:
    print("\n[ERROR] Connection to chain server 1 failed!")
    print("Please ensure all three chain servers are running first:")
    print("    python server_chain_1.py")
    print("    python server_chain_2.py")
    print("    python server_chain_3.py\n")


