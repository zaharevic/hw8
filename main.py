from os import path
all_data = []
last_id = 0
file_base = "base.txt"
temp_file = "temp.txt"

if not path.exists(file_base):
    with open(file_base,"w", encoding="utf-8") as f:
        pass

def read_records():
    global all_data, last_id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
        return []

def show_all():
    if all_data:
        print(*all_data, sep= "\n")
    else:
        print("Empty data! \n")

def add_new_record():
    global last_id

    array = ["surname", "name", "patronymic", "phone number"]
    string = ""

    for i in array:
        string += input(f"Enter {i}: ") + " "
    last_id += 1
    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string} \n")

def search_by_name():
    records = read_records()
    count = 0
    name = input("Enter name: ")
    if name.isalpha():
        for i in range(0,len(records)):
            person = records[i].split()
            if person[2] == name:
                if count == 0:
                    print("List: ")
                print(f"{records[i]} \n")
                count += 1
        if count == 0:
            print("There is no such record")
    else:
        print("invalid name")

def search_by_surename():
    records = read_records()
    count = 0
    surename = input("Enter surename: ")
    if surename.isalpha():
        for i in range(0, len(records)):
            person = records[i].split()
            if person[1] == surename:
                if count == 0:
                    print("List: ")
                print(f"{records[i]} \n")
                count += 1
        if count == 0:
            print("There is no such record")
    else:
        print("invalid surename")

def search_by_patronymic():
    records = read_records()
    count = 0
    patronymic = input("Enter patronymic: ")
    if patronymic.isalpha():
        for i in range(0, len(records)):
            person = records[i].split()
            if person[3] == patronymic:
                if count == 0:
                    print("List: ")
                print(f"{records[i]} \n")
                count += 1
        if count == 0:
            print("There is no such record")
    else:
        print("invalid patronymic")

def search_by_number():
    records = read_records()
    count = 0
    number = input("Enter phone number: ")
    if number.isdigit():
        for i in range(0, len(records)):
            person = records[i].split()
            if person[4] == number:
                if count == 0:
                    print("List: ")
                print(f"{records[i]} \n")
                count += 1
        if count == 0:
            print("There is no such record")
    else:
        print("invalid phone number")

def search_by_ID():
    records = read_records()
    count = 0
    ID = input("Enter phone ID: ")
    if ID.isdigit():
        for i in range(0, len(records)):
            person = records[i].split()
            if person[0] == ID:
                if count == 0:
                    print("List: ")
                print(f"{records[i]} \n")
                count += 1
        if count == 0:
            print("There is no such record")
    else:
        print("invalid phone ID")

def search_record_menu():
    flag = True
    while(flag):
        reply = input("Search menu: \n"
                      "1. Search by name\n"
                      "2. Search by surename\n"
                      "3. Search by patronymic\n"
                      "4. Search by phone number\n"
                      "5. Search by ID\n"
                      "5. Back\n")
        match reply:
            case "1":
                search_by_name()
            case "2":
                search_by_surename()
            case "3":
                search_by_patronymic()
            case "4":
                search_by_number()
            case "5":
                search_by_ID()
            case "6":
                flag = False

def change_record():
    array = ["surname", "name", "patronymic", "phone number"]
    string= ""
    records = read_records()
    print("list: ")
    for i in range(0,len(records)):
        print(f"{records[i]} ")
    id = input("Enter the id of the record you want to change: ")
    with open(temp_file,"w+",encoding="utf-8") as t:
        for i in range(0,len(records)):
            person = records[i].split()
            if person[0] == id:
                for j in array:
                    string += input(f"Enter {j}: ") + " "
                t.write(f"{i+1} {string} \n")
            else:
                t.write(f"{records[i]} \n")
    with open(temp_file, encoding="utf-8") as t1:
        with open(file_base, "w+", encoding="utf-8") as f:
            for line in t1:
                f.write(line)

def delete_record():
    global last_id

    records = read_records()
    print("list: ")
    for i in range(0, len(records)):
        print(f"{records[i]} ")
    id = input("Enter the id of the record you want to delete: ")
    with open(temp_file,"w+",encoding="utf-8") as t:
        for i in range(0,len(records)):
            person = records[i].split()
            if person[0] != id:
                if int(person[0]) < int(id):
                    t.write(f"{records[i]} \n")
                elif int(person[0]) > int(id):
                    t.write(f"{int(person[0]) -1} {person[1]} {person[2]} {person[3]} {person[4]}")
    last_id -= 1
    with open(temp_file, encoding="utf-8") as t1:
        with open(file_base, "w+", encoding="utf-8") as f:
            for line in t1:
                f.write(line)

def main_menu():
    play = True
    while(play):
        read_records()
        answer = input("Phone book: \n"
                        "1. Show all records\n"
                        "2. Add record\n"
                        "3. Search a record \n"
                        "4. Change record\n"
                        "5. Delete record\n"
                        "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_record()
            case "3":
                search_record_menu()
            case "4":
                change_record()
            case "5":
                delete_record()
            case "6":
                play = False
            case _:
                print("Try again! \n")

if __name__ == "__main__":
    main_menu()