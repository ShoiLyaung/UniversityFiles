// OpenMP header
#include <omp.h>
#include <stdio.h>

int main()
{
	int i;
	const int N = 1000;
	int a = 50;
	int b = 0;

	//#pragma omp parallel for default(shared)
	#pragma omp parallel for default(none) private(i) private(a) private(b)
	//#pragma omp parallel for default(none) private(i) private(a) lastprivate(b)
	//#pragma omp parallel for default(none) private(i) firstprivate(a) lastprivate(b)
	for (i=0; i<N; i++)
	{
		b = a + i;
		printf("a=%d\n", a);
	}

	printf("i=%d\na=%d b=%d (expected a=50 b=1049)\n", i, a, b);
}
