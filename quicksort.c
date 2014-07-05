#include<stdio.h>
#include<stdlib.h>

#define SIZE 10
void quickSort(int A[], int p, int r);
int partition(int A[], int p, int r);

//Start of main
main(int argc, char* argv[])
{
	
	int A[SIZE];
        int d = 0,n=0,k=0;
        for (d= 0; d < SIZE; d++)
        {
                A[d]=0;
        }

    
    if(argc <2)
    {
                int i =0;
                int j = SIZE;

                printf("Please type %d digitals here, each number a line\n",j);
                for(i =0; i< SIZE; i++)
                {
                        scanf("%d",&A[i]);
                }
		n=SIZE;
    }
    else if(argc ==2)
    {
                int c=0;
                FILE *fp = fopen(argv[1],"r");
		d=0;
                while(fscanf(fp,"%d",&A[d++])!= EOF)
                {
                      /*  printf ("%d",A[d]);*/
                }
				fclose(fp);
				n=d-1;
     }
		
//Calling the sorting function
	quickSort(A, 0, n-1);

//  Printing the sorted array in an output file
FILE *fw=fopen("Quicksort_output.txt","w");	
	for(k = 0; k < n; k++)
	{
		fprintf(fw, "%d\n", A[k]);
	}
	fclose(fw);
}
//End of main

//Recursive sorting function
void quickSort(int A[], int p, int r)
{
	int q;

	while(p < r)
	{
		q = partition(A, p, r);
		quickSort(A, p, (q-1));
		p = q + 1;
	}
}

//Function to find a pivot point which partitions the array to 2 subarrays having smaller numbers than the pivot on 1 side and larger numbers on the other
int partition(int A[], int p, int r)
{
	int x = A[r];
	int i = p-1;
	int j;
	int temp;

	for(j = p; j <= (r-1); j++)
	{
		if(A[j] <= x)
		{
			i++;
			temp = A[i];
			A[i] = A[j];
			A[j] = temp;
		}
	}
	
	int temp = A[i+1];
	A[i+1] = A[r];
	A[r] = temp;

	return (i+1);
}
