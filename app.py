#!/usr/bin/env python

import cgi

# Define a função para a conversão de Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 1.8) + 32

# Cria um objeto FieldStorage para obter os dados do formulário
form = cgi.FieldStorage()

# Verifica se o formulário foi enviado
if form:
    # Obtém o valor do campo Celsius do formulário
    celsius = float(form.getvalue('celsius'))

    # Realiza a conversão para Fahrenheit
    fahrenheit = celsius_para_fahrenheit(celsius)

    # Exibe o resultado da conversão na página
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head>")
    print("<title>Conversor de Celsius para Fahrenheit</title>")
    print("</head>")
    print("<body>")
    print("<h1>Conversor de Celsius para Fahrenheit</h1>")
    print("<p>O resultado da conversão é: %.2f °F</p>" % fahrenheit)
    print("</body>")
    print("</html>")
else:
    # Exibe o formulário para que o usuário digite o valor em Celsius
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head>")
    print("<title>Conversor de Celsius para Fahrenheit</title>")
    print("</head>")
    print("<body>")
    print("<h1>Conversor de Celsius para Fahrenheit</h1>")
    print("<form method='post'>")
    print("<label for='celsius'>Graus Celsius:</label>")
    print("<input type='number' id='celsius' name='celsius' required>")
    print("<br>")
    print("<button type='submit'>Converter</button>")
    print("</form>")
    print("</body>")
    print("</html>")
