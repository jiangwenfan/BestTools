import java.util.Arrays;
class BubbleSort{

    public static void main(String[] args){
    int[] num = {9,2,3,1,5,7,4,6,8};
    System.out.println("inital-----------:"+Arrays.toString(num));
    
    for(int i=0;i<num.length-1;i++){
        for(int j=0;j<num.length-1-i;j++){
            int temp;
            if(num[j]>num[j+1]){
                temp = num[j+1];
                num[j+1] = num[j];
                num[j] = temp;
            }
        }
        System.out.println(Arrays.toString(num));
    }
    System.out.println("res---------"+Arrays.toString(num));
}
}
