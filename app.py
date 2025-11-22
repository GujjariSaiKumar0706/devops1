from flask import Flask,jsonify,request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)    

students = [
    {'id': 1, 'name': 'Alice', 'age': 20},
]
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)
@app.route('/new-student',methods=['POST'])
def add_student():
    new_student = request.json 
    students.append(new_student)
    return jsonify({'message':'new student added'}), 201
@app.route('/update-student/<int:ind>', methods=['PATCH'])
def get_student(ind):
    student = request.json
    students[ind].update(student)
    return jsonify({'message':'student details updated'}), 200

@app.route('/delete-student/<int:ind>', methods=['DELETE'])
def delete_student(ind):
    students.pop(ind)
    return jsonify({'message':'student deleted'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)
    