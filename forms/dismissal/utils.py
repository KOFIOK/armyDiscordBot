"""
Dismissal system utilities
Contains helper functions for message management and view restoration
"""

import discord
from discord import ui


async def send_dismissal_button_message(channel):
    """Send dismissal button message, avoiding duplicates using pinned messages."""
    
    # Check pinned messages first for dismissal message
    try:
        pinned_messages = await channel.pins()
        for message in pinned_messages:
            if (message.author == channel.guild.me and 
                message.embeds and
                message.embeds[0].title and
                "Рапорты на увольнение" in message.embeds[0].title):
                
                # Found pinned dismissal message, restore the view
                from .views import DismissalReportButton
                view = DismissalReportButton()
                try:
                    await message.edit(view=view)
                    print(f"Updated existing pinned dismissal message {message.id}")
                    return
                except Exception as e:
                    print(f"Error updating pinned dismissal message: {e}")
                    # If update fails, unpin and delete old message, create new one
                    try:
                        await message.unpin()
                        await message.delete()
                        print(f"Removed old pinned dismissal message {message.id}")
                    except:
                        pass
                    break
    except Exception as e:
        print(f"Error checking pinned messages for dismissal: {e}")
        # Create new message if none exists or old one couldn't be updated
    embed = discord.Embed(
        title="Рапорты на увольнение",
        description="Нажмите на кнопку ниже, чтобы отправить рапорт на увольнение.",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="Инструкция", 
        value="1. Нажмите на кнопку и заполните открывшуюся форму\n2. Нажмите 'Отправить'\n3. Ваш рапорт будет рассматриваться в течении __24 часов__.", 
        inline=False
    )
    
    from .views import DismissalReportButton
    view = DismissalReportButton()
    message = await channel.send(embed=embed, view=view)
    
    # Pin the new message for easy access
    try:
        await message.pin()
        print(f"Pinned new dismissal message {message.id}")
    except Exception as e:
        print(f"Error pinning dismissal message: {e}")


async def restore_dismissal_approval_views(bot, channel):
    """Restore approval views for existing dismissal report messages."""
    try:
        async for message in channel.history(limit=50):
            # Check if message is from bot and has dismissal report embed
            if (message.author == bot.user and 
                message.embeds and
                message.embeds[0].description and
                "подал рапорт на увольнение!" in message.embeds[0].description):
                
                embed = message.embeds[0]
                
                # Check if report is still pending (not approved/rejected)
                # We check if there's no "Обработано" field, which means it's still pending
                status_pending = True
                for field in embed.fields:
                    if field.name == "Обработано":
                        status_pending = False
                        break
                
                if status_pending:
                    # Extract user ID from footer if possible
                    # This is a fallback since we can't perfectly restore user_id
                    # but the view will still work for approval/rejection
                    from .views import DismissalApprovalView
                    view = DismissalApprovalView(user_id=None)
                      
                    # Edit message to restore the view
                    try:
                        await message.edit(view=view)
                        print(f"Restored approval view for dismissal report message {message.id}")
                    except discord.NotFound:
                        continue
                    except Exception as e:
                        print(f"Error restoring view for message {message.id}: {e}")
                        
    except Exception as e:
        print(f"Error restoring dismissal approval views: {e}")


async def restore_dismissal_button_views(bot, channel):
    """Restore dismissal button views for existing dismissal button messages using pinned messages."""
    try:
        # Check pinned messages first
        pinned_messages = await channel.pins()
        for message in pinned_messages:
            if (message.author == bot.user and 
                message.embeds and
                message.embeds[0].title and
                "Рапорты на увольнение" in message.embeds[0].title):
                
                # Add the view back to the pinned message
                from .views import DismissalReportButton
                view = DismissalReportButton()
                try:
                    await message.edit(view=view)
                    print(f"Restored dismissal button view for pinned message {message.id}")
                    return  # Found and restored pinned message
                except discord.NotFound:
                    continue
                except Exception as e:
                    print(f"Error restoring dismissal button view for pinned message {message.id}: {e}")
        
        # If no pinned message found, check recent history as fallback
        async for message in channel.history(limit=50):
            # Check if message is from bot and has dismissal button embed
            if (message.author == bot.user and 
                message.embeds and
                message.embeds[0].title and
                "Рапорты на увольнение" in message.embeds[0].title):
                
                # Add the view back to the message
                from .views import DismissalReportButton
                view = DismissalReportButton()
                try:
                    await message.edit(view=view)
                    print(f"Restored dismissal button view for message {message.id}")
                except discord.NotFound:
                    continue
                except Exception as e:
                    print(f"Error restoring dismissal button view for message {message.id}: {e}")                    
    except Exception as e:
        print(f"Error restoring dismissal button views: {e}")
