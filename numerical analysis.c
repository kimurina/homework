#include <stdio.h>
#define es 0.01

double taylor_series();
double find_root_using_bisection();
double find_root_using_false_position();
double equation_system_solver();
double a,b,c,d;
double f(double x)
{
   return a*x*x*x+b+x*x+c*x*d;
}

void main()
{

	 int menu;
  
   while( 1 )
   {
      printf("[ ID : 1315872 ]\n");
      printf("[ Name : ±èÀ¯¸®³ª ]\n");
      printf("\n");
      printf("1. e^x\n\n");
      printf("2. Cubic Equation Solver (Bisection ver.)\n\n");
      printf("3. Cubic Equation Solver (False-position ver.)\n\n");
      printf("4. Equation System Solver \n\n");
	  printf("5. Quit\n\n");
      printf(">");
      scanf_s("%d", &menu);
	  printf("\n");

      if( menu == 1 )
		  taylor_series();
	  else if( menu == 2 )
		  find_root_using_bisection();
	  else if( menu == 3 )
		  find_root_using_false_position();
	  else if( menu == 4)
		  equation_system_solver();
	  else
		  return;
   }
   return;
}


double taylor_series()
{
	
	float x;
	float new_term,taylor_sum=1;
	float k=1;
	int sum=1,i;
	
	printf("x = ");
	scanf_s("%f",&x);
	printf("\n");
	
	for (i=1;i<11;i++)
	{
		sum *= i;
		k *= x;
		new_term= k/sum;
		taylor_sum += new_term;
	}
	
	printf("e^%f = %f\n", x, taylor_sum);
	printf("\n");
	
	return taylor_sum;
}


double find_root_using_bisection()
{

    double ea;
    double xrold=0;
    double xl,xu,xr;
    int count=0; 

	printf("a = ");
	scanf_s("%lf",&a);
	printf("\n");
	printf("b = ");
	scanf_s("%lf",&b);
	printf("\n");
	printf("c = ");
	scanf_s("%lf",&c);
	printf("\n");
	printf("d = ");
	scanf_s("%lf",&d);
	printf("\n");
	printf("xl = ");
	scanf_s("%lf",&xl);
	printf("\n");
	printf("xu = ");
	scanf_s("%lf",&xu);
	printf("\n");

	while(1)
	{
		xr=(xl+xu)/2;

		if(f(xl)*f(xr)<0)
			xu=xr;
		else
			xl=xr;
	
		count++;

		if(xr!=0)
         ea=(xr-xrold)/xr*100;
		
		if(ea>0 && ea<es) break;

		xrold=xr;
	}
	printf("Found root = %f\n",xr);
	printf("\n");

	return xr;
}


double find_root_using_false_position()
{

    double ea;
    double xrold=0;
    double xl,xu,xr;
    int count=0; 

	printf("a = ");
	scanf_s("%lf",&a);
	printf("\n");
	printf("b = ");
	scanf_s("%lf",&b);
	printf("\n");
	printf("c = ");
	scanf_s("%lf",&c);
	printf("\n");
	printf("d = ");
	scanf_s("%lf",&d);
	printf("\n");
	printf("xl = ");
	scanf_s("%lf",&xl);
	printf("\n");
	printf("xu = ");
	scanf_s("%lf",&xu);
	printf("\n");

	while(1)
	{
		xr=xu-(f(xu)*(xl-xu)/(f(xl)-f(xu)));

		if(f(xl)*f(xr)<0)
			xu=xr;
		else
			xl=xr;
	
		count++;

		if(xr!=0)
         ea=(xr-xrold)/xr*100;
		
		if(ea>0 && ea<es) break;

		xrold=xr;
	}
	printf("Found root = %f\n",xr);
	printf("\n");

	return xr;
}

double equation_system_solver()
{
	int n=0;
	double A[10][10]={0,0};
	double B[10][1]={0,0};
	double X[10][1]={0,0};
	int k,i,j;
	double factor=0;
	double sum=0;

	printf("n = ");
	scanf("%d",&n);
	printf("\n");

	printf("A = ");
	
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
			scanf("%f",&A[i][j]);
	}
	printf("\n");

	printf("B = ");

	for(i=1;i<=n;i++)
	{
		scanf("%f",&B[i][1]);
	}
	printf("\n");
	
	
	for(k=1;k<n;k++)
	{
		for(i=k+1;i<=n;i++)
			 {
				 if(A[k][k]!=0)
				 {
					 factor = A[i][k]/A[k][k];
					 A[i][k] = factor;
				 }
				 for(j=k+1;j<=n;j++)
					 A[i][j] -= factor*A[k][j];
		}
	}
	 
	 
	 for(i=2;i<=n;i++)
	 {
		 sum = B[i][1];
		 for(j=1;j<=i-1;j++)
			 {
				 sum -= A[i][j]*B[j][1];
				 B[i][1] = sum;
		 }
	 }
	 
	 
	 X[n][1] = B[n][1]/A[n][n];
	 
	 for(i=n;i>=1;i--)
	 {
		 sum = 0;
		 for(j=i+1;j<=n;j++)
		 {
			 sum += A[i][j]*X[j][1];
		 }
		 
		 if(A[i][i]!=0)
			 X[i][1] = (B[i][1] - sum)/A[i][i];
	 }
	 
	 printf("X = ");
	 
	 for(k=1;k<=n;k++)
	 {
		 printf("%f ",X[k][1]);
	 }
	 
	 printf("\n\n");
	 
	 return 0;
}