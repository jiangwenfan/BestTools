#include<stdio.h>
void frame(int l0,int w1);
void body(int l0,int w2);
void printfshow(int l,int w,char a[]);
int main(){
	int a,b,length0,wide0,wide1,wide2;
	printf("input face size:\n");
	printf("/teg: 10 20\n");
	scanf("%d %d",&a,&b);
	//big number is length;small number is wide; 
	if(a > b){
		length0 = a;
		wide0 = b;
	}else{
		length0 = b;
		wide0 = a;
	}
	wide1 = wide0*0.15; //inner wide is 25% one side
	wide2 = wide0 - 2*wide1; //body wide
	
	frame(length0,wide1);
	body(length0,wide2);
	frame(length0,wide1);
	return 0;
}

void frame(int l0,int w1){
	for(int i = 0;i < w1;i++){
		for(int j = 0;j < l0;j++){
			printf("\033[43;34m0\033[0m");
		}
		printf("\n");
	}
}
void body(int l0,int w2){
	int up,middle,down;
	up = w2*0.15;
	middle = w2*0.64;
	down = w2*0.21;

	char b[] = "#";
	printfshow(l0,w2,b);

	/*
	for(int i = 0;i < w2;i++){
		for(int j = 0;j < l0;j++){
			printf("\033[32m#\033[0m");
		}
		printf("\n");
	} */
}
void printfshow(int l,int w,char a[]){
	for(int i=0;i<w;i++){
		for(int j=0;j<l;j++){
			printf("%s",a);
		}
		printf("\n");
	}
}
