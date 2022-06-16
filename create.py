from app import db, Owners, Car

db.drop_all() # this is a comment :P
db.create_all()


# person1 = Owners(first_name="Dave", last_name="Smith")
# db.session.add(person1)
# db.session.commit()

# car1 = Car(reg="WQA1 3TF", ownerbr=person1)
# db.session.add(car1)
# db.session.commit()
# car2 = Car(reg="SOMETHING", ownerbr=person1)
# db.session.add(car2)
# db.session.commit()

# print(person1.cars)

# print(car1.ownerbr.last_name + ', ' + car1.ownerbr.first_name)