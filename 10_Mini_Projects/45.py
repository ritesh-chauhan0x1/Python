"""
Mini Project: Student Records Management System
================================================
A CLI application to manage student records with CRUD operations.
Features: Add, View, Update, Delete, Search, Calculate Grades, Export
"""

import json
import os
from datetime import datetime

class Student:
    """Student class to represent individual student"""
    
    def __init__(self, student_id, name, age, grade_level, subjects=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade_level = grade_level
        self.subjects = subjects if subjects else {}
        self.enrollment_date = datetime.now().strftime("%Y-%m-%d")
    
    def add_subject(self, subject, marks):
        """Add or update subject marks"""
        if 0 <= marks <= 100:
            self.subjects[subject] = marks
            return True
        return False
    
    def calculate_average(self):
        """Calculate average marks"""
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)
    
    def get_grade(self):
        """Calculate overall grade based on average"""
        avg = self.calculate_average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"
    
    def to_dict(self):
        """Convert student object to dictionary"""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade_level": self.grade_level,
            "subjects": self.subjects,
            "enrollment_date": self.enrollment_date
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create student object from dictionary"""
        student = cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["grade_level"],
            data.get("subjects", {})
        )
        student.enrollment_date = data.get("enrollment_date", datetime.now().strftime("%Y-%m-%d"))
        return student

class StudentManagementSystem:
    """Student Management System Class"""
    
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}
        self.load_students()
    
    def load_students(self):
        """Load students from file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    for student_data in data:
                        student = Student.from_dict(student_data)
                        self.students[student.student_id] = student
                print(f"✅ Loaded {len(self.students)} student records")
            else:
                print("📝 Starting with empty database")
        except Exception as e:
            print(f"❌ Error loading students: {e}")
            self.students = {}
    
    def save_students(self):
        """Save students to file"""
        try:
            data = [student.to_dict() for student in self.students.values()]
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=2)
            print(f"💾 Saved {len(self.students)} student records")
        except Exception as e:
            print(f"❌ Error saving students: {e}")
    
    def add_student(self, student_id, name, age, grade_level):
        """Add a new student"""
        if student_id in self.students:
            print(f"\n❌ Student ID {student_id} already exists!")
            return False
        
        student = Student(student_id, name, age, grade_level)
        self.students[student_id] = student
        print(f"\n✅ Student added: {name} (ID: {student_id})")
        self.save_students()
        return True
    
    def view_student(self, student_id):
        """View individual student details"""
        if student_id not in self.students:
            print(f"\n❌ Student ID {student_id} not found!")
            return
        
        student = self.students[student_id]
        print("\n" + "="*60)
        print("              STUDENT DETAILS")
        print("="*60)
        print(f"Student ID:       {student.student_id}")
        print(f"Name:             {student.name}")
        print(f"Age:              {student.age}")
        print(f"Grade Level:      {student.grade_level}")
        print(f"Enrollment Date:  {student.enrollment_date}")
        print(f"\nSubjects & Marks:")
        if student.subjects:
            for subject, marks in student.subjects.items():
                print(f"  • {subject}: {marks}/100")
            print(f"\nAverage:          {student.calculate_average():.2f}%")
            print(f"Overall Grade:    {student.get_grade()}")
        else:
            print("  No subjects added yet")
        print("="*60)
    
    def view_all_students(self):
        """View all students"""
        if not self.students:
            print("\n📝 No students in the database!")
            return
        
        print("\n" + "="*90)
        print("                        ALL STUDENTS")
        print("="*90)
        print(f"{'ID':<10} {'Name':<25} {'Age':<5} {'Grade':<8} {'Subjects':<8} {'Average':<8} {'Grade':<6}")
        print("-"*90)
        
        for student in self.students.values():
            avg = student.calculate_average()
            grade = student.get_grade()
            subject_count = len(student.subjects)
            print(f"{student.student_id:<10} {student.name:<25} {student.age:<5} "
                  f"{student.grade_level:<8} {subject_count:<8} {avg:<8.2f} {grade:<6}")
        
        print("="*90)
        print(f"Total Students: {len(self.students)}")
        print("="*90)
    
    def update_student(self, student_id, name=None, age=None, grade_level=None):
        """Update student information"""
        if student_id not in self.students:
            print(f"\n❌ Student ID {student_id} not found!")
            return False
        
        student = self.students[student_id]
        if name:
            student.name = name
        if age:
            student.age = age
        if grade_level:
            student.grade_level = grade_level
        
        print(f"\n✅ Student {student_id} updated successfully!")
        self.save_students()
        return True
    
    def delete_student(self, student_id):
        """Delete a student"""
        if student_id not in self.students:
            print(f"\n❌ Student ID {student_id} not found!")
            return False
        
        student = self.students[student_id]
        del self.students[student_id]
        print(f"\n🗑️  Deleted student: {student.name} (ID: {student_id})")
        self.save_students()
        return True
    
    def add_marks(self, student_id, subject, marks):
        """Add or update subject marks for a student"""
        if student_id not in self.students:
            print(f"\n❌ Student ID {student_id} not found!")
            return False
        
        student = self.students[student_id]
        if student.add_subject(subject, marks):
            print(f"\n✅ Marks added: {subject} - {marks}/100 for {student.name}")
            self.save_students()
            return True
        else:
            print("\n❌ Invalid marks! Must be between 0 and 100")
            return False
    
    def search_students(self, keyword):
        """Search students by name"""
        results = [s for s in self.students.values() if keyword.lower() in s.name.lower()]
        
        if not results:
            print(f"\n🔍 No students found matching '{keyword}'")
            return
        
        print(f"\n🔍 Found {len(results)} student(s) matching '{keyword}':")
        print("-"*60)
        for student in results:
            print(f"ID: {student.student_id} | Name: {student.name} | "
                  f"Grade: {student.grade_level} | Average: {student.calculate_average():.2f}%")
    
    def get_statistics(self):
        """Display system statistics"""
        if not self.students:
            print("\n📊 No data available for statistics")
            return
        
        total_students = len(self.students)
        all_averages = [s.calculate_average() for s in self.students.values()]
        overall_avg = sum(all_averages) / len(all_averages) if all_averages else 0
        
        grade_distribution = {"A+": 0, "A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for student in self.students.values():
            grade = student.get_grade()
            grade_distribution[grade] += 1
        
        print("\n" + "="*60)
        print("              SYSTEM STATISTICS")
        print("="*60)
        print(f"Total Students:        {total_students}")
        print(f"Overall Average:       {overall_avg:.2f}%")
        print(f"Highest Average:       {max(all_averages):.2f}%" if all_averages else "N/A")
        print(f"Lowest Average:        {min(all_averages):.2f}%" if all_averages else "N/A")
        print(f"\nGrade Distribution:")
        for grade, count in grade_distribution.items():
            percentage = (count / total_students) * 100 if total_students > 0 else 0
            bar = "█" * int(percentage / 5)
            print(f"  {grade}:  {count:2d} students {bar} ({percentage:.1f}%)")
        print("="*60)

def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("      STUDENT RECORDS MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. View Student")
    print("3. View All Students")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add/Update Marks")
    print("7. Search Students")
    print("8. Statistics")
    print("0. Exit")
    print("="*50)

def main():
    """Main program function"""
    sms = StudentManagementSystem()
    
    print("\n🎓 Welcome to Student Records Management System!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-8): ").strip()
            
            if choice == '0':
                print("\n👋 Saving and exiting...")
                sms.save_students()
                print("Goodbye!")
                break
            
            elif choice == '1':  # Add Student
                student_id = input("\nEnter Student ID: ").strip()
                name = input("Enter Name: ").strip()
                age = int(input("Enter Age: "))
                grade_level = input("Enter Grade Level (e.g., 10th): ").strip()
                sms.add_student(student_id, name, age, grade_level)
            
            elif choice == '2':  # View Student
                student_id = input("\nEnter Student ID: ").strip()
                sms.view_student(student_id)
            
            elif choice == '3':  # View All
                sms.view_all_students()
            
            elif choice == '4':  # Update Student
                student_id = input("\nEnter Student ID to update: ").strip()
                if student_id in sms.students:
                    print("Leave blank to keep current value")
                    name = input("New Name: ").strip() or None
                    age_input = input("New Age: ").strip()
                    age = int(age_input) if age_input else None
                    grade_level = input("New Grade Level: ").strip() or None
                    sms.update_student(student_id, name, age, grade_level)
                else:
                    print(f"❌ Student ID {student_id} not found!")
            
            elif choice == '5':  # Delete Student
                student_id = input("\nEnter Student ID to delete: ").strip()
                confirm = input(f"Delete student {student_id}? (y/n): ")
                if confirm.lower() == 'y':
                    sms.delete_student(student_id)
            
            elif choice == '6':  # Add Marks
                student_id = input("\nEnter Student ID: ").strip()
                subject = input("Enter Subject Name: ").strip()
                marks = int(input("Enter Marks (0-100): "))
                sms.add_marks(student_id, subject, marks)
            
            elif choice == '7':  # Search
                keyword = input("\nEnter student name to search: ").strip()
                sms.search_students(keyword)
            
            elif choice == '8':  # Statistics
                sms.get_statistics()
            
            else:
                print("\n❌ Invalid choice! Please enter 0-8.")
        
        except ValueError as e:
            print(f"\n❌ Invalid input: {e}")
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted. Saving...")
            sms.save_students()
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()

"""
FEATURES IMPLEMENTED:
✅ Add new students with unique IDs
✅ View individual student details
✅ View all students in tabular format
✅ Update student information
✅ Delete students
✅ Add/update subject marks
✅ Automatic grade calculation (A+ to F)
✅ Search students by name
✅ System statistics and analytics
✅ Grade distribution visualization
✅ File persistence (JSON)
✅ Error handling throughout
✅ User-friendly CLI interface

ENHANCEMENT IDEAS:
1. Add attendance tracking
2. Generate report cards (PDF)
3. Add parent contact information
4. Implement fee management
5. Add class/section management
6. Create teacher portal
7. Add email notifications
8. Generate performance graphs
9. Implement database (SQLite)
10. Create web dashboard with Flask/Django
"""
