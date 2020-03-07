import java.util.Scanner;
import java.io.*;
class candy
{ static final int MOD_DIVISOR = 1_000_000_007;
	/* Returns true if the there is a subarray of arr[] with a sum equal to 
	'sum' otherwise returns false. Also, prints the result */
	static int  candies(int arr[], int n) 
	{ int l = arr[n-1];
	    int c=l;
	    for (int  i=n-2;i>=0;i--){
	       int x= Math.min(l-1,arr[i]);
	       if (x>=0)
	       c+=x;
	       l =x;
	       }
		
		

		System.out.println(c); 
		return 1; 
	} 

	public static void main(String[] args) 
	{ Scanner ob = new Scanner (System.in);
	    int t = ob.nextInt();
        for (int j=0;j<t;j++)
{       int n = ob.nextInt();
   
    int[] arr=new int[n];
for(int i=0;i<n;i++){
 arr[i]=ob.nextInt();}
    candies(arr,n);
	} 
	ob.close();
	    
	}
} 
/* OUTPUT :
 * 2
3
3 4 12
19
4
8 4 5 9
21

 */

