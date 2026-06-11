import java.util.*;

public class Student {
    private int id ;
    private String name ;
    private List<String> courses ;                 
    private Map<String, Integer> scores ;          

    public Student (int id, String name, List<String> courses, Map<String, Integer> scores) {
        this.id = id ;
        this.name = name ;
        this.courses = new ArrayList<>(courses);
        this.scores = new HashMap<>(scores);
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public List<String> getCourses() {
        return courses;
    }

    public Map<String, Integer> getScores() {
        return scores;
    }


    public double getAverageScore() {
        if (courses.isEmpty()) return 0.0;

        int total = courses.stream()
                .mapToInt(course -> scores.getOrDefault(course, 0)) // handle missing scores
                .sum();

        return (double) total / courses.size();
    }
};
