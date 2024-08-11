import java.util.Scanner;

public class TDM{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of Stations (max 10)");
        int n = sc.nextInt();
        int[] pt = new int[n];
        int[] rem_pt = new int[n];
        int[] wt = new int[n];
        int[] tat = new int[n];
        int awt=0, atat=0;

        System.out.println("Enter the processing time for all Stations ");
        for (int i=0;i<n;i++){
            int t = sc.nextInt();
            pt[i] = t;
            rem_pt[i] = pt[i];
        }

        System.out.println("Enter the size of frame ");
        int qt = sc.nextInt();

        int count=0,sq = 0;

        while(true){

            for(int i=0;i<n;i++){
                if(rem_pt[i] == 0){
                    count++;
                    continue;
                }

                int temp = qt;
                if(rem_pt[i] > qt){
                    rem_pt[i] -= qt;

                }else{
                    temp = rem_pt[i];
                    rem_pt[i] = 0;
                }
                sq += temp;
                tat[i] = sq;
            }
            if(count == n){
                break;
            }
            count = 0;
        }

        System.out.println("-------------------------------------------------------");
        System.out.println("Station  Processing Time  Completion Time  Waiting Time");
        System.out.println("-------------------------------------------------------");
        for (int i=0;i<n;i++){

            wt[i] = tat[i] - pt[i];
            awt += wt[i];
            atat += tat[i]; 
            System.out.println(i+1+"\t\t"+pt[i]+"\t\t"+tat[i]+"\t\t"+wt[i]);
        }
        System.out.println("The Average Waiting Time is "+(awt/n));
        System.out.println("The average Turn around Time is "+(atat/n));

        sc.close();
    }
}