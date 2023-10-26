#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 835

void mtrx_multi_prl(int a[N][N], int b[N][N], int c[N][N])
{
int i, j, k;
// parallel matrix multiplication
#pragma omp parallel for shared(a, b, c) private(i, j, k)
for (i = 0; i < N; i++)
	for (j = 0; j < N; j++)
		for (k = 0; k < N; k++)
			c[i][j] += a[i][k] * b[k][j];
}

void mtrx_multi_srl(int a[N][N], int b[N][N], int c[N][N])
{
int i, j, k;
// serial matrix multiplication
//#pragma omp parallel for shared(a, b, c) private(i, j, k)
for (i = 0; i < N; i++)
	for (j = 0; j < N; j++)
		for (k = 0; k < N; k++)
			c[i][j] += a[i][k] * b[k][j];
}

int main(int argc, char *argv[])
{
double begin,end,prl_time,srl_time;
int a[N][N], b[N][N], c[N][N];
int i,j;
// Initialize the matrixes
for (i = 0; i < N; i++)
    for (j = 0; j < N; j++)
    {
        a[i][j] = i+j;
        b[i][j] = i*j;
    }

begin = omp_get_wtime();
mtrx_multi_srl(a, b, c);
end = omp_get_wtime();
srl_time=(end-begin)*1000;
printf("serial time:%fms,  C[0][1] equals to %d\n",srl_time,c[0][1]);

for (i = 0; i < N; i++)
    for (j = 0; j < N; j++)
        c[i][j] = 0;

begin = omp_get_wtime();
mtrx_multi_prl(a, b, c);
end = omp_get_wtime();
prl_time=(end-begin)*1000;
printf("parallel time:%fms,  C[0][1] equals to %d\n",prl_time,c[0][1]);

printf("\nboost:%f\n\n",(srl_time/prl_time));

return 0;
}
