from flask import Flask, jsonify, request

app = Flask(__name__)

tareas = [
    {"id": 1, "titulo": "Leer sobre APIs", "completada": False},
    {"id": 2, "titulo": "Probar Postman", "completada": True}
]

@app.get("/tareas")
def obtener_tareas():
    return jsonify(tareas), 200

@app.get("/tareas/<int:id>")
def obtener_tarea(id):
    for tarea in tareas:
        if tarea["id"] == id:
            return jsonify(tarea), 200
    return jsonify({"error": "Tarea no encontrada"}), 404

@app.post("/tareas")
def crear_tarea():
    datos = request.get_json()
    if not datos or "titulo" not in datos:
        return jsonify({"error": "Falta el campo 'titulo'"}), 400
    
    nuevo_id = tareas[-1]["id"] + 1 if tareas else 1
    nueva_tarea = {
        "id": nuevo_id, 
        "titulo": datos["titulo"],
        "completada": datos.get("completada", False)
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
