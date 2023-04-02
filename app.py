from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

app = Flask(__name__)

# Cargar el modelo guardado
model = load_model('model.h5')

# Definir una función para procesar la imagen
def predict_image(file):
    image = Image.open(file).convert('RGB')
    image = image.resize((32, 32))
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)[0]
    return prediction

# Definir la ruta de la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Definir la ruta para procesar la imagen cargada
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        prediction = predict_image(file)
        predicted_class = np.argmax(prediction)
        class_names = ['clase1', 'clase2', 'clase3'] # Reemplazar con las clases de tu modelo
        predicted_class_name = class_names[predicted_class]
        return render_template('result.html', predicted_class=predicted_class_name)

if __name__ == '__main__':
    app.run(debug=True)