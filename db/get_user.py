from db.models import User, async_session
from sqlalchemy import select

async def get_user(user_id):
    async with async_session() as session:
        result = await session.scalar(select(User).where(User.user_id == user_id))
        return result