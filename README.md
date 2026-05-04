
* Python 3.9 o superior
* pip
* Docker



## Estructura del proyecto
.
├── app.py
├── Docker/Dockerfile
└── README.md



### Instalar dependencias

```bash
pip install flask
```

### Ejecutar la aplicación

```bash
python app.py
```

### Acceder a la API

La API estará disponible en:

```
http://localhost:5000
```

---

## Ejecución con Docker

### Construir la imagen

```bash
docker build -t api-tareas -f docker/Dockerfile .
```

### Ejecutar el contenedor

```bash
docker run -p 5000:5000 api-tareas
```
