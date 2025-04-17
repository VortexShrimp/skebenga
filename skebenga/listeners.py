import coc
import os
import aiohttp
import discord

# Helper function to send a webhook.
async def send_embed_via_webhook(webhook_url: str, embed: discord.Embed) -> None:
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(webhook_url, session=session)
        await webhook.send(embed=embed)

@coc.ClanEvents.member_join()
async def on_clan_member_join(old_member: coc.ClanMember, new_member: coc.ClanMember) -> None:
    webhook_url: str = os.getenv('DISCORD_CLAN_WEBHOOK')
    if webhook_url is None:
        return

    embed = discord.Embed(colour=discord.Colour.green(),
                          title='Player Joined',
                          description=f'Player `{new_member.name} ({new_member.tag})` has joined the clan.')
    embed.set_thumbnail(url=new_member.clan.badge.url)

    frame += (
        f'`{'League:':<20}` `{new_member.league.name:<20.20}`\n'
        f'`{'Trophies:':<20}` `{new_member.trophies:<20}`\n'
        f'`{'Best Trophies:':<20}` `{new_member.best_trophies:<20}`\n'
        f'`{'War Stars:':<20}` `{new_member.war_stars:<20}`\n'
        f'`{'Attack Wins:':<20}` `{new_member.attack_wins:<20}`\n'
        f'`{'Defense Wins:':<20}` `{new_member.defense_wins:<20}`\n'
        f'`{'Capital Contribution':<20}` `{new_member.clan_capital_contributions:<20}`\n'
        )

    embed.add_field(name='Info',
                    value=frame,
                    inline=False)
    
    await send_embed_via_webhook(webhook_url, embed)

@coc.ClanEvents.member_leave()
async def on_clan_member_leave(old_member: coc.ClanMember, new_member: coc.ClanMember) -> None:
    webhook_url: str = os.getenv('DISCORD_CLAN_WEBHOOK')
    if webhook_url is None:
        return
    
    embed = discord.Embed(colour=discord.Colour.red(),
                          title='Player Left',
                          description=f'Player `{new_member.name} ({new_member.tag})` has left the clan.')
    embed.set_thumbnail(url=new_member.clan.badge.url)
    
    await send_embed_via_webhook(webhook_url, embed)

@coc.ClanEvents.level()
async def on_clan_level_changed(old_clan: coc.Clan, new_clan: coc.Clan) -> None:
    webhook_url: str = os.getenv('DISCORD_CLAN_WEBHOOK')
    if webhook_url is None:
        return
    
    embed = discord.Embed(colour=discord.Colour.yellow(),
                          title='Level Up',
                          description=f'The clan has leveled up from {old_clan.level} to {new_clan.level}.')
    embed.set_thumbnail(url=new_clan.badge.url)
    
    await send_embed_via_webhook(webhook_url, embed)

@coc.ClanEvents.description()
async def on_clan_description_changed(old_clan: coc.Clan, new_clan: coc.Clan) -> None:
    webhook_url: str = os.getenv('DISCORD_CLAN_WEBHOOK')
    if webhook_url is None:
        return
    
    embed = discord.Embed(colour=discord.Colour.yellow(),
                          title='Description Update')
    embed.set_thumbnail(url=new_clan.badge.url)

    embed.add_field(name='Old',
                    value=old_clan.description,
                    inline=False)

    embed.add_field(name='New',
                    value=new_clan.description,
                    inline=False)
    
    await send_embed_via_webhook(webhook_url, embed)

@coc.ClanEvents.badge()
async def on_clan_badge_changed(old_clan: coc.Clan, new_clan: coc.Clan) -> None:
    webhook_url: str = os.getenv('DISCORD_CLAN_WEBHOOK')
    if webhook_url is None:
        return
    
    embed = discord.Embed(colour=discord.Colour.yellow(),
                          title='Badge Update',
                          description='The clan\'s badge has been updated.')
    embed.set_thumbnail(url=new_clan.badge.url)

    await send_embed_via_webhook(webhook_url, embed)
