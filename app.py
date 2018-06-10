from flask import Flask
from Flask_SQLAlchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI']='mysql://root:@localhost/shiyanlou'
db = SQLAlchemy(app)


class File(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))
    content = db.Column(db.Text)
    category = relationship('Category', backref='file')
    def __repr__(self):
        return "<File(name=%s)>" % self.name

class Category(Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    def __repr__(self):
        return '<Category(name=%s)>' % self.name

if __name__ == '__main__':
    db.create_all()
    app.run()




