//Reverse string using two pointers 
public class ReverseString {
    static void printReverse(char[] s){
       int pointer1 = 0;
       int pointer2 = s.length - 1;

       while(pointer1 < pointer2){
        char tmp = s[pointer1];
        s[pointer1] = s[pointer2];
        s[pointer2] = tmp;

        pointer1++;
        pointer2--;

       }
       System.out.println(s);
}
//Reverse string using two pointers and for loop
static void printReverseString(char[] s){
    for(int i = 0, j = s.length - 1; i < s.length/2; i++, j--){
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;

    }
    System.out.println(s);
}
    public static void main(String[] args) {
        char[] s = {'H', 'e', 'l', 'l', 'o'};
        char[] t = {'H', 'e', 'l', 'l', 'o'};
 
        printReverse(s);
        printReverseString(t);
    }
}
