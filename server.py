import uuid

from flask import Flask, request, jsonify, render_template
import base64
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'app/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    data = request.get_json()
    image_data = data['image']
    image_data = image_data.split(",")[1]  # Remove the data URL prefix
    image_bytes = base64.b64decode(image_data)

    # Generate a unique filename
    filename = str(uuid.uuid4()) + '.png'
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, 'wb') as file:
        file.write(image_bytes)

    return jsonify({'message': 'Image uploaded successfully', 'filename': filename})


if __name__ == '__main__':
    app.run(debug=True)
