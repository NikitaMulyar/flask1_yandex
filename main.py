from flask import Flask

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def apples():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    return "<br>".join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                      'Присоединяйся!'])


@app.route('/image_mars')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  </body>
                  <img src="/static/images/mars.jpg" height="216" width="288" alt="здесь должна была быть картинка, но не нашлась"/>
                  <body>
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
