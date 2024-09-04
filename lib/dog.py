from models import Dog

def create_table(base, engine):
    base

def save(session, dog):
    session.add(dog)

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    dogs = session.query(Dog).filter(Dog.name == name).first()
    return dogs

def find_by_id(session, id):
    dogs = session.query(Dog).filter(Dog.id == id).first()
    return dogs

def find_by_name_and_breed(session, name, breed):
    dogs = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dogs

def update_breed(session, dog, breed):
    if dog:
        dog.breed = breed
        session.commit()