import java.util.Scanner;

class Star{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("please input your birthday month: ");
		int month = sc.nextInt();
		System.out.println("please input your birthday day: ");
		int day = sc.nextInt();
		
		String[] star = {"test..","魔蝎-水瓶","水瓶-双鱼","双鱼-白羊","白羊-金牛","金牛-双子","双子-巨蟹","巨蟹-狮子","狮子-处女","处女-天秤","天秤-天蝎","天蝎-射手","射手-魔蝎"};
		
		int[] line = {0,19,18,20,19,20,20,22,22,22,22,21,21};
		//System.out.println("array test:"+star.length);
		String mon = star[month];
		int line_num = line[month];

		String[] temporary;
		String delimeter = "-";
		temporary = mon.split(delimeter);
		
		if (day > line_num) {
			//System.out.println("last:"+mon);
			System.out.println("\n你的星座是："+temporary[1]+" 座\n");
		}else{
			//System.out.println("home:"+mon);
			System.out.println("\n你的星座是: "+temporary[0]+" 座\n");
		}
		
	
}
}
