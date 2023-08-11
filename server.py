from editor import editor
from downloader import download, getExt


import os
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/edit', methods=['POST'])
def edit_handler():
    url = request.args.get('url', '')
    args_hex = request.args.get('args', '')
    args = decode_hex_args(args_hex)
    

    # Process the decoded values
    # You can perform any desired operations on the decoded URL and args here

    file = download(url)
    try:
        result = editor(file, args)

        with open(result.filename, 'rb') as f:
            contents = f.read()

        response = make_response(contents)
        response.headers['Content-Disposition'] = f'attachment; filename={getExt(result.filename)}'

        os.unlink(result.filename) # does this work? will the file still be needed?

        return response, 200  # Replace 200 with your desired status code
    except Exception as e:
        os.unlink(result.filename)
        return str(e), 500

    # editor("samhyde.mp4", "e=1")

def decode_hex_args(hex_args):
    try:
        # Convert hexadecimal string to bytes
        bytes_data = bytes.fromhex(hex_args)

        # Decode bytes using UTF-8
        decoded_args = bytes_data.decode('utf-8')

        return decoded_args
    except Exception as e:
        # Handle any potential exceptions
        return f"[ERROR] {str(e)}"
    


def clearTmp():
    for filename in os.listdir('./tmp'):
        file_path = os.path.join('./tmp', filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            os.rmdir(file_path)

if __name__ == '__main__':
    app.run(port=8738)

clearTmp()