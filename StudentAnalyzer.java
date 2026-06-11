import java.util.*;
import java.util.stream.Collectors;

public class StudentAnalyzer {

    
    public static List<Student> getTopNStudents(List<Student> students, int n) {

        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getAverageScore).reversed())
                .limit(n)
                .collect(Collectors.toList());
    }

   
    public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {

        Map<String, Double> courseAverages = new HashMap<>();

        Set<String> allCourses = getAllUniqueCourses(students);

        for (String course : allCourses) {
            double avg = students.stream()
                    .mapToInt(student -> student.getScores().getOrDefault(course, 0))
                    .average()
                    .orElse(0.0);

            courseAverages.put(course, avg);
        }

        return courseAverages;
    }

   
    public static Set<String> getAllUniqueCourses(List<Student> students) {

        return students.stream()
                .flatMap(student -> student.getCourses().stream())
                .collect(Collectors.toCollection(HashSet::new));
    }
}
