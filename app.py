from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def home():
    return "Servicio Web para convertir imágenes. Usa /convert con una imagen."

@app.route('/convert', methods=['POST'])
def convert_image():
    if 'image' not in request.files:
        return "No se ha subido ninguna imagen", 400

    file = request.files['image']
    format_to = request.form.get('format', 'JPEG')  # Por defecto convierte a JPEG

    try:
        img = Image.open(file)
        img_io = io.BytesIO()
        img.save(img_io, format=format_to)
        img_io.seek(0)
        return send_file(img_io, mimetype=f'image/{format_to.lower()}')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
