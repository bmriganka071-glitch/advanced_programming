import React, { useState } from "react";

function EnrollmentDashboard() {

  const [students, setStudents] = useState(new Map());

  const [name, setName] = useState("");
  const [gpa, setGpa] = useState("");
  const [selectedCourses, setSelectedCourses] = useState(new Set());
  const [filterCourse, setFilterCourse] = useState("");

  const courseList = ["DSA", "Math", "DBMS", "OS", "CN"];

  // Handle course selection
  const toggleCourse = (course) => {
    setSelectedCourses(prev => {
      const newSet = new Set(prev);
      if (newSet.has(course)) {
        newSet.delete(course);
      } else {
        newSet.add(course);
      }
      return newSet;
    });
  };

  // Add student
  const addStudent = () => {

    if (!name || !gpa) return;

    const student = {
      id: Date.now(),
      name: name,
      enrolledCourses: new Set(selectedCourses),
      gpa: parseFloat(gpa)
    };

    setStudents(prev => {
      const newMap = new Map(prev);
      newMap.set(student.id, student);
      return newMap;
    });

    // reset form
    setName("");
    setGpa("");
    setSelectedCourses(new Set());
  };

  // Remove student
  const removeStudent = (id) => {
    setStudents(prev => {
      const newMap = new Map(prev);
      newMap.delete(id);
      return newMap;
    });
  };

  const studentArray = [...students.values()];

  // Sort by GPA
  const sortedStudents = [...studentArray].sort((a, b) => b.gpa - a.gpa);

  // Filter students
  const filteredStudents = sortedStudents.filter(student =>
    filterCourse === "" ? true : student.enrolledCourses.has(filterCourse)
  );

  // Unique courses
  const allCourses = studentArray.reduce((set, student) => {
    student.enrolledCourses.forEach(course => set.add(course));
    return set;
  }, new Set());

  const uniqueCoursesArray = [...allCourses];

  return (
    <div style={{ padding: "20px" }}>

      <h2>Course Enrollment Dashboard</h2>

      <h3>Add Student</h3>

      <input
        placeholder="Student Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <input
        type="number"
        placeholder="GPA"
        value={gpa}
        onChange={(e) => setGpa(e.target.value)}
      />

      <h4>Select Courses</h4>

      {courseList.map(course => (
        <div key={course}>
          <label>
            <input
              type="checkbox"
              checked={selectedCourses.has(course)}
              onChange={() => toggleCourse(course)}
            />
            {course}
          </label>
        </div>
      ))}

      <br />

      <button onClick={addStudent}>
        Add Student
      </button>

      <h3>Filter by Course</h3>

      <input
        placeholder="Course name"
        value={filterCourse}
        onChange={(e) => setFilterCourse(e.target.value)}
      />

      <h3>Unique Courses</h3>

      <ul>
        {uniqueCoursesArray.map(course => (
          <li key={course}>{course}</li>
        ))}
      </ul>

      <h3>Students (Sorted by GPA)</h3>

      <ul>
        {filteredStudents.map(student => (
          <li key={student.id}>
            {student.name} | GPA: {student.gpa} | Courses: {[...student.enrolledCourses].join(", ")}
            <button onClick={() => removeStudent(student.id)}>
              Remove
            </button>
          </li>
        ))}
      </ul>

    </div>
  );
}

export default EnrollmentDashboard;

// time complexity for filtering students : O(n)
