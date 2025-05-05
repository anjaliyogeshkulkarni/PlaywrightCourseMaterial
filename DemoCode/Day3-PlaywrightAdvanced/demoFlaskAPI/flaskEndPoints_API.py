from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def append_to_text_file(data, filename):
    try:
        # Ensure the directory exists.
        if os.path.dirname(filename):
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "a") as fappend:
            # Convert data to a comma-separated string
            data_str = ",".join(map(str, data.values())) + "\n"
            print(data_str)
            chars_added = fappend.write(data_str)
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
def handle_post():

    try:
        # Get the JSON data from the request body.
        data = request.get_json()

        # Check if the data is valid (optional, but recommended).
        if not data:
            return jsonify({'error': 'No data provided in the request body'}), 400  # Bad Request
        else:
            # Process the data.
            print('Received data:', data)

            # Append data to the text file.
            try:
                chars_added = append_to_text_file(data, filename="my_data.txt")
            except Exception as e:
                return jsonify({'error': f'Failed to write to file: {e}'}), 500

        # Create a response.
        if 'name' in data and 'age' in data:
            message = f'Records added successfully.'
        else:
            message = "File Not Updated"
        response_data = {
            'message': message,
            'chars_added': chars_added,
            'status': 'success'
        }
        print("Response Message: ",message)
        response_json = jsonify(response_data)
        return response_json, 200

    except Exception as e:
        # Handle errors.
        error_message = f'An error occurred: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 500

@app.route('/demo_get_endpoint', methods=['GET'])
def handle_get():
    """
    This function handles GET requests to the '/my_get_endpoint' URL.
    It reads data from the text file and returns it as a JSON response.
    """
    try:
        file_data = read_from_text_file(filename="my_data.txt")  # Read the data
        print("FileData : ",file_data)
        if not file_data:
            return jsonify({'message': 'No data available or file is empty'}), 200  # send 200 ok, with message
        else:
            return jsonify(file_data), 200

    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 500

@app.route('/demo_delete_endpoint', methods=['DELETE'])
def handle_delete():
    try:
        print("In delete API")
        os.remove("my_data.txt")
        message ="File Deleted"
        return jsonify({'output': message}), 200
    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
