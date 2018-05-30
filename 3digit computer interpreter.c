#include <stdio.h>

#define SIZE 1000

void input(int M[]);

int interpret(int M[], int R[]);

void print(int count, int R[], int M[]);

 
int main(){


	int M[SIZE]={0};

	int R[10]={0};

	int count;

 

	input(M);

	count = interpret(M, R);

	print(count, R, M);

	

	return 0;

}

 

void input(int M[]){

	int i;

	for(i=0; i<SIZE; i++){

		scanf("%d", &M[i]);

		if(M[i] == 0)

			break;

	}
	printf("명령어 실행 횟수: ");
}

 

int interpret(int M[], int R[]){

	int PC = 0;  

	int count;

	int opcode, op1, op2;

 

	for(count = 1; M[PC] != 100; count++){

		opcode = M[PC]/100;

		op1 = (M[PC]/10)%10;

		op2 = M[PC]%10;

		PC++;

	    switch(opcode){
		     case 2: 
				 R[op1] = op2;
				 break;

		     case 3:
				 R[op1] = (R[op1]+op2)%1000;
				 break;

		     case 4:
				 R[op1] = (R[op1]*op2)%1000;
				 break;

			 case 5:
				 R[op1] = R[op2];
				 break;

			 case 6:
				 R[op1] = (R[op1]+R[op2])%1000;
				 break;

			 case 7: 
				 R[op1] = (R[op1]*R[op2])%1000;
				 break;

			 case 8:
				 R[op1] = M[R[op2]];
				 break;
			 
			 case 9:
				 M[R[op2]] = R[op1];
				 break;

			 case 0:
				 if(R[op2]!=0)
					 PC = R[op1];
				 break;
				
			 case 1:
				 break;

		}
	}

	return count;
}

void print(int count, int R[], int M[]){
	int i;
	printf("%d\n", count);
	
	printf("[레지스터 값 출력]\n");
	for(i=0; i<10; i++)
		printf("R[%d] = %d\n", i, R[i]);
	
	printf("[메모리 변수 값 출력]\n");
	for(i=0; M[i]!=0; i++)
		printf("M[%d] = %d\n", i, M[i]);
}