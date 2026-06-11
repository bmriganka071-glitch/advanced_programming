import java.util.*;

public class Main {
    public static void main(String[] args) {

        List<Student> students = new ArrayList<>();

        List<String> courses1 = Arrays.asList("Math", "DSA", "OS");
        Map<String, Integer> scores1 = new HashMap<>();
        scores1.put("Math", 90);
        scores1.put("DSA", 85);
        scores1.put("OS", 80);

        students.add(new Student(1, "Rahul", courses1, scores1));

        List<String> courses2 = Arrays.asList("Math", "DSA", "DBMS");
        Map<String, Integer> scores2 = new HashMap<>();
        scores2.put("Math", 95);
        scores2.put("DSA", 88);
        scores2.put("DBMS", 92);

        students.add(new Student(2, "Ankit", courses2, scores2));

        
        List<Student> topStudents = StudentAnalyzer.getTopNStudents(students, 1);
        System.out.println("Top Student: " + topStudents.get(0).getName());

        
        Map<String, Double> averages = StudentAnalyzer.getAverageScorePerCourse(students);
        System.out.println("Course Averages: " + averages);

        
        Set<String> uniqueCourses = StudentAnalyzer.getAllUniqueCourses(students);
        System.out.println("Unique Courses: " + uniqueCourses);
    }
}



// Time complexity :
// for calculating course average : O(n)
// Explanation: traversing the students takes O(n) time 
//              traversal of course of each student takes O(c) time
//              total time : O(n*c)
//              Timecomplexity : O(n)   
//sorting n students = O(nlogn)