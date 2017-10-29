from cloudbot import hook
import sqlite3
from cloudbot import blacklist

tfwdb = "data/tfw.db"

@hook.regex(r'(?i)^tfw(.*)')
def tfwadd(match, nick, host):
	if blacklist.bl_ret(nick) or blacklist.bl_ret(host):
		return
	global tfwdb
	matchtext = match.group(0)
	db = sqlite3.connect(tfwdb)
	cur = db.cursor()
	query = "CREATE TABLE IF NOT EXISTS tfw (text TEXT);"
	cur.execute(query)
	print("Adding tfw:", matchtext)
	cur.execute("INSERT INTO tfw VALUES(?)", (matchtext,))
	db.commit()
	db.close()

@hook.command('tfw')
def tfwgrab(nick, host):
	if blacklist.bl_ret(nick) or blacklist.bl_ret(host):
		return
	global tfwdb
	db = sqlite3.connect(tfwdb)
	cur = db.cursor()
	query = "SELECT * FROM tfw ORDER BY RANDOM() LIMIT 1;"
	cur.execute(query)
	ret = cur.fetchone()[0]
	db.close()
	return ret

@hook.command('deltfw', permissions=["botcontrol"])
def deletetfw(text):
	global tfwdb
	db = sqlite3.connect(tfwdb)
	cur = db.cursor()
	query = "DELETE FROM tfw WHERE text IS ?;"
	cur.execute(query, (text,))
	db.commit()
	db.close()
	return "Removed."

@hook.command('counttfw', permissions=["botcontrol"])
def counttfw():
	global tfwdb
	db = sqlite3.connect(tfwdb)
	cur = db.cursor()
	query = "SELECT * FROM tfw;"
	cur.execute(query)
	x = 0
	obj = cur.fetchall()
	for item in obj:
		x += 1
	db.close()
	return x
