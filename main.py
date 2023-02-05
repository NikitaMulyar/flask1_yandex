from flask import Flask, request
from random import choice


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
</div>""" for i in range(5)])
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/style.css"/>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  </body>
                  <img src="/static/img/mars.jpg" height="216" width="288" alt="здесь должна была быть картинка, но не нашлась"/>
                  <br/><br/>
                  {html_text}
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="static/css/style3.css" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div id="main">
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="second_name" placeholder="Введите Фамилию" name="second_name">
                                        <input type="text" class="form-control" id="first_name" placeholder="Введите Имя" name="first_name">
                                        <br/>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее основное</option>
                                              <option>Среднее полное</option>
                                              <option>Высшее неоконченное</option>
                                              <option>Высшее оконченное</option>
                                              <option>Ыыы бес абрасавания</option>
                                            </select>
                                         </div>
                                         <p>Какие у Вас есть профессии?</p>
                                         <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career" name="about">
                                            <label class="form-check-label" for="career">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career2" name="about">
                                            <label class="form-check-label" for="career2">Пилот</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career3" name="about">
                                            <label class="form-check-label" for="career3">Строитель</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career4" name="about">
                                            <label class="form-check-label" for="career4">Экзобиолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career5" name="about">
                                            <label class="form-check-label" for="career5">Врач</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career6" name="about">
                                            <label class="form-check-label" for="career6">Инженер по терраформированию</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career7" name="about">
                                            <label class="form-check-label" for="career7">Климатолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career8" name="about">
                                            <label class="form-check-label" for="career8">Специалист по радиационной защите</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career9" name="about">
                                            <label class="form-check-label" for="career9">Астрогеолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career10" name="about">
                                            <label class="form-check-label" for="career10">Гляциолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career11" name="about">
                                            <label class="form-check-label" for="career11">Инженер жизнеобеспечения</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career12" name="about">
                                            <label class="form-check-label" for="career12">Метеоролог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career13" name="about">
                                            <label class="form-check-label" for="career13">Оператор марсохода</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career14" name="about">
                                            <label class="form-check-label" for="career14">Киберинженер</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career15" name="about">
                                            <label class="form-check-label" for="career15">Штурман</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career16" name="about">
                                            <label class="form-check-label" for="career16">Пилот дронов</label>
                                        </div>
                                        <br/>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <br/>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="reason"></textarea>
                                        </div>
                                        <br/>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <br/>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <br/>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['first_name'])
        print(request.form['second_name'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form.get('accept'))
        print(request.form['sex'])
        print(request.form['reason'])
        print(request.form)
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planet_info(planet_name):
    text = {'Меркурий': ['Отдаленная от Земли планета.', 'Вот Меркурий. И на нём всё по-другому.',
                         'Он ближайший к Солнцу из планет.', 'Очень быстро там проходят годы,',
                         'А вот сутки... Сутки - вовсе нет.'],
            'Венера:': ['Сестрица Земли', 'Все изумруды будто бы зажглись',
                        'В туманном воздухе блистательной Венеры',
                        'И, словно слезы, звезды пролились', 'На полотно небесной сферы...'],
            'Марс': ['Прекрасная красная планета!', 'Есть предположенье, что когда-то',
                     'Реки марсианские текли -', 'Там, наверно, жизнь была, ребята...',
                     'Но сокрыта тайна Марса от Земли.'],
            'Юпитер': ['Газообразный шар?!', 'Огромная, красивая планета...',
                       'В честь Бога это чудо нарекли...',
                       'Юпитер есть восьмое чудо света...', 'Он зажигает космоса огни...'],
            'Сатурн': ['Царь Хронос.', 'Весь космос красота его затмила...',
                       'Как Бог красив, неповторим Сатурн...',
                       'В той красоте характера стихия...', 'Заворожил собой он всех вокруг...'],
            'Уран': ['Есть, возможно, углеводород,', 'Но мороз такой, что даже летом',
                     'Между скал лежит застывший лёд.',
                     'Будто бы из глубины Вселенной', 'Видим мы Урана тусклый свет,'],
            'Нептун:': ['Восьмой от Солнца, дальше в тридцать раз нашей Земли',
                        'Нептун в сиянье голубом - "морское божество"',
                        'Нашёл, в координатах вычисленных, - Галле.',
                        'Расчетов Адамса и Леверье стал торжеством -',
                        'Всех, чьи труды законы неба открывали.'],
            'Лучшая планета': ['Пассажирам на станции объявляется:',
                               '- Поезд курьерский на Марс отправляется!',
                               'Будем - по точным расчётам диспетчера -',
                               'Мы на Венере в одиннадцать вечера.',
                               'Нам обещал межпланетный дежурный',
                               'Ужин и бал на вокзале Сатурна.',
                               'Можем по Млечному ехать Пути,',
                               'Можем и Солнце кругом обойти.',
                               'Пересечём мы Большую Медведицу.',
                               'Будет доволен тот, кто проедется.',
                               'Тронулся с места небесный экспресс,',
                               'Искрой сверкнул и за тучей исчез.',
                               'Слышится голос какой-то синьоры:',
                               '- Ах, я опять опоздала на скорый!',
                               '- Не огорчайтесь. На небеса',
                               'Новый пойдёт через четверть часа.',
                               '- Благодарю! - отвечает туристка. -',
                               'В сущности, мне поезда не нужны.',
                               'Не тороплюсь я, а ехать мне близко.',
                               'Доеду в троллейбусе до Луны.'],
            'Земля': ['Планета Земля — родимый наш дом.',
                      'Но много ли мы знаем о нем?',
                      'Загадки ее постоянно решаем.',
                      'Но форму Земли до конца мы не знаем.',
                      'А форма Земли без рек и морей',
                      'Зовется геоид! Учи и умней!',
                      'А что там внутри? Принимаем на веру.',
                      'Не видно ядро. Летим в атмосферу!',
                      'Мы ей благодарны, что можем дышать',
                      'И много проблем с нею можем решать.'],
            'Плутон': ['Ворота в него — на краю океана?',
                       'Хоть мал, но имеет Плутон свою свиту:',
                       'Побольше - Харон, меньше - Никта и Гидра,',
                       'Кружатся над богом по разным орбитам,',
                       'Харон приближается, кажется слитным.']}
    if planet_name not in text:
        planet_name = 'Лучшая планета'
    colors = ['dark', 'success', 'secondary', 'warning', 'danger', 'primary', 'info', 'light']
    html_text = "".join([f"""<div class="alert alert-{choice(colors)}" role="alert">
  {i}
</div>""" for i in text[planet_name]])
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Варианты выбора</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/style.css"/>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                  </body>
                  {html_text}
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def test(nickname, level, rating):
    colors = ['success', 'warning', 'danger']
    if rating < 60:
        clr = colors[2]
    elif rating < 80:
        clr = colors[1]
    else:
        clr = colors[0]
    html_text = f"""<div class="alert alert-{clr}" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора:</div>"""
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Результаты</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <h4>{html_text}
                    составляет {rating}!
                    <div class="alert alert-info" role="alert">Желаем удачи!</div></h4>
                  </body>
                </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="static/css/style3.css" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div id="main">
                                <h1>Загрузка фотографии</h1>
                                <h2>для участия в миссии</h2>
                                <form class="login_form" method="post">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input class="form-control-file" type="file" id="photo" name="file" onchange="preview()">
                                        <br/><br/>
                                        <img id="frame" src="" class="img-fluid" />
                                        <br/><br/>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>

                            <script>
                                function preview() {
                                    frame.src = URL.createObjectURL(event.target.files[0]);
                                }
                            </script>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('file'))
        return "Форма отправлена"


@app.route('/carousel')
def photos():
    s = 4
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="static/css/style4.css" />
                        <title>Пейзажи "Доктор Кто"</title>
                      </head>
                      <body>
                        <div id="main">
                            <h1>Красивые пейзажи!</h1>
                            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                              <ol class="carousel-indicators">
                                <li data-target="#carouselExampleIndicators" data-slide-to="0"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                                <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
                              </ol>
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img class="d-block w-100" src="static/img/doc1.jpeg" alt="First slide">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="static/img/doc2.jpeg" alt="Second slide">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="static/img/doc3.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="static/img/doc4.jpeg" alt="Fourth slide">
                                </div>
                              </div>
                              <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                        </div>
                        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
