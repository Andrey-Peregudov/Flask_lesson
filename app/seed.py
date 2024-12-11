from models import User, Tovar, Zakaz, Address
from main import db


def seeds():
    data = User(name="Vasiliy", is_active=True)
    data.set_password('111')
    db.session.add(data)
    db.session.commit()
    db.session.refresh(data)

    addr = Address(city='Kazan', ulica='Lenina', user_id=data.id)
    addr2 = Address(city='Voronezh', ulica='Kosmonavtov', user_id=data.id)

    db.session.add(addr)
    db.session.add(addr2)
    db.session.commit()


    data4 = Tovar(name="Костюм", price=50, ostatok=20, url_photo="suit.jpg")
    data5 = Tovar(name="Брюки", price=150, ostatok=14, url_photo="trousers.jpg")
    data6 = Tovar(name="Рубашка", price=250, ostatok=10, url_photo="shirt.jpg")

    db.session.add(data4)
    db.session.add(data5)
    db.session.add(data6)

    db.session.commit()

#Добавление заказа
    zakaz = Zakaz(user_id=data.id, tovar_id=data4.id, quantity=5)


    db.session.add(zakaz)

    db.session.commit()
