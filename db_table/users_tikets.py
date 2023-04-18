import sqlalchemy
from data.db_session import SqlAlchemyBase


class User_tikets(SqlAlchemyBase):
    __tablename__ = 'users_tikets'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), autoincrement=True)
    id_data_film = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('data_films.id'), autoincrement=True)
    id_film = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('films.id'), autoincrement=True)
