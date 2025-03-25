from bot import bot
from pyrogram import types, enums, errors, filters
from logging import getLogger
import text_manager as tm


logger = getLogger(__name__)


async def send_text(user: types.User, text_key: str, **kwargs):
    try: 
        if kwargs.__len__() == 0:
            await bot.send_message(
                chat_id=user.id,
                text=tm.get_by_lang_code(text_key, language_code=user.language_code)
            )
        else:
            await bot.send_message(
                chat_id=user.id,
                text=tm.get_by_lang_code(text_key, language_code=user.language_code).format(**kwargs)
            )
    except errors.PeerIdInvalid:
        pass
    except errors.UserIsBot:
        pass


@bot.on_chat_member_updated()
async def on_chat_member_updated(_, cmu: types.ChatMemberUpdated):
    if cmu.new_chat_member.user.is_self:

        if (cmu.new_chat_member.status == enums.ChatMemberStatus.LEFT) or (cmu.new_chat_member.status == enums.ChatMemberStatus.BANNED):
            return
        
        if (cmu.new_chat_member.status == enums.ChatMemberStatus.ADMINISTRATOR) and (cmu.new_chat_member.privileges.can_restrict_members):
            banned = []
            async for member in cmu.chat.get_members(filter=enums.ChatMembersFilter.BANNED):
                await bot.unban_chat_member(cmu.chat.id, member.user.id)
                banned.append(member)
            
            if banned.__len__() == 0:
                await send_text(cmu.from_user, "blacklist_is_empty")
            else:
                await send_text(cmu.from_user, "successfully_cleared", count=banned.__len__())

        else:
            await send_text(cmu.from_user, "bot_need_ban_right")
        
        await cmu.chat.leave()


@bot.on_message(filters.command("start"))
async def on_command_start(_, msg: types.Message):
    await send_text(msg.from_user, "command_start")
