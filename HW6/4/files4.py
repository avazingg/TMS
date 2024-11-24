def create_binary_content_into_file(file_name, number_of_file):
    with open (file_name, "wb") as file:
        file.writelines([f"hello, it's file number {number_of_file}\n".encode(),
                         f"yep, it's content of file: {number_of_file}\n".encode(),
                         f"{number_of_file} {number_of_file} {number_of_file}".encode()
                         ])

def read_binary_data_from_file(file_name):
    storage = []
    with open(file_name, "rb") as file:
        for line in file:
            storage.append(line.decode())
    print(storage)
    return  storage

def rewrite_file_content(file_name, storage):
    with open(file_name, "wb") as file:
        for element in storage:
            file.write(element.encode())

create_binary_content_into_file("file1.bin",1)
create_binary_content_into_file("file2.bin",2)
storage1 = read_binary_data_from_file("file1.bin")
storage2 = read_binary_data_from_file("file2.bin")
rewrite_file_content("file1.bin", storage2)
rewrite_file_content("file2.bin", storage1)
