import webbrowser
import os

# HTML de la primera página (fondo negro con el mensaje)
html_content_1 = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Google</title>
    <style>
        body {
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 20%;
            cursor: pointer;
        }
        .small-text {
            font-size: 12px;
            color: gray;
        }
    </style>
</head>
<body>
    <h1>¡Marca tu asistencia con nosotros!</h1>
    <p class="small-text">Haz click en cualquier parte de la página para continuar</p>

    <script>
        // Espera a que el DOM esté listo
        document.addEventListener('DOMContentLoaded', function() {
            document.body.addEventListener('click', function() {
                // Usa la ruta absoluta de pagina2.html
                window.location.href = "file://""" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagina2.html").replace("\\", "/") + """";
            });
        });
    </script>
</body>
</html>
"""

# HTML de la segunda página (fondo negro con los botones de login y registro)
html_content_2 = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Opciones</title>
    <style>
        body {
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 20%;
        }
        .button {
            background-color: #4CAF50; /* Verde */
            color: white;
            padding: 15px 32px;
            text-align: center;
            font-size: 16px;
            margin: 10px;
            cursor: pointer;
            border: none;
            border-radius: 4px;
        }
        .button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Bienvenido</h1>
    <button class="button" onclick="alert('Iniciar sesión')">Iniciar sesión</button>
    <button class="button" onclick="alert('Registrarse')">Registrarse</button>
</body>
</html>
"""

# Crear un directorio para almacenar los archivos HTML si no existe
output_dir = os.path.dirname(os.path.abspath(__file__))
file_name_1 = os.path.join(output_dir, "pagina1.html")
file_name_2 = os.path.join(output_dir, "pagina2.html")

# Guardar la primera página en un archivo HTML
with open(file_name_1, "w", encoding="utf-8") as file:
    file.write(html_content_1)

# Guardar la segunda página en un archivo HTML
with open(file_name_2, "w", encoding="utf-8") as file:
    file.write(html_content_2)

# Abrir la primera página en el navegador utilizando la ruta absoluta
webbrowser.open_new_tab(f"file://{file_name_1}")