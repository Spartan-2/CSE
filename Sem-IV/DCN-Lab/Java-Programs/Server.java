import java.util.Scanner;
import java.io.*;
import java.net.*;


public class Server{
    public static void main(String[] args) throws Exception{

        ServerSocket sersock = new ServerSocket(4000);
        System.out.println("Server Waiting for Connection ");
        Socket soc = sersock.accept();
        System.out.println("Connection Established! Waiting for chatting ");
        InputStream istream = soc.getInputStream();
        BufferedReader fileread = new BufferedReader(new InputStreamReader(istream));

        String fname = fileread.readLine();
        OutputStream ostream = soc.getOutputStream();
        PrintWriter pwrite = new PrintWriter(ostream,true);
        String str;

        BufferedReader content = new BufferedReader(new FileReader(fname));
        while((str = content.readLine()) != null){
            pwrite.println(str);
        }
        sersock.close();
        soc.close();
        fileread.close();
        pwrite.close();
        content.close();


    }
}