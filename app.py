from flask import Flask, render_template, request

app = Flask(__name__)

medications = []

@app.route('/')
def index():
    return render_template('index.html', medications=medications)

@app.route('/add', methods=['POST'])
def add_medication():
    med_name = request.form['med_name']
    dosage = request.form['dosage']
    time = request.form['time']
    medications.append({'name': med_name, 'dosage': dosage, 'time': time})
    return render_template('index.html', medications=medications)

if __name__ == '__main__':
    app.run(debug=True)
