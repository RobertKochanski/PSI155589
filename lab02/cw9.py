from file_manager import FileManager

print(FileManager('file.txt').read_file())
FileManager('file.txt').update_file('test ')
print(FileManager('file.txt').read_file())
