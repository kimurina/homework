#include <stdio.h>

int n; // node의 총 개수
int m; // color의 수
int l = 2; //binary tree
int G[10][10] = {0,1}; // matrix G
//int x[10] = {0,1}; // 1: exist an adge, 0: no edge, solution
int total_visiting;
int total_nodes;
int i,j,k;

int BACKTRACK(int n);
int GETNEXT(int k);
int BOUND(int k);

int main(){
	scanf("%d",&n);
	for (i=0; i<n; i++)
		for(j=0; j<n; j++)
			scanf("%d", &G[i][j]);
	scanf("%d",&m);
	BACKTRACK(n);
}

int BACKTRACK(int n){
	k=1;
	for(i=1; i<=n; i++)
		G[1][i] = -1;
	while(0<k && k<=n){
		GETNEXT(k);
		if(G[1][k] == -1)
			k--;
		else
			if(k == n){
				for(i=1; i<=n; i++)
					printf("%d\n", G[1][i]);
			}
			else
				k++;
	}
}

int GETNEXT(int k){
	while(i<l){
		i++;
		G[1][k] = G[1][k+1];
		if(BOUND(k) == 1)
			return;
	}
	if(i==1)
		G[1][i] = -1;
}

int BOUND(int k){
	for(i=1; i<k; i++){
		if(G[1][k] == G[1][i])
			return 0;
	}
	return 1;
}





