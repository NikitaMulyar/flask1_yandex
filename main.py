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
                  <img src="/static/img/mars.jpg" height="216" width="288" alt="здесь должна была быть картинка, но не нашлась"/>
                  <body>
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promo_image():
    text = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
            'Присоединяйся!']
    colors = ['dark', 'success', 'secondary', 'warning', 'danger']
    html_text = "".join([f"""<div class="alert alert-{colors[i]}" role="alert">
  {text[i]}
</div>"""for i in range(5)])
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  </body>
                  <img src="/static/img/mars.jpg" height="216" width="288" alt="здесь должна была быть картинка, но не нашлась"/>
                  <br/><br/>
                  {html_text}
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
