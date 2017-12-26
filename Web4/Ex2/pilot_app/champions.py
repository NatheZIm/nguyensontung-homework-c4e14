from mlab import mlab_connect
from models.champ import Champ
from random import choice,randint

mlab_connect()

champ_name = [

    "Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "Aurelion Sol", "Azir",
    "Bard", "Blitzcrank", "Brand", "Braum",
    "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki",
    "Darius", "Diana", "Dr. Mundo", "Draven",
    "Ekko", "Elise", "Evelynn", "Ezreal","Fiddlesticks", "Fiora", "Fizz",
    "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves",
    "Hecarim", "Heimerdinger","Illaoi", "Irelia", "Ivern",
    "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx",
    "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'zix", "Kindred", "Kled", "Kog'Maw",
    "LeBlanc", "Lee Sin", "Leona", "Lissandra", "Lucian", "Lulu", "Lux",
    "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana",
    "Nami", "Nasus", "Nautilus", "Nidalee", "Nocturne", "Nunu",
    "Olaf", "Orianna", "Ornn","Pantheon", "Poppy","Quinn",
    "Rakan", "Rammus", "Rek'Sai", "Renekton", "Rengar", "Riven", "Rumble", "Ryze",
    "Sejuani", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Syndra",
    "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch","Udyr", "Urgot",
    "Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor", "Vladimir", "Volibear","Warwick", "Wukong",
    "Xayah", "Xerath", "Xin Zhao","Yasuo", "Yorick","Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"
]

champ_role = ["Assassin", "Maskman", "Mage", "Support", "Tank", "Fighter"]


for i in champ_name:
    champ = Champ(
        image = i + ".png",
        name = i,
        role = choice(champ_role)
    )
    champ.save()
