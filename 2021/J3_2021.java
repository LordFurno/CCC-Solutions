import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;
public class Main
{
	public static void main(String[] args)
    {
        ArrayList<String> directions=new ArrayList<String>();
        Scanner input=new Scanner(System.in);
        String in="";
        while(in.equals("99999")!=true){
        
            System.out.print("");
            in=input.nextLine();
            int sum=Integer.parseInt(in.charAt(0)+"")+Integer.parseInt(in.charAt(1)+"");
            if (in.equals("99999")){
                break;
            }
            if(sum%2==0 && sum!=0){
                directions.add("right");
                System.out.println("right "+in.charAt(2)+in.charAt(3)+in.charAt(4));
            }
            else if(sum%2!=0){
                directions.add("left");
                System.out.println("left "+in.charAt(2)+in.charAt(3)+in.charAt(4));
            }
            else if(sum==0){
                directions.add(directions.get(directions.size()-1));
                System.out.println(directions.get(directions.size()-1)+" "+in.charAt(2)+in.charAt(3)+in.charAt(4));
            }
        }
        input.close();
  
    }
}
