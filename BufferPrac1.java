import java.io.*;
import java.util.*;

public class BufferPrac1 {
    public static void main(String [] args) throws IOException{
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

       String [] input = br.readLine().split(" ");
       int l = input.length;
       int[] numbers = new int[l];
       int sum = 0;

       for (int i=0; i<l; i++){
            numbers[i] = Integer.parseInt(input[i]);
            sum += numbers[i];
       }

       float avr = (float) sum/l;

       bw.write("입력된 숫자의 평균: "+avr+"\n");
       bw.flush();

       br.close();
       bw.close();

    }
}