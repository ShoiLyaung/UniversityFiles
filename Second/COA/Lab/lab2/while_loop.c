// OpenMP header
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int i = 0;
	const int N = 50;
	int cnt = 0;
	int a[N];

	srand(2);
	for (i=0; i<N; i++)
	{
		a[i] = rand()%3;	
	}

	#pragma omp parallel default(shared)
	i = 0;
	while (i<N)
	{
		printf("i=%d is executed by thread %d\n", i, omp_get_thread_num());
		if (a[i] == 0)
		{
			cnt += 1;
		}
		i++;
	}
	printf("There are %d random numbers equaling 0\n", cnt);
	return(0);
}
