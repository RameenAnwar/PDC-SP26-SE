# pyrefly: ignore [missing-import]
from mpi4py import MPI

comm=MPI.COMM_WORLD
rank = comm.rank
print("my rank is : " , rank)

if rank==0:
    data= 10000000
    destination_process = 1
    comm.send(data,dest=destination_process)
    print ("sending data %s " %data +\
           "to process %d" %destination_process)
   
if rank==1:
    data=comm.recv(source=0)
    print ("data received is = %s" %data)
