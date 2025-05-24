from db.session import Base
from sqlalchemy import Column, String
from db.mixins import TimeStampModelMixin

class Todo(TimeStampModelMixin, Base):    
    title = Column(String,nullable=False)
