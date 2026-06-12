from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print("my rank is %i" % (rank))

if rank == 1 and size > 5:  # Only if enough processes
    data_send = "a"
    destination_process = 5
    source_process = 5
    
    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)
    
    print("sending data %s to process %d" % (data_send, destination_process))
    print("data received is = %s" % data_received)

elif rank == 5 and size > 5:  # Only if enough processes
    data_send = "b"
    destination_process = 1
    source_process = 1
    
    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)
    
    print("sending data %s to process %d" % (data_send, destination_process))
    print("data received is = %s" % data_received)

else:
    print("Process %d has nothing to do (need at least 6 processes)" % rank)