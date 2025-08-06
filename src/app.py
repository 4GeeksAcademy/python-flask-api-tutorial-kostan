from flask import Flask, jsonify, request
app = Flask(__name__)


some_data = { "name": "Bobby", "lastname": "Rixer" }
todos = [{
        "label": "Sample", "done": True
    }]


todo_counter = 1

@app.route('/myroute', methods=['GET'])
def hello_world():
    json_text = jsonify(some_data)
    return json_text

@app.route('/todos', methods=['GET'])
def hello():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    if not request_body:
        return jsonify({'error': 'faltan datos'}), 400
    todos.append(request_body)
    return jsonify(list(todos)), 200 

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        del todos[position]
        return jsonify(todos), 200
    else:
        return jsonify({'error': 'Tarea no encontrada'}), 404




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)