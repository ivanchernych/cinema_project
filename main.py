from flask import Flask, render_template, redirect, url_for, request
from data import db_session
from forms.register_form import RegisterForm
from db_table.users import Users
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms.login_form import LoginForm
from db_table.films import Films
from db_table.data_films import Data_films
from db_table.halls import Halls
from db_table.users_tikets import User_tikets
from db_table.pick_user_tikets import Pick_user_tikets
import os
from werkzeug.utils import secure_filename

ROWS = 7
UPLOAD_FOLDER = 'static/image'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dgfhfjhekghejgerkglerjglerjgkejglkejghdjgjhjghjdhguukeqrreyhg'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
login_manager = LoginManager()
login_manager.init_app(app)


def create_hall(id_session, name_hall):
    db_session.global_init('db/cinema.db')
    db_sess = db_session.create_session()
    for i in range(ROWS):
        hall = Halls()
        hall.id_session = id_session
        hall.row = i + 1
        hall.name = name_hall
        db_sess.add(hall)
        db_sess.commit()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(Users).get(user_id)


@app.route('/')
def main():
    db_session.global_init('db/cinema.db')
    db_sess = db_session.create_session()
    films = db_sess.query(Films).all()
    return render_template('movie_list.html', films=films)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/cinema/<name_film>', methods=['GET', 'POST'])
def cinema(name_film):
    db_session.global_init('db/cinema.db')
    db_sess = db_session.create_session()
    films_info = db_sess.query(Films).filter(name_film == Films.name).first()
    halls = db_sess.query(Data_films).filter(films_info.id == Data_films.id_film).all()
    return render_template('info_films.html', films=films_info, halls=halls, open_information_cinema=films_info.name)


@app.route(f'/cinema/<name_film>/<id_session>', methods=['GET', 'POST'])
def halls(name_film, id_session):
    if not current_user.is_authenticated:
        return redirect("/login")
    else:
        info_tikets_table = {}

        db_session.global_init('db/cinema.db')
        db_sess = db_session.create_session()

        info_tikets = db_sess.query(Pick_user_tikets).filter(Pick_user_tikets.id_user == current_user.id,
                                                             Pick_user_tikets.id_data_film == id_session).all()

        if info_tikets:
            info_tikets_table = {
                'кол-во биллетов': len(info_tikets),
                'цена': 0,
                'места': []
            }
            for item in info_tikets:
                price = db_sess.query(Data_films).filter(Data_films.id == item.id_data_film).first()
                info_tikets_table['цена'] += int(price.price)
                info_tikets_table['места'] += [f'ряд {item.row}, место {item.column}']
        halls_info = db_sess.query(Halls).filter(Halls.id_session == id_session).all()
        data_name_hall = db_sess.query(Data_films).filter(Data_films.id == id_session).first()
        if not halls_info:
            create_hall(id_session, data_name_hall.name_hall)
        table_hall = []
        for i in range(ROWS):
            hall_view = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == i + 1).first()
            table_hall.append([i + 1, [[hall_view.column1, 1], [hall_view.column2, 2], [hall_view.column3, 3],
                                       [hall_view.column4, 4], [hall_view.column5, 5], [hall_view.column6, 6],
                                       [hall_view.column7, 7], [hall_view.column8, 8], [hall_view.column9, 9]]])
        return render_template('hall_view.html', hall=table_hall, name_film=name_film, id_session=id_session,
                               info_tikets_table=info_tikets_table)


