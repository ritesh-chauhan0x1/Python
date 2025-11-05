"""
Mini Project: CLI To-Do List Manager
=====================================
A command-line to-do list application with file persistence.
Features: Add, View, Complete, Delete, Save/Load tasks
"""

import json
import os
from datetime import datetime

class TodoList:
    """To-Do List Manager Class"""
    
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = []
        self.load_todos()
    
    def load_todos(self):
        """Load todos from file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    self.todos = json.load(file)
                print(f"✅ Loaded {len(self.todos)} tasks from {self.filename}")
            else:
                print("📝 Starting with empty to-do list")
        except Exception as e:
            print(f"❌ Error loading todos: {e}")
            self.todos = []
    
    def save_todos(self):
        """Save todos to file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.todos, file, indent=2)
            print(f"💾 Saved {len(self.todos)} tasks to {self.filename}")
        except Exception as e:
            print(f"❌ Error saving todos: {e}")
    
    def add_todo(self, task, priority="Medium"):
        """Add a new todo"""
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "priority": priority,
            "completed": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.todos.append(todo)
        print(f"\n✅ Task added: '{task}' (Priority: {priority})")
        self.save_todos()
    
    def view_todos(self, show_completed=True):
        """Display all todos"""
        if not self.todos:
            print("\n📝 No tasks in your to-do list!")
            return
        
        print("\n" + "="*70)
        print("                    MY TO-DO LIST")
        print("="*70)
        
        active_tasks = []
        completed_tasks = []
        
        for todo in self.todos:
            if todo["completed"]:
                completed_tasks.append(todo)
            else:
                active_tasks.append(todo)
        
        if active_tasks:
            print("\n📌 ACTIVE TASKS:")
            print("-" * 70)
            for todo in active_tasks:
                priority_emoji = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
                emoji = priority_emoji.get(todo["priority"], "⚪")
                print(f"{todo['id']}. {emoji} [{todo['priority']}] {todo['task']}")
                print(f"   Created: {todo['created']}")
        
        if completed_tasks and show_completed:
            print("\n✅ COMPLETED TASKS:")
            print("-" * 70)
            for todo in completed_tasks:
                print(f"{todo['id']}. ✓ {todo['task']}")
        
        print("="*70)
        print(f"Total: {len(active_tasks)} active, {len(completed_tasks)} completed")
        print("="*70)
    
    def complete_todo(self, task_id):
        """Mark a todo as completed"""
        for todo in self.todos:
            if todo["id"] == task_id:
                if todo["completed"]:
                    print(f"\n⚠️  Task {task_id} is already completed!")
                else:
                    todo["completed"] = True
                    print(f"\n✅ Task {task_id} marked as completed: '{todo['task']}'")
                    self.save_todos()
                return
        print(f"\n❌ Task {task_id} not found!")
    
    def delete_todo(self, task_id):
        """Delete a todo"""
        for i, todo in enumerate(self.todos):
            if todo["id"] == task_id:
                deleted_task = self.todos.pop(i)
                print(f"\n🗑️  Deleted task: '{deleted_task['task']}'")
                self.save_todos()
                return
        print(f"\n❌ Task {task_id} not found!")
    
    def search_todos(self, keyword):
        """Search todos by keyword"""
        results = [t for t in self.todos if keyword.lower() in t["task"].lower()]
        
        if not results:
            print(f"\n🔍 No tasks found containing '{keyword}'")
            return
        
        print(f"\n🔍 Found {len(results)} task(s) containing '{keyword}':")
        print("-" * 70)
        for todo in results:
            status = "✓" if todo["completed"] else "○"
            print(f"{status} {todo['id']}. {todo['task']} [{todo['priority']}]")
    
    def clear_completed(self):
        """Remove all completed tasks"""
        completed_count = len([t for t in self.todos if t["completed"]])
        self.todos = [t for t in self.todos if not t["completed"]]
        print(f"\n🗑️  Cleared {completed_count} completed task(s)")
        self.save_todos()
    
    def get_statistics(self):
        """Show task statistics"""
        total = len(self.todos)
        completed = len([t for t in self.todos if t["completed"]])
        active = total - completed
        
        priority_counts = {"High": 0, "Medium": 0, "Low": 0}
        for todo in self.todos:
            if not todo["completed"] and todo["priority"] in priority_counts:
                priority_counts[todo["priority"]] += 1
        
        print("\n" + "="*50)
        print("           TASK STATISTICS")
        print("="*50)
        print(f"Total Tasks:      {total}")
        print(f"Active Tasks:     {active}")
        print(f"Completed Tasks:  {completed}")
        if total > 0:
            print(f"Completion Rate:  {(completed/total)*100:.1f}%")
        print(f"\nPriority Breakdown (Active):")
        print(f"  🔴 High:    {priority_counts['High']}")
        print(f"  🟡 Medium:  {priority_counts['Medium']}")
        print(f"  🟢 Low:     {priority_counts['Low']}")
        print("="*50)

