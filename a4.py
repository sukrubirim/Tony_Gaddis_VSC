def create_number_file():
    import random
    file_name=input("Enter a file name: ")
    num_file=open(file_name,"w")
    for line in range(random.randint(1,10)):
        num_file.write(f"{random.randint(1,100)}\n")
    num_file.close()
    return file_name

def display_several_number_of_line(file_name):
    MAX_ORDER_LINE=5
    count=1
    num_file=open(file_name,"r")
    line=num_file.readline()
    while line!="" and count<=5:
        print(f"#{count} ",line,end="")
        count+=1
        line=num_file.readline()
    num_file.close()

def display_all_numbers():
    number_file=open("number_file.txt","r")
    num=number_file.readline()
    count=0
    while num!="":
        count+=1
        print(f"#{count} ",num,end="")
        num=number_file.readline()
    number_file.close
    
main()
def main():
    file_name=create_number_file()
    display_several_number_of_line(file_name)
    display_all_numbers()

main()