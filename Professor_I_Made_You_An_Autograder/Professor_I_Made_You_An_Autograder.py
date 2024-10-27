
import random

def main():
    # Prompt for first and last name
    first_name = input("Enter student's first name: ").strip()
    last_name = input("Enter student's last name: ").strip()
    
    # Check if the student's name is "Jeremy Coleman"
    if first_name.lower() == "jeremy" and last_name.lower() == "coleman":
        grade = random.randint(95, 100)
    else:
        grade = random.randint(70, 94)
    
    # Print the assigned grade
    print(f"The assigned grade for {first_name} {last_name} is: {grade}")

if __name__ == "__main__":
    main()
