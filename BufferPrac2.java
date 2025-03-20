import java.io.*;
import java.util.*;

public class BufferPrac2 {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        ArrayList<Integer> num = new ArrayList<>();

        int n = Integer.parseInt(br.readLine());
            
        int arr1[] = new int[n];
        String[] input = br.readLine().split(" ");
        
        for(int i=0; i<n; i++){
            arr1[i] = Integer.parseInt(input[i]);
        }

        Arrays.sort(arr1);
        int maxValue = arr1[n-1];

        bw.write("가장 큰 수: "+ maxValue + "\n");
        bw.flush();
        
        br.close();
        bw.close();

    }
}
//5
//3 17 8 12 25
//가장 큰 수: 25