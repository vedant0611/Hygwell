from sqlalchemy import Column, Integer, String, Text
from database import Base

class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String, unique=True, index=True)
    content = Column(Text)
    content_type = Column(String)  # 'url' or 'pdf'