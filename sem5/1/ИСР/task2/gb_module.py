# писал сам, не нашел старой лабы
import json
import os


class GuestBook:


    def make_json(self, filename = 'data.json'):
        with open(filename, 'w') as file:
            file.write('')

    
    def delete_json(self, filename = 'data.json'):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        os.remove(path)


    def rename_json(self, new_filename, filename = 'data.json'):
        os.rename(filename, new_filename)


    def read_json(self, filename = 'data.json'):
        with open(filename, 'r') as file:
            read_json = json.load(file)
        return read_json

    
    def write_json(self, json_text, filename = 'data.json'):
        with open(filename, 'w') as file:
            json.dump(json_text, file, ensure_ascii=False, indent=4)



# GuestBook.make_json()
# print(GuestBook.read_json())
# GuestBook.delete_json('data_copy.json')
# GuestBook.rename_json('super_data.json')

