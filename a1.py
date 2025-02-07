def create_student_file():
    import random
    file_name=input("Enter the file name: ")
    student_file=open(file_name,"w")
    num_of_students=int(input("Enter the number of students: "))
    for i in range(num_of_students):
        student_file.write(f"{input("Enter the student name: ")}\n")
        student_file.write(f"{float(random.randrange(0,100))}\n")
    student_file.close()
    return file_name

def delete_student(file_name):
    import os
    student_file=open(file_name,"r")
    temp_file=open("temp_file.txt","w")
    search=input("Enter the name of the student you want to delete: ")
    name=student_file.readline()
    found=False
    while name!="":
        final_grade=student_file.readline()
        name=name.rstrip("\n")
        final_grade=final_grade.rstrip("\n")
        if search!=name:
            temp_file.write(f"{name}\n")
            temp_file.write(f"{final_grade}\n")
        else:
            found=True
        name=student_file.readline()
    student_file.close()
    temp_file.close()
    os.remove(file_name)
    os.rename("temp_file.txt",file_name)
    if found:
        print("The file has been updated.")
    else:
        print(f"There is no student named {search} in the file.")
        
def main():
    file_name=create_student_file()
    delete_student(file_name)

main()