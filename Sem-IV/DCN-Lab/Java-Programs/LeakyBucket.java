import java.util.Scanner;
public class LeakyBucket {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Bucket size and rate ");
        int buc_cap = sc.nextInt();
        int rate = sc.nextInt();

        System.out.println("Enter the number of packets ");
        int n = sc.nextInt();
        int[] pac = new int[n];
        System.out.println("Enter the size of packets ");
        for (int i=0;i<n;i++){
            pac[i] = sc.nextInt();
        }

        int buc_rem = 0,recieved = 0,sent =0;   
        System.out.println("Clock  Packet size  Recieved  sent  Remaining ");
        for(int i=0;i<n;i++){

            if(pac[i] >0){
                if(buc_rem + pac[i] < buc_cap){
                    recieved = pac[i];
                    buc_rem += pac[i];
                }else{
                    recieved = -1;
                }
            }else{
                recieved = 0;
            }

            if(buc_rem > rate){
                sent = rate;
                buc_rem -= rate;
            }else{
                sent = buc_rem;
                buc_rem = 0;
            }
            if(recieved == -1){
                System.out.println((i+1)+"\t"+pac[i]+"\tDropped"+"\t"+sent+"\t"+buc_rem);

            }else{
                System.out.println((i+1)+"\t"+pac[i]+"\t"+recieved+sent+"\t"+buc_rem);
            }

        }
        sc.close();
    }    
}