def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("          TO-DO LIST MANAGER")
    print("="*50)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Tasks")
    print("6. Clear Completed Tasks")
    print("7. Statistics")
    print("0. Exit")
    print("="*50)

def main():
    """Main program function"""
    todo_list = TodoList()
    
    print("\n🎉 Welcome to To-Do List Manager!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-7): ").strip()
            
            if choice == '0':
                print("\n👋 Saving and exiting...")
                todo_list.save_todos()
                print("Goodbye!")
                break
            
            elif choice == '1':  # Add Task
                task = input("\nEnter task description: ").strip()
                if not task:
                    print("❌ Task cannot be empty!")
                    continue
                print("\nPriority: 1. High  2. Medium  3. Low")
                priority_choice = input("Select priority (default: Medium): ").strip()
                priority_map = {"1": "High", "2": "Medium", "3": "Low"}
                priority = priority_map.get(priority_choice, "Medium")
                todo_list.add_todo(task, priority)
            
            elif choice == '2':  # View Tasks
                todo_list.view_todos()
            
            elif choice == '3':  # Complete Task
                todo_list.view_todos(show_completed=False)
                try:
                    task_id = int(input("\nEnter task ID to mark as completed: "))
                    todo_list.complete_todo(task_id)
                except ValueError:
                    print("❌ Invalid task ID!")
            
            elif choice == '4':  # Delete Task
                todo_list.view_todos()
                try:
                    task_id = int(input("\nEnter task ID to delete: "))
                    confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ")
                    if confirm.lower() == 'y':
                        todo_list.delete_todo(task_id)
                except ValueError:
                    print("❌ Invalid task ID!")
            
            elif choice == '5':  # Search
                keyword = input("\nEnter search keyword: ").strip()
                todo_list.search_todos(keyword)
            
            elif choice == '6':  # Clear Completed
                confirm = input("Clear all completed tasks? (y/n): ")
                if confirm.lower() == 'y':
                    todo_list.clear_completed()
            
            elif choice == '7':  # Statistics
                todo_list.get_statistics()
            
            else:
                print("\n❌ Invalid choice! Please enter 0-7.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted. Saving...")
            todo_list.save_todos()
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()

"""
FEATURES IMPLEMENTED:
✅ Add tasks with priority levels
✅ View all tasks (active and completed)
✅ Mark tasks as completed
✅ Delete tasks
✅ Search tasks by keyword
✅ Clear completed tasks
✅ Task statistics and analytics
✅ File persistence (JSON)
✅ Error handling
✅ User-friendly interface with emojis

ENHANCEMENT IDEAS:
1. Add due dates and reminders
2. Add categories/tags for tasks
3. Implement task editing
4. Add recurring tasks
5. Export to CSV or Excel
6. Add subtasks
7. Implement task sorting options
8. Add calendar view
9. Create web interface with Flask
10. Add user authentication for multiple users
"""