@app.route(f'/cinema/<name_film>/<id_session>/<int:row>/<int:column>', methods=['GET', 'POST'])
def buy_tikets(name_film, id_session, row, column):
    if not current_user.is_authenticated:
        return redirect("/login")
    db_session.global_init('db/cinema.db')
    db_sess = db_session.create_session()

    tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == row).first()
    if column == 1:
        tikets.column1 = 'x'
        user_tiket = Pick_user_tikets()
        user_tiket.id_user = current_user.id
        id_film = db_sess.query(Films).filter(Films.name == name_film).first()
        user_tiket.id_film = id_film.id
        user_tiket.id_data_film = id_session
        user_tiket.column = column
        user_tiket.row = row
        db_sess.add(user_tiket)
        db_sess.commit()
    elif column == 2:
        tikets.column2 = 'x'
        user_tiket = Pick_user_tikets()
        user_tiket.id_user = current_user.id
        id_film = db_sess.query(Films).filter(Films.name == name_film).first()
        user_tiket.id_film = id_film.id
        user_tiket.id_data_film = id_session
        user_tiket.column = column
        user_tiket.row = row
        db_sess.add(user_tiket)
        db_sess.commit()
    elif column == 3:
        tikets.column3 = 'x'
        user_tiket = Pick_user_tikets()
        user_tiket.id_user = current_user.id
        id_film = db_sess.query(Films).filter(Films.name == name_film).first()
        user_tiket.id_film = id_film.id
        user_tiket.id_data_film = id_session
        user_tiket.column = column
        user_tiket.row = row
        db_sess.add(user_tiket)
        db_sess.commit()
    elif column == 4:
        tikets.column4 = 'x'
        user_tiket = Pick_user_tikets()
        user_tiket.id_user = current_user.id
        id_film = db_sess.query(Films).filter(Films.name == name_film).first()
        user_tiket.id_film = id_film.id
        user_tiket.id_data_film = id_session
        user_tiket.column = column
        user_tiket.row = row
        db_sess.add(user_tiket)
        db_sess.commit()
    elif column == 5:
        tikets.column5 = 'x'
        user_tiket = Pick_user_tikets()
        user_tiket.id_user = current_user.id
        id_film = db_sess.query(Films).filter(Films.name == name_film).first()
        user_tiket.id_film = id_film.id
        user_tiket.id_data_film = id_session
        user_tiket.column = column
        user_tiket.row = row
        db_sess.add(user_tiket)
        db_sess.commit()
    elif column == 6:
        tikets.column6 = 'x'
        user_tiket = Pick_user_tikets()
        user_tiket.id_user = current_user.id
        id_film = db_sess.query(Films).filter(Films.name == name_film).first()
        user_tiket.id_film = id_film.id
        user_tiket.id_data_film = id_session
        user_tiket.column = column
        user_tiket.row = row
        db_sess.add(user_tiket)
        db_sess.commit()
    elif column == 7:
        tikets.column7 = 'x'
        user_tiket = Pick_user_tikets()
        user_tiket.id_user = current_user.id
        id_film = db_sess.query(Films).filter(Films.name == name_film).first()
        user_tiket.id_film = id_film.id
        user_tiket.id_data_film = id_session
        user_tiket.column = column
        user_tiket.row = row
        db_sess.add(user_tiket)
        db_sess.commit()
    elif column == 8:
        tikets.column8 = 'x'
        user_tiket = Pick_user_tikets()
        user_tiket.id_user = current_user.id
        id_film = db_sess.query(Films).filter(Films.name == name_film).first()
        user_tiket.id_film = id_film.id
        user_tiket.id_data_film = id_session
        user_tiket.column = column
        user_tiket.row = row
        db_sess.add(user_tiket)
        db_sess.commit()
    elif column == 9:
        tikets.column9 = 'x'
        user_tiket = Pick_user_tikets()
        user_tiket.id_user = current_user.id
        id_film = db_sess.query(Films).filter(Films.name == name_film).first()
        user_tiket.id_film = id_film.id
        user_tiket.id_data_film = id_session
        user_tiket.column = column
        user_tiket.row = row
        db_sess.add(user_tiket)
        db_sess.commit()

    return redirect(f'/cinema/{name_film}/{id_session}')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_session.global_init("db/cinema.db")
        db_sess = db_session.create_session()
        if db_sess.query(Users).filter(Users.email == form.email.data, Users.login == form.login.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = Users(
            email=form.email.data,
            login=form.login.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Users).filter(Users.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route(f'/profile', methods=['GET', 'POST'])
def profile():
    user = current_user
    db_session.global_init("db/cinema.db")
    db_sess = db_session.create_session()
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            user = db_sess.query(Users).filter(Users.id == user.id).first()
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            user.avatar = filename
            db_sess.commit()

    tikets = []
    tiket_user = db_sess.query(User_tikets).filter(User_tikets.id_user == user.id).all()
    for item in tiket_user:
        film = db_sess.query(Films).filter(Films.id == item.id_film).first()
        data = db_sess.query(Data_films).filter(Data_films.id == item.id_data_film).first()
        tikets.append(
            f'фильм: {film.name}, {data.name_hall}, дата: {data.day} {data.time}, ряд {item.row} место {item.column}')
    user_avatar = db_sess.query(Users).filter(Users.id == user.id).first().avatar
    return render_template('profile.html', user=user, tikets=tikets, avatar=user_avatar)


@app.route(f'/cinema/cancellation/<name_film>/<id_session>', methods=['GET', 'POST'])
def cancellation(name_film, id_session):
    db_session.global_init('db/cinema.db')
    db_sess = db_session.create_session()
    row = db_sess.query(Pick_user_tikets).filter(Pick_user_tikets.id_user == current_user.id,
                                                 Pick_user_tikets.id_data_film == id_session).all()

    for el in row:
        if el.column == 1:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column1 = None
            db_sess.commit()
        elif el.column == 2:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column2 = None
            db_sess.commit()
        elif el.column == 3:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column3 = None
            db_sess.commit()
        elif el.column == 4:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column4 = None
            db_sess.commit()
        elif el.column == 5:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column5 = None
            db_sess.commit()
        elif el.column == 6:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column6 = None
            db_sess.commit()
        elif el.column == 7:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column7 = None
            db_sess.commit()
        elif el.column == 8:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column8 = None
            db_sess.commit()
        elif el.column == 9:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column9 = None
            db_sess.commit()

    db_sess.query(Pick_user_tikets).filter(Pick_user_tikets.id_user == current_user.id,
                                           Pick_user_tikets.id_data_film == id_session).delete()
    db_sess.commit()
    return redirect(f'/cinema/{name_film}/{id_session}')


@app.route(f'/cinema/buy/<name_film>/<id_session>', methods=['GET', 'POST'])
def buy(name_film, id_session):
    db_session.global_init('db/cinema.db')
    db_sess = db_session.create_session()
    row = db_sess.query(Pick_user_tikets).filter(Pick_user_tikets.id_user == current_user.id,
                                                 Pick_user_tikets.id_data_film == id_session).all()
    for el in row:
        if el.column == 1:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column1 = 'buy'
            db_sess.commit()
        elif el.column == 2:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column2 = 'buy'
            db_sess.commit()
        elif el.column == 3:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column3 = 'buy'
            db_sess.commit()
        elif el.column == 4:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column4 = 'buy'
            db_sess.commit()
        elif el.column == 5:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column5 = 'buy'
            db_sess.commit()
        elif el.column == 6:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column6 = 'buy'
            db_sess.commit()
        elif el.column == 7:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column7 = 'buy'
            db_sess.commit()
        elif el.column == 8:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column8 = 'buy'
            db_sess.commit()
        elif el.column == 9:
            tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == el.row).first()
            tikets.column9 = 'buy'
            db_sess.commit()

    tiket = db_sess.query(Pick_user_tikets).filter(Pick_user_tikets.id_user == current_user.id,
                                                   Pick_user_tikets.id_data_film == id_session).all()
    for item in tiket:
        user_tiket = User_tikets()
        user_tiket.id_user = item.id_user
        user_tiket.row = item.row
        user_tiket.column = item.column
        user_tiket.id_data_film = item.id_data_film
        user_tiket.id_film = item.id_film
        db_sess.add(user_tiket)
        db_sess.commit()

    db_sess.query(Pick_user_tikets).filter(Pick_user_tikets.id_user == current_user.id,
                                           Pick_user_tikets.id_data_film == id_session).delete()
    db_sess.commit()

    return redirect(f'/cinema/{name_film}/{id_session}')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
