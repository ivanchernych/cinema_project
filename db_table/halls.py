import sqlalchemy
from data.db_session import SqlAlchemyBase


class Halls(SqlAlchemyBase):
    __tablename__ = 'halls'

    id_session = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    row = sqlalchemy.Column(sqlalchemy.Integer)
    column1 = sqlalchemy.Column(sqlalchemy.String)
    column2 = sqlalchemy.Column(sqlalchemy.String)
    column3 = sqlalchemy.Column(sqlalchemy.String)
    column4 = sqlalchemy.Column(sqlalchemy.String)
    column5 = sqlalchemy.Column(sqlalchemy.String)
    column6 = sqlalchemy.Column(sqlalchemy.String)
    column7 = sqlalchemy.Column(sqlalchemy.String)
    column8 = sqlalchemy.Column(sqlalchemy.String)
    column9 = sqlalchemy.Column(sqlalchemy.String)


