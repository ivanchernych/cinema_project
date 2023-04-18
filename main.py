from flask import Flask, render_template, redirect
from data import db_session
from forms.register_form import RegisterForm
from db_table.users import Users
from flask_login import LoginManager, login_user, logout_user, login_required
from forms.login_form import LoginForm
from db_table.films import Films

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dgfhfjhekghejgerkglerjglerjgkejglkejghdjgjhjghjdhguukeqrreyhg'
login_manager = LoginManager()
login_manager.init_app(app)


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
    print(films_info.name)
    return render_template('info_films.html', films=films_info)


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
