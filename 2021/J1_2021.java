import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;
public class Main
{
	public static void main(String[] args)
    {
        Scanner input=new Scanner(System.in);
        System.out.print("");
        int b=input.nextInt();
        int value=(b*5)-400;
        System.out.println(value);
        if(value>100){
            System.out.println(-1);
        }
        else if(value<100){
            System.out.println(1);
        }
        else{
            System.out.println(0);
        }
        input.close();
  
    }
}
