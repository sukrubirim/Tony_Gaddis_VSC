def create_a_number_list():
    upper_range=int(input("Enter the upper range of list 1-? "))
    num_list=[]
    for i in range(1,upper_range+1):
        num_list.append(i)
    return num_list

def accumulator_for_file(num_list):
    total=0
    file_name=input("Enter the file name: ")
    num_file=open(file_name,"w")
    for number in num_list:
        num_file.write(f"{number}\n")
        total+=number
    num_file.close()
    return total,file_name 

def main():
    num_list=create_a_number_list()
    total,file_name=accumulator_for_file(num_list)
    print(f"Total value in {file_name.rstrip(".txt")} file : {total}")

main()