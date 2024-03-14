intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, test_guild=[1204606906337984513])
bot.remove_command('help')

emoji = "<:emoji_77:1215712871976009788>"
emoji1 = "<:crypto:1215729173029593129>"


connection = sqlite3.connect('server.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS `users_table` (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      cash INTEGER DEFAULT 0,
                      bank INTEGER DEFAULT 0,
                      rep INTEGER DEFAULT 0,
                      lvl INTEGER DEFAULT 1,
                      debt INTEGER DEFAULT 0,
                      crypto INTEGER DEFAULT 0,
                      server_id INTEGER
                  );""")
    
for guild in bot.guilds:
    for member in guild.members:
        if cursor.execute(f"SELECT id FROM  `users_table` WHERE id = {member.id}").fetchone() is None:
                cursor.execute(f"INSERT INTO `users_table` VALUES('{member}, {member.id}, 1, 0, 0, 1, 0, 0')")
                connection.commit()
            
        else:
            pass
            
    connection.commit()
    
cursor.execute("""CREATE  TABLE IF NOT EXISTS shop (
    role_id INT,
    id INT,
    cost BIGINT
    )""")
