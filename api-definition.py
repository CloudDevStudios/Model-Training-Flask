from flask import Flask, jsonify, request

app = Flask(__name__)

trainingsdaten = []
modelle = []

@app.route('/trainingsdaten', methods=['POST'])
def upload_trainingsdaten():
    data = request.get_json()
    trainingsdaten.append(data)
    return jsonify({'message': 'Trainingsdaten erfolgreich hochgeladen'})

@app.route('/modelle', methods=['GET'])
def get_modelle():
    return jsonify(modelle)

if __name__ == '__main__':
    app.run(debug=True)
