import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;
public class Main
{
	public static void main(String[] args)
    {
        Scanner input=new Scanner(System.in);

        System.out.print("");//M
        int m=input.nextInt();

        System.out.print("");//N
        int n=input.nextInt();

        System.out.print("");//K
        int k=input.nextInt();
        input.nextLine();//Because I take string input after int

        ArrayList<String []> commands=new ArrayList<String[]>();
        for(int i=0;i<k;i++){
            System.out.print("");//Commnad
            String temp=input.nextLine();

            String[] test=temp.split(" ",2);
            commands.add(test);

        }

        ArrayList<String[]> canvas = new ArrayList<String[]>();
        for(int i=0;i<m;i++){
            String[] temp = new String[n];
            for(int a=0;a<n;a++){
                temp[a]="B";
            }
            canvas.add(temp);
        }
        for(String[] list:commands){//Applies the commands
            if(list[0].equals("R")){
                String[] temporary= new String[n];
                int rowNumber=Integer.parseInt(list[1])-1;//Subtract 1 because index starts at 0
                String[] row=canvas.get(rowNumber);
                for(int a=0;a<n;a++){
                    if(row[a].equals("B")){
                        temporary[a]="G";
                    }
                    else if(row[a].equals("G")){
                        temporary[a]="B";
                    }
                }
                canvas.set(rowNumber,temporary);
            }
            else if(list[0].equals("C")){
                int column=Integer.parseInt(list[1])-1;
                for(int c=0;c<canvas.size();c++){
                    String [] temporary2=canvas.get(c);
                    if(temporary2[column].equals("B")){
                        temporary2[column]="G";
                    }
                    else if(temporary2[column].equals("G")){
                        temporary2[column]="B";
                    }
                    canvas.set(c,temporary2);
                }
    
            }
        }
        int count=0;
        for(String[] testing:canvas){
            for(String elements:testing){
                if(elements.equals("G")){
                    count++;
                }
            }
        }
        System.out.println(count);
        input.close();
  
    }
}
