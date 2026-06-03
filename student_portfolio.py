total_students = 0
total_scholarship_students = 0


def parent_notification():
    pass


def process_student(full_name: str,age: int,jamb_score: int,school_name="Lagos Secondary School",*test_scores,**other_details):
    first_name = full_name.strip().split(" ")[0]
    last_name = full_name.strip().split(" ")[1]

    swapped_first_name , swapped_last_name = last_name, first_name

    scores_count = len(test_scores)
    total_score = 0
    for scores in test_scores:
        total_score += scores 
    
    average = total_score

    average /= scores_count

    overall_performance_score = ((jamb_score / 4) + average) / 2

    initials = f"{first_name[0].upper()}{last_name[0].upper()}"

    academic_level = ""

    if overall_performance_score >= 85:
        academic_level = "Genius"
    elif 75 <= overall_performance_score <= 84:
        academic_level = "Excellent" 
    elif 60 <= overall_performance_score <= 74:
        academic_level = "Good" 
    elif 45 <= overall_performance_score <= 59:
        academic_level = "Average" 
    else:
        academic_level = "Needs Improvement"

    scholarship_status = ""

    global total_scholarship_students

    if jamb_score >= 320 and average >= 80:
        scholarship_status = "Full Scholarship"
        total_scholarship_students += 1
    elif jamb_score >= 280 and average >= 70:
        scholarship_status = "Partial Scholarship"
        total_scholarship_students += 1
    else:
        scholarship_status = "No Scholarship"

    parent_notification()

    age_category = "Adult" if age > 19 else "Child" if age < 13 else "Teenager" 

    global total_students 
    total_students += 1

    print(f"Student {total_students}\n")
    print(f"Original Name: {full_name}\n")
    print(f"Swapped Name : {swapped_last_name} {swapped_first_name}\n")
    print(f"Initials     : {initials}\n")
    print(f"Age          : {age} ({age_category})\n")
    print(f"School       : {school_name}\n")
    print(f"JAMB Score   : {jamb_score}\n")
    print("Test Scores  : \n")
    for i , test_score in enumerate(test_scores):
        subject_name = "Maths"
        if i == 1:
            subject_name = "English"
        elif i == 2:
            subject_name = "Physics"
        print(f"\t{i + 1} {subject_name} - {test_score}\n")

    print(f"Average      : {average}\n")
    print(f"Overall Score: {overall_performance_score}\n")
    print(f"Academic Level: {academic_level}\n")
    print(f"Scholarship  : {scholarship_status}\n\n")
        

print("=== STUDENT ACADEMIC PORTFOLIO SYSTEM ===\n\n")
for i in range(1,5):
    process_student("Ade Ola",22,300,"CLH",90,80,89)


print(f"Total Students Processed : {total_students}\n")
print(f"Students with Scholarship: {total_scholarship_students}")


        




    
