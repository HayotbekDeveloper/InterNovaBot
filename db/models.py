from config.bot_config import SQLALCHEMY_URL
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


engine = create_async_engine(SQLALCHEMY_URL, echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int]= mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    description: Mapped[str]= mapped_column()
    photo: Mapped[str] = mapped_column()
    
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)