#include<stdio.h>

int x[10],G[10][10];
int n,i,j,m;


void BOUND(int k){
	while(1)
	{
		x[k]=(x[k]+1)%(m+1);
		if(x[k]==0)
			return;
		for(j=1;j<=n;j++){
			if(G[k][j]!=0&&(x[k]==x[j]))
				break;
		}
		if(j==n+1)
			return;
	}
}

void GETNEXT(int k){
	do
	{
		BOUND(k);
		if(x[k]==0)
			return;
		if(k==n){
			for(i=1;i<=n;i++)
				printf("%d ",x[i]);
			printf("\n");
		}
		else{
			GETNEXT(k+1);
		}
	}while(k<n+1);
}

void main(){
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		for(j=1; j<=n; j++)
			scanf("%d", &G[i][j]);
	scanf("%d", &m);
	printf("\n");
	
	G[i][j]=1;
	G[j][i]=1;
	
	for(i=0;i<=n;i++)
		x[i]=0;
	GETNEXT(1);
}




