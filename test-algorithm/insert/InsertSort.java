import java.util.Arrays;

class InsertSort{
    public static void main(String[] args){
        int[] nums = {1,5,7,3,4,9,8,2,6};
        for(int i=1;i<nums.length;i++){
            int temp = nums[i]; //磨出来的数
            int j = i-1; //收留的数的下标
            while(j>=0 && nums[j]>temp){
                nums[j+1] = nums[j];
                j--;
            }
            nums[j+1]=temp;
    }
        System.out.println(Arrays.toString(nums));
    }

}
