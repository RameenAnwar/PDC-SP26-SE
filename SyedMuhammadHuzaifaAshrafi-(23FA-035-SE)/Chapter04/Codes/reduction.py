import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

array_size = 10
recvdata = np.zeros(array_size, dtype=np.int64)  # Explicit 64-bit integer
senddata = (rank + 1) * np.arange(array_size, dtype=np.int64)

print("Process %d sending: %s" % (rank, senddata))

comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)

if rank == 0:
    print("Process %d after Reduce - SUM: %s" % (rank, recvdata))