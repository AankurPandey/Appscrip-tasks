                                //task 9

// program to reverse the array in java
public class RemoveArray{ 

//this is the method toreverse the passed array 
public static int reverseTheArray(int arr[], int n){ 
        int temp=0;//temp is a variable used for storing between values
        int iterate=int(n/2);
        n=n-1;
        for( int index =0;index<iterate;index++,n--){
            temp=arr[index];
            arr[index]=arr[n];
            arr[n]=temp;
        }
        return arr
    }  
       //main method defines that the execution of program will start from here 
    public static void main (String[] args) {  
        int arr[] = {10,20,30,40,50};  
        int length = arr.length;  
        int rever[] = removeDuplicateElements(arr, length);  //function call statement
        
        //printing array elements  
        for (int i=0; i<length; i++)  
           System.out.print(arr[i]+" ");  
    }  
} 
