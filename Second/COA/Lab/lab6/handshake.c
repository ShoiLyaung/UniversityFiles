#include<mpi.h>
#include<stdio.h>
#include<string.h>

int main(int argc, char **argv){
    MPI_Init(&argc, &argv);
    int rank, size, i,tag=111;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

/* 主线程 */
    if(rank == 0){
        char sendMess[] = "REQ";
        int len = strlen(sendMess) + 1;
        for (i=1; i<size; i++){
            MPI_Send(&sendMess, len, MPI_CHAR, i, tag, MPI_COMM_WORLD);
        }

        char recvMess[100];
        for (i=1; i<size; i++){
            MPI_Recv(&recvMess, 100, MPI_CHAR, i, tag,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
            printf("%i received %s from %i\n", rank, recvMess, i);
        }
    }

/* 从线程 */
    else{
        char mess[100];
        MPI_Recv(&mess, 100, MPI_CHAR, 0, tag,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
        printf("%i received %s\n", rank, mess);

        char sendMess[] = "ACK";
        int len = strlen(sendMess) + 1;

        MPI_Send(&sendMess, len, MPI_CHAR, 0, tag, MPI_COMM_WORLD);
    }
    MPI_Finalize();
}