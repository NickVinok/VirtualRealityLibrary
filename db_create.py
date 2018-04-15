from DatabasesTest import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(20), index = True)
    email = db.Column(db.String(64), index = True, unique=True)
    income = db.Column(db.Integer)
    rooms = db.relationship("Rooms", backref='person', lazy=True)
    userToArt = db.relationship('Art', secondary=userToArt, lazy='subquery',
                           backref=db.backref('users', lazy=True))

    def __repr__(self):
        return "<User %r>" % self.login


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('x1ser.id'))
    roomToArt = db.Relationship("Art", secondary=roomToArt, lazy = 'subquery', backref=db.backref('Rooms', lazy = True))


class Art(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey(User.id), lazy='joined')


roomToArt = db.Table("pieces_of_art_in rooms",  db.Column("room_id", db.ForeignKeys("Room.id"),primary_key = True),
                     db.Column("Art_id", db.ForeignKeys("Art.id"), primary_key=True))

userToArt = db.Table("pieces_of_art_on_users", db.Column("art_id", db.ForeignKeys("Art.id"), primary_key=True),
                     db.Column("User_id", db.ForeignKeys("User.id"), primary_key = True))
