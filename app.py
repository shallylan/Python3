from sqlalchemy import create_engine
from sqlalchemy.ext.decalarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from datetime import DateTime

engine = create_engine('mysql://root:@localhost/shiyanlou')

Base = declarative_base()

class File(Base):
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    created_time = Column(DateTime)
    category_id = Column(Integer, ForeignKey('Category.id'))
    content = Column(Text)
    def __repr__(self):
        return "<File(name=%s)>" % self.name

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))

Base.metadata.create_all(engine)



