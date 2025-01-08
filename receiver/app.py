import os
from flask import Flask, request

app = Flask(__name__)
UPLOAD_FOLDER = "./uploads/"

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "Error: No file part in the request.", 400

    file = request.files["file"]
    if file.filename == "":
        return "Error: No file selected.", 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return f"File received and saved as {file_path}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    


