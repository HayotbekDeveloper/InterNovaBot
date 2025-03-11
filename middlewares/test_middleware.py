from typing import Any, Dict, Awaitable, Callable
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from aiogram.dispatcher.flags import get_flag
from config.bot_config import bot

class ChatActionMiddleware(BaseMiddleware):
    async def __call__(
        self, 
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message, 
        data: Dict[str, Any]
    ) -> Any:
        type_operation = get_flag(data, "type_operation")
        
        if not type_operation:
            return await handler(event, data)
        
        async with ChatActionSender(
            bot=bot, 
            action=type_operation, 
            chat_id=event.chat.id
        ):
            return await handler(event, data)