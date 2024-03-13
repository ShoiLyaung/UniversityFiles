// OpenMP header
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	int nthreads, tid;

	// Begin of parallel region
	#pragma omp parallel private(nthreads, tid)
	{
		// Getting thread number
		tid = omp_get_thread_num();
		printf("Hello world, from thread = %d\n", tid);
		
		if (tid == 0)
		{
			// Getting the total number of thread
			nthreads = omp_get_num_threads();
			printf("Number of threads = %d\n", nthreads);
		}
	}
	return(0);
}
