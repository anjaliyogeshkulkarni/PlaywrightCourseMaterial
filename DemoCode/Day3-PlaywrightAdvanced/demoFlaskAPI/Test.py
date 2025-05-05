import os

def append_to_file(filename, data):

    with open(filename, "a") as f:
        data = {'name': 'Bob', 'age': 25}
        print(data)
        # Convert data to a comma-separated string
        data_str = ",".join(map(str, data.values())) + "\n"
        print(data_str)
        chars_added = f.write(data_str)
        print(f"Data successfully appended to {filename}")
        return chars_added

payload = {'name': 'Bob', 'age': 25}
chars_added = append_to_file("my_data.txt",payload)
print(chars_added)

