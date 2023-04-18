import sqlalchemy
from data.db_session import SqlAlchemyBase


class Data_films(SqlAlchemyBase):
    __tablename__ = 'data_films'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_film = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('films.id'), autoincrement=True)
    day = sqlalchemy.Column(sqlalchemy.String)
    time = sqlalchemy.Column(sqlalchemy.String)
    hall_session = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('halls.id_session'), autoincrement=True)