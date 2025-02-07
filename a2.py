def main():
    import os
    found=False
    search=input("Enter the student name whose grade want you to change: ")
    student_file=open("students.txt","r")
    temp_file=open("temp.txt","w")
    s=student_file.readline()
    while s!="":
        temp_file.write(s)
        f=student_file.readline()
        if s.rstrip("\n")==search:
            temp_file.write(f"{float(input(f"Enter the new score for {s.rstrip("\n")} : "))}\n")
            found=True        
        else:
            temp_file.write(f)
        s=student_file.readline()
    student_file.close()
    temp_file.close()
    os.remove("students.txt")
    os.renames("temp.txt","students.txt")
    if found:
        print("The file has been updated.")
    else:
        print(f"There is no one in this file named {search}.")  
    display_highest_score()
    
def display_highest_score():
    student_file=open("students.txt","r")
    max_grade_name=""
    max_grade=0.0
    name=student_file.readline()
    while name!="":
        grade=student_file.readline()
        if float(grade.rstrip("\n"))>max_grade:
            max_grade_name=name.rstrip("\n")
            max_grade=float(grade.rstrip("\n"))
        name=student_file.readline()
    student_file.close()
    print("Highest grade & name: ",end=" ")
    print(max_grade,max_grade_name,sep=" & ")
    
main()