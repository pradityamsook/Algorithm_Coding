using System;
					
public class Program
{
	#pragma warning disable
	public static int Tribonacci(int n) {
        /*
        Answer <= 2^31 - 1; that's mean the length of array limit at 41.
        Because a parameter is Integer(in C# is Int32). 
        */
        int[] arr = new int[41];
		int answer = 0;
        
        if (n == 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 1;
        if (arr.Length > 38) {
            return 0;
        }
		for (int i = 0; i < n + 1; i++) {
			if (i == 0 || i== 1 || i == 2) {
				arr[0] = 0;
				arr[1] = 1;
				arr[2] = 1;
			} 
			arr[i + 3] = arr[i] + arr[i + 1] + arr[i + 2]; 
			answer = arr[i];
			//Console.WriteLine("+++");
			//Console.WriteLine(answer);
		
		}
		return answer;  
    }
		
	public static void Main()
	{
		int answer = Tribonacci(4);
	}
}