# Visualización de Indicadores del Curso

## Descripción
Proyecto responsive desarrollado en Python Flask para visualizar indicadores del curso (simulados) a partir de registros del LMS Moodle.

## Proceso SCRUM Simplificado

- **Planificación:**  
  - Definir indicadores a mostrar (ej.: completitud, asistencia, calificaciones).  
  - Crear backlog mínimo con funcionalidades esenciales.

- **Ejecución:**  
  - Desarrollar una aplicación Flask básica (ver `app.py`).
  - Implementar pruebas unitarias (ver `test_app.py`).
  - Usar análisis estático con Pylint (se ejecutará más adelante).

- **Revisión:**  
  - Ejecutar pruebas con `pytest` y revisar el código con `pylint`.

- **Retrospectiva:**  
  - Documentar en este README mejoras y lecciones aprendidas.

- **Entrega:**  
  - Consolidar el código, ejecutar la aplicación y generar este documento PDF.
  - Incluir en la carátula:  
    - **Repositorio del código:** [Enlace a GitHub](https://github.com/tu_usuario/tu_repositorio)

## Instrucciones para Ejecutar el Proyecto

1. **Clonar el repositorio y configurar el entorno:**

   ```bash
   git clone <URL-de-tu-repositorio>
   cd flask_indicadores
   pipenv install
   pipenv shell
