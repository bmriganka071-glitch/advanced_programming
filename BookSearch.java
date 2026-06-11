import java.util.ArrayList;
import java.util.Scanner;
  
 class BookSearch{
  
  public static void main(String[]args){
    ArrayList<String>bookTitles=new ArrayList<>();
    bookTitles.add("Wings Of Fire");
  
    bookTitles.add("A Song Of Ice And Fire");

    bookTitles.add("The Theory Of Everything");
 
    bookTitles.add("A Brief History Of Time");
    
    bookTitles.add("Pride And Prejudice");

    Scanner scanner=new Scanner(System.in);
    System.out.println("Enter a word to search:");
    String searchWord=scanner.nextLine();

    System.out.println("Books containing'"+searchWord+"':");
    for(String title:bookTitles){
        if(title.toLowerCase().contains(searchWord.toLowerCase())){
          System.out.println(title);
    }
  }
}
 }