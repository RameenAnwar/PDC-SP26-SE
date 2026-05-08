import numpy
from mpi4py import MPI 

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

if rank == 0:
    array_to_share = numpy.arange(size * 2)   # example: 8 items if size=4
    array_to_share = array_to_share.reshape(size, -1)
else:
    array_to_share = None

recvbuf = comm.scatter(array_to_share, root=0)

print("rank", rank, "received", recvbuf)