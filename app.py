from flask import Flask, render_template, request
import pytesseract
from PIL import Image

app = Flask(__name__)

# Definindo o caminho do Tesseract no Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""

    if request.method == "POST":
        image_file = request.files["image"]
        image = Image.open(image_file)
        # Faz OCR em português
        text = pytesseract.image_to_string(image, lang="por")

    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
