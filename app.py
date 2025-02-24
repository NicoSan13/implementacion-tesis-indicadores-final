"""
Módulo principal de la aplicación Flask para la visualización de indicadores del curso.
Incluye rutas para mostrar indicadores en formato HTML y JSON, y maneja errores personalizados.
"""

import random
from flask import Flask, render_template, jsonify, abort

app = Flask(__name__)


def obtener_indicadores():
    """
    Simula la obtención de indicadores del curso.

    Retorna:
        dict: Diccionario con indicadores generados aleatoriamente.
    """
    return {
        "completitud": random.randint(70, 100),
        "asistencia": random.randint(80, 100),
        "calificaciones": random.randint(60, 100),
    }


@app.route("/")
def index():
    """
    Ruta principal que muestra los indicadores del curso en formato HTML.

    Retorna:
        HTML renderizado desde la plantilla 'index.html'.
    """
    indicadores = obtener_indicadores()
    return render_template("index.html", indicadores=indicadores)


@app.route("/api/indicadores", methods=["GET"])
def api_indicadores():
    """
    API que retorna los indicadores del curso en formato JSON.

    Retorna:
        JSON: Diccionario con los indicadores.
    """
    indicadores = obtener_indicadores()
    if not indicadores:
        abort(404)
    return jsonify(indicadores)


@app.errorhandler(404)
def not_found():
    """
    Maneja el error 404 mostrando una página personalizada.

    Retorna:
        tuple: HTML renderizado desde la plantilla '404.html' y el código de estado 404.
    """
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
