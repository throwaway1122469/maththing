import discord
from discord.ext import commands
import math
import os
bot = commands.Bot(case_insensitive=True, command_prefix='$')


@bot.command()
async def chei(ctx):
    await ctx.send('sqrt = radacina patrata\nx^n = x la puterea n \nx*n = x inmultit cu n\nx/n = x pe n (fractie)')

@bot.command(aliases = ['eq'])
async def qd(ctx, a:int, b:int, c:int):
    await ctx.send(f'{a}x^2 + {b}x + {c} = 0')
    await ctx.send(f' a = {a}, b = {b}, c = {c}')
    deltaBonus = 4*a*c
    if deltaBonus < 0:
        deltaBonus = '(' + str(4*a*c) + ')'
    delta = int(b**2 - 4*a*c)
    await ctx.send(f'Delta = b^2 - 4ac => {b}^2 - 4\*{a}\*{c} => {b**2} - {deltaBonus} => {delta}')
    if delta == 0:
        l = b**2
        d = 2*a 
        x = l/d
        return await ctx.send(f'Delta este egal cu 0, x este b^2/2a => x = {b}^2/2*{a} => x = {l}/{d} =>  x = {x}')
    if delta < 0:
        return await ctx.send('Delta este mai mic de 0, S = multimea vida')
    if delta > 0:
        r = -(b)
        g = math.sqrt(delta)
        h = 2*a
        lol = r-g
        xOne = lol/h
        lel = r+g
        xTwo = lel/h
        await ctx.send(f'Delta esta mai mare de zero,\nx1 => -b - sqrt(delta)/2a => -({b}) - sqrt({delta}) / 2\*{a} => {r}-{g}/{h} => x = {r-g}/{h} => x =  {xOne}\nx2 => -b + sqrt(delta)/2a => -({b}) + sqrt({delta}) / 2\*{a} => {r}+{g}/{h} => x = {r+g}/{h} => x =  {xTwo}')
    
bot.run(os.getenv('TOKEN'))
