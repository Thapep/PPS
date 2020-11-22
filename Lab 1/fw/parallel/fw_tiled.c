/*
  Tiled version of the Floyd-Warshall algorithm.
  command-line arguments: N, B
  N = size of graph
  B = size of tile
  works only when N is a multiple of B
*/
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include "util.h"

inline int min(int a, int b);
inline void FW(int **A, int K, int I, int J, int N);

int main(int argc, char **argv)
{
     int **A;
     int i,j,k;
     struct timeval t1, t2;
     double time;
     int B=64;
     int N=1024;

     if (argc != 3){
        fprintf(stdout, "Usage %s N B\n", argv[0]);
        exit(0);
     }

     N=atoi(argv[1]);
     B=atoi(argv[2]);

     A=(int **)malloc(N*sizeof(int *));
     for(i=0; i<N; i++)A[i]=(int *)malloc(N*sizeof(int));

     graph_init_random(A,-1,N,128*N);

     gettimeofday(&t1,0);

     /* 
      * k is the step number
      * i, j are the row and column numbers
      * N is the size of graph
      * B is the size of tile
      */

     /*
      * Because of the nature of the algortithm, we need each block of code
      * that can run in parallel to finish before we move on to the next. 
      * One idea is to use the directive #pragma omp barrier after each block 
      * of parallel code to ensure the meeting of the dependency conditions.
      */


     /* For every B sized tile (of N total): */
     for(k=0;k<N;k+=B){
	/* 
	 * Firstly compute FW for the K-th diagonal tile
	 */
        FW(A,k,k,k,B);

	/*
	 * Then compute the tiles on the k-th row and k-th column.
	 * We can try to parallelize this!
	 */

	/* N, B, k should be private, i and j shared */
       
	#pragma omp parallel
	{
		#pragma omp single
		{
			for(i=0; i<k; i+=B)
			   #pragma omp task
	        	   {FW(A,k,i,k,B);}
		
		        for(i=k+B; i<N; i+=B)
			   #pragma omp task
		           {FW(A,k,i,k,B);}
		
		        for(j=0; j<k; j+=B)
			   #pragma omp task
		           {FW(A,k,k,j,B);}
		
		        for(j=k+B; j<N; j+=B)
			   #pragma omp task
			   {FW(A,k,k,j,B);}
			   
		}
	}

	#pragma omp barrier

	/*
	 * Then compute the rest of the tiles for this step.
	 * We can also parallelize these computations!
	 */
	#pragma omp parallel
	{
		#pragma omp single
		{	

	        for(i=0; i<k; i+=B)
	           for(j=0; j<k; j+=B)
	                #pragma omp task
			{FW(A,k,i,j,B);}

	        for(i=0; i<k; i+=B)
	           for(j=k+B; j<N; j+=B)
	                #pragma omp task
			{FW(A,k,i,j,B);}
                    
		for(i=k+B; i<N; i+=B)
		   for(j=0; j<k; j+=B)
  	                #pragma omp task
			{FW(A,k,i,j,B);}

  	        for(i=k+B; i<N; i+=B)
  	           for(j=k+B; j<N; j+=B)
  	                #pragma omp task
			{FW(A,k,i,j,B);}
  	   	}
	}
	#pragma omp barrier
/* End of big k for loop */
}

     gettimeofday(&t2,0);

     time=(double)((t2.tv_sec-t1.tv_sec)*1000000+t2.tv_usec-t1.tv_usec)/1000000;
     printf("FW_TILED,%d,%d,%.4f\n", N,B,time);

     /*
     for(i=0; i<N; i++)
        for(j=0; j<N; j++) fprintf(stdout,"%d\n", A[i][j]);
     */

     return 0;
}

inline int min(int a, int b)
{
     if(a<=b)return a;
     else return b;
}

inline void FW(int **A, int K, int I, int J, int N)
{
     int i,j,k;
     /* We make the base case of FW parallel the same way we did on the fw.c file */ 
     for(k=K; k<K+N; k++)
		#pragma omp parallel for shared(N, k) private(i, j, A)
        for(i=I; i<I+N; i++)
           for(j=J; j<J+N; j++)
              A[i][j]=min(A[i][j], A[i][k]+A[k][j]);
     
}
