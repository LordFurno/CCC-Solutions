import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;
public class Main
{
	public static void main(String[] args)
    {
        Scanner input=new Scanner(System.in);
        System.out.print("");
        int bids=input.nextInt();
        ArrayList<Integer> values= new ArrayList<Integer>();
        ArrayList<String> names=new ArrayList<String>();
        input.nextLine();
        for(int i=1;i<(bids*2)+1;i++){
            if(i%2==0){
                System.out.print("");
                int temp=input.nextInt();
                values.add(temp);
                input.nextLine();
            }
            else{
                System.out.print("");
                String name=input.nextLine();
                names.add(name);
            }
        }
        System.out.println(names.get(values.indexOf(Collections.max(values))));
        input.close();
  
    }
}
