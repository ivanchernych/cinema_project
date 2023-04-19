from flask import Flask, render_template, redirect
from data import db_session
from forms.register_form import RegisterForm
from db_table.users import Users
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms.login_form import LoginForm
from db_table.films import Films
from db_table.data_films import Data_films
from db_table.halls import Halls
from db_table.users_tikets import User_tikets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dgfhfjhekghejgerkglerjglerjgkejglkejghdjgjhjghjdhguukeqrreyhg'
login_manager = LoginManager()
login_manager.init_app(app)


def create_hall(id_session, name_hall):
    db_session.global_init('db/cinema.db')
    db_sess = db_session.create_session()
    for i in range(7):
        hall = Halls()
        hall.id_session = id_session
        hall.row = i + 1
        hall.name = name_hall
        db_sess.add(hall)
        db_sess.commit()


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
    db_session.global_init('db/cinema.db')
    db_sess = db_session.create_session()

    halls_info = db_sess.query(Halls).filter(Halls.id_session == id_session).all()
    data_name_hall = db_sess.query(Data_films).filter(Data_films.id == id_session).first()
    if not halls_info:
        create_hall(id_session, data_name_hall.name_hall)
    table_hall = []
    for i in range(7):
        hall_view = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == i + 1).first()
        table_hall.append([i + 1, [[hall_view.column1, 1], [hall_view.column2, 2], [hall_view.column3, 3], [hall_view.column4, 4],
                           [hall_view.column5, 5], [hall_view.column6, 6], [hall_view.column7, 7]]])
    return render_template('hall_view.html', hall=table_hall, name_film=name_film, id_session=id_session)


@app.route(f'/cinema/<name_film>/<id_session>/<int:row>/<int:column>', methods=['GET', 'POST'])
def buy_tikets(name_film, id_session, row, column):
    if not current_user.is_authenticated:
        return redirect("/login")
    db_session.global_init('db/cinema.db')
    db_sess = db_session.create_session()

    tikets = db_sess.query(Halls).filter(Halls.id_session == id_session, Halls.row == row).first()

    if column == 1:
        print('+')
        tikets.column1 = 'x'

        user_tiket = User_tikets()

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
        user_tiket = User_tikets()

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
        user_tiket = User_tikets()

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
        user_tiket = User_tikets()

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
        user_tiket = User_tikets()

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
        user_tiket = User_tikets()

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
        user_tiket = User_tikets()

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


if __name__ == '__main__':
    app.run(port=8080,  host='127.0.0.1')
