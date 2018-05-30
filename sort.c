#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int exchangeCounter, mergeCounter, quickCounter;
void Exchange_sort(int num[],int N);
void Merge_sort(int num[], int left, int right);
void Merge(int num[], int left, int mid, int right);
void Quick_sort(int num[], int left, int right);
int Average();
int N = 0;
int i,j;

int main()
{
	int num[1000];
    int random;     
    
	srand((unsigned)time(NULL));
    random = rand();
	
	printf("Enter N : ");
	scanf("%d" , &N);
	
	for (j=0; j<1000; j++){    
		for (i=0; i<N; i++){          
			random = rand()%100+1;
			num[i]=random;
		}     
		
		Exchange_sort(num,N);
		Merge_sort(num,0,N-1);
		Quick_sort(num,0,N-1); 
	}
	Average();
}


void Exchange_sort(int num[],int N)
{
	int i, j, temp;
	
	for(i=1; i<N; i++)
		for(j=i+1; j<=N; j++)
			if(num[j]<num[i])
			{
				exchangeCounter++;
				temp = num[i];
				num[i] = num[j];
				num[j] = temp;
			}
}

void Merge_sort(int num[], int left, int right)
{
	int mid;

	if(left<right){
		mid = (left + right) / 2;
		Merge_sort(num,left,mid);
		Merge_sort(num,mid+1,right);
		Merge(num,left,mid+1,right);
		mergeCounter++;
	}
}


void Merge(int num[], int left, int mid, int right)
{
	int i, j, k, m;
	int temp[1000];

	i = left;
	j = mid + 1;
	k = left;
	
	while(i<=mid && j<=right){
		if(num[i]<num[j]){
			temp[k] = num[i];
			i++;
		}
		else{
			temp[k] = num[j];
			j++;
		}
	}
	k++;

	if(i > mid){
		for(m=j; m<=right; m++){
			temp[k] = num[i];
			k++;
		}
	}
	else{
		for(m=i; m<=mid; m++){
			temp[k] = num[m];
			k++;
		}
	}

	for(m=left; m<=right; m++){
		num[m] = temp[m];
	}
}

void Quick_sort(int num[], int left, int right)
{
	int pivot, i, j, temp;
	
	if(left<right)
	{
		i = left;
		j = right + 1;
		pivot = num[left];
		do{
			do{ i++; } while (num[i] < pivot);
			do{ j--; } while (num[j] > pivot);

			if(i<j)
			{
				temp = num[i];
				num[i] = num[j];
				num[j] = temp;
			}
		}while(i<j);

		temp = num[left];
		num[left] = num[j];
		num[j] = temp;

		if(left != j){
			quickCounter++;
			Quick_sort(num,left,j-1);
			Quick_sort(num,j+1,right);
		}
		
	}
}

int Average()
{
	printf("Average # of comparisons for Exchange Sort : %d\n", exchangeCounter/1000);
	printf("Average # of comparisons for Merge Sort : %d\n", mergeCounter/1000);
	printf("Average # of comparisons for Quick Sort : %d\n", quickCounter/1000);
}



	
	



