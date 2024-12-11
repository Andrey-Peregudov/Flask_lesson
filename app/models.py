import sqlalchemy as sa
from main import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    password_hash = sa.Column(sa.String(255), nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)
    admin = sa.Column(sa.Boolean, default=False)

    id_tovar = db.Column(sa.Integer, db.ForeignKey('tovars.id'))

    address = db.relationship('Address', backref='address', lazy='dynamic')

    #Создания отношения между таблицами users и zakaz (1 to 1)
    zakaz = db.relationship('Zakaz', backref='users', uselist=False)



    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Address(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    city = sa.Column(sa.String(255))
    ulica = sa.Column(sa.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Tovar(db.Model):
    __tablename__ = 'tovars'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    url_photo = sa.Column(sa.String(255), nullable=True)
    price = sa.Column(sa.Integer, nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)
    ostatok = sa.Column(sa.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Создания отношения между таблицами tovars и zakaz (meny to one)
    zakaz = db.relationship('Zakaz', backref='tovars')


#Таблица для связи товаров и пользователей
class Zakaz(db.Model):
    __tablename__ = 'zakaz'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, db.ForeignKey('users.id'))
    tovar_id = sa.Column(sa.Integer, db.ForeignKey('tovars.id'))
    quantity = sa.Column(sa.Integer, nullable=False)

