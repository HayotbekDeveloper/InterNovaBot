from db.models import User, async_session


async def add_user(user_id, name, age, description, photo):
    async with async_session() as session:
        user = User(user_id=user_id, name=name, age=age, description=description, photo=photo)
        session.add(user)
        await session.commit()