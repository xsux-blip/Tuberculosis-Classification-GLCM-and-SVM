from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

app = Flask(__name__, static_url_path="/static")

app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = {".jpg", ".jpeg", ".png"}
app.config["UPLOAD_PATH"] = "./static/images/uploads/"

model = None


# Fungsi untuk memeriksa ekstensi berkas yang diunggah
def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["UPLOAD_EXTENSIONS"]
    )


# Fungsi untuk memprediksi kelas gambar
def predict_class(image_data):
    # Ganti dengan logika prediksi sesuai dengan model Anda
    return "Normal"


@app.route("/")
def beranda():
    return render_template("index.html")


@app.route("/api/deteksi", methods=["POST"])
def apiDeteksi():
    hasil_prediksi = "(none)"
    gambar_prediksi = "(none)"

    if "file" not in request.files:
        return jsonify({"error": "No file part"})

    uploaded_file = request.files["file"]

    if uploaded_file.filename == "":
        return jsonify({"error": "No selected file"})

    # if uploaded_file and allowed_file(uploaded_file.filename):
    filename = secure_filename(uploaded_file.filename)
    gambar_prediksi = "/static/images/uploads/" + filename
    file_path = os.path.join(app.config["UPLOAD_PATH"], filename)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    test_image = Image.open(file_path)
    test_image_resized = test_image.resize((500, 500))
    test_image_rgb = test_image_resized.convert(
        "L"
    )  # Ensure the image has RGB channels
    image_array = np.array(test_image_rgb)
    # test_image_x = image_array / 255

    # Expand the shape to match model input shape (None, 200, 200, 3)
    test_image_x = np.expand_dims(image_array, axis=0)

    hasil_prediksi = model.predict(test_image_x / 255)

    if hasil_prediksi[0][0] > 0.5:
        hasil = "Tuberculosis"
    else:
        hasil = "Normal"
    return jsonify({"prediksi": hasil, "gambar_prediksi": gambar_prediksi})


if __name__ == "__main__":
    model = load_model("model_tbc.h5")
    app.run(debug=True)
