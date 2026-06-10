from mpi4py import MPI
import numpy as np

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0, 0, 0, 0]

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()  # Fixed
    size = comm.Get_size()  # Fixed

    # Create a grid as square as possible
    grid_row = int(np.floor(np.sqrt(size)))
    grid_column = size // grid_row
    
    # Adjust if product exceeds size
    while grid_row * grid_column > size:
        grid_column -= 1
    while grid_row * grid_column > size:
        grid_row -= 1

    if rank == 0:
        print("Building a %d x %d grid topology for %d processes:" % (grid_row, grid_column, size))
        print("Total processes in grid: %d" % (grid_row * grid_column))
        print("Note: Some processes may not be in the grid if size is not perfect square\n")

    # Create Cartesian topology
    cartesian_communicator = comm.Create_cart(
        dims=(grid_row, grid_column),
        periods=(True, True),  # Periodic boundaries (toroidal)
        reorder=True
    )
    
    # Only processes in the grid will have valid communicator
    if cartesian_communicator != MPI.COMM_NULL:
        my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.Get_rank())
        
        # Get neighbors (shift by 1 in each dimension)
        neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
        neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)
        
        print("Process = %d, row = %d, column = %d" % (rank, my_mpi_row, my_mpi_col))
        print("----> neighbour_processes[UP] = %d" % neighbour_processes[UP])
        print("----> neighbour_processes[DOWN] = %d" % neighbour_processes[DOWN])
        print("----> neighbour_processes[LEFT] = %d" % neighbour_processes[LEFT])
        print("----> neighbour_processes[RIGHT] = %d\n" % neighbour_processes[RIGHT])
    else:
        print("Process %d is not part of the Cartesian grid" % rank)