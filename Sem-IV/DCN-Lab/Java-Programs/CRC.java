import java.util.*;
public class CRC {

    public static String xor(String a,String b){
        int len = Math.max(a.length(),b.length());
        int x = Integer.parseInt(a,2);
        int y = Integer.parseInt(b,2);
        String result = Integer.toBinaryString((x^y));
        result = String.format("%"+len+"s",result).replace(" ","0");
        return result;
    }

    public static String divide(String dividend,String divisor){
        int dlen = divisor.length();
        int dndlen = dividend.length();

        while(dndlen >= dlen){
            String temp;
            if(dividend.charAt(0) == '1'){
                temp = xor(divisor,dividend.substring(0,dlen));
            }else{
                temp = xor("0",dividend.substring(0,dlen));
            }
            dividend = temp.substring(1) + dividend.substring(dlen);
            dndlen -= 1;
        }
        return dividend;
    }

    public static String generate(String message,String generator){
        int msglen = message.length();
        int gtrlen = generator.length();

        String dividend = String.format("%-"+(msglen+gtrlen -1)+"s",message).replace(" ","0");
        String rem = divide(dividend,generator);

        return message+rem;
    }

    public static boolean checkCodeword(String gw, String codeword){
        String temp = divide(codeword,gw);
        return (Integer.parseInt(temp) == 0);

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Using CRC-CITT");
        String generator = "10000100001001";
        System.out.println("1.Generate Codeword\t2.Check Codeword\t3.Exit");
        int choice = sc.nextInt();

        switch(choice){
            case 1:
                System.out.println("Enter the message");
                String msg = sc.next();
                System.out.println("Codeword :"+generate(msg,generator));
                break;
            case 2:
                System.out.println("Enter the codeword");
                String code = sc.nextLine();
                if(checkCodeword(code,generator)){
                    System.out.println("No error");
                }else{
                    System.out.println("Error");
                }
        }
        sc.close();
    }
}
