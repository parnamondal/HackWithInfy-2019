import java.io.*;
import java.util.Scanner;
import java.util.*; 

public class Solution {
    static void hello(char str[],int n){ 
        int s=(int)(str[0]); int co=1;
        for (int i=1;i<n;i++) {
            int x =(int)(str[i]);
            if (x==s){
            s=x;}
            else{
co++;
s=x;}
        }
        System.out.println(co);
        
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
         
          int n = in.nextInt();
          char[] str = new char[n];
String s = in.next(); s=s.toUpperCase();
for (int i =0;i<n;i++){
      str[i] = s.charAt(i);}
hello(str,n);

      
    }//main method
}//main class
/* OUTPUT :
 * 5
RRBBR
3
3
rbb
2

 */