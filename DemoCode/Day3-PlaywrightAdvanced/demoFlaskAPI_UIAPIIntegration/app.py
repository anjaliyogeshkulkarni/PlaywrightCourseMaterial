from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

def append_to_text_file(data, filename):
    try:
        # Ensure the directory exists.
        if os.path.dirname(filename):
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as fwrite:
            # Convert data to a comma-separated string
            # data_str = ",".join(map(str, data.values())) + "\n"
            # print(data_str)
            chars_added = fwrite.write(data)
            print(f"Data successfully appended to {filename}")
            return chars_added
    except Exception as e:
        print(f"Error appending to file: {e}")
        raise

def read_from_text_file(filename="my_data.txt"):
    """
    Reads data from a local text file and returns it as a list of lists.

    Args:
        filename (str, optional): The name of the text file. Defaults to "data.txt".

    Returns:
        list: A list of lists, where each inner list represents a row of data.
              Returns an empty list if the file does not exist or an error occurs.
    """
    try:
        if not os.path.exists(filename):
            print(f"File not found: {filename}")
            return []  # Return an empty list if the file doesn't exist

        with open(filename, "r") as f:
            lines = f.readlines()
        data = []
        for line in lines:
            row = line.strip().split(",")
            print (row)
            data.append(row)
        return data
    except Exception as e:
        print(f"Error reading from file: {e}")
        return []  # Return an empty list if an error occurs


@app.route('/demo_post_endpoint', methods=['POST'])
def demo_post():

    try:
        # Get the JSON data from the request body.
        form_data = request.get_json()
        name = form_data.get("name")
        age = form_data.get("age")

        data = name + "," + age + "\n"
        # Check if the data is valid (optional, but recommended).
        if not data:
            return jsonify({'error': 'No data provided in the request body'}), 400  # Bad Request
        else:
            # Process the data.
            print('Received data:', data)

            # Append data to the text file.
            try:
                chars_added = append_to_text_file(data, filename="my_data.txt")
                message = f'Records added successfully.'
            except Exception as e:
                message = f'Records Not updated in File.'
                return jsonify({'error': f'Failed to write to file: {e}'}), 500

        response_data = {
            'message': message,
            'chars_added': chars_added,
            'status': 'success'
        }
        response_json = jsonify(response_data)
        return response_json, 200

    except Exception as e:
        # Handle errors.
        error_message = f'An error occurred: {str(e)}'
        return jsonify({'error': error_message}), 500

@app.route('/demo_get_endpoint', methods=['GET'])
def demo_get():
    if not os.path.exists("my_data.txt"):
        return jsonify({"name": "", "age": ""})

    with open("my_data.txt", "r") as f:
        line = f.readline().strip()  # Read first line

    if not line:
        return jsonify({"name": "", "age": ""})

    name, age = line.split(",")
    return jsonify({"name": name, "age": age})


if __name__ == '__main__':
    app.run(debug=True)
