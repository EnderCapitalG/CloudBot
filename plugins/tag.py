import sqlite3
from cloudbot import hook
from cloudbot import blacklist

tagdb = "data/Tag.db"

#for regex triggers
def syncDB():
	global tagdb
	db = sqlite3.connect(tagdb)
	cur = db.cursor()
	query = "SELECT * FROM tags;"
	cur.execute(query)
	table = cur.fetchall()

	db.close()
	global tagName
	tagName = table
	return table

tagName = syncDB()

def addtoDB(text):
	global tagdb
	db = sqlite3.connect(tagdb)
	cur = db.cursor()
	Name = text.split(' ', 1)[0]
	Tag = text.split(' ', 1)[1]
	Name = Name.replace('"', r'\"')
	Tag = Tag.replace('"', r'\"')
	#make sure it's not tagged
	query = "SELECT tags FROM tags WHERE name IS ? COLLATE NOCASE;"
	cur.execute(query, (Name,))
	table = cur.fetchall()
	for item in table:
		if Tag in item[0]:
			return 1

	query = "INSERT INTO tags VALUES (?, ?);"
	cur.execute(query, (Name, Tag))
	db.commit()
	db.close()
	syncDB()
	print("Added to tag %s: %s" % (Name, Tag))
	return 0

def delfromDB(name, text):
	global tagdb
	db = sqlite3.connect(tagdb)
	cur = db.cursor()
	name.replace('"', '\"')
	text.replace('"', '\"')
	query = "SELECT tags FROM tags WHERE name IS ? COLLATE NOCASE;"
	cur.execute(query, (name,))
	table = cur.fetchall()

	for item in table:
		if text in item[0]:
			query = "DELETE FROM tags WHERE name IS ? AND tags IS ?;"
			cur.execute(query, (name, text))
			db.commit()

	db.close()
	syncDB()
	print("Deleting from tag %s: %s" % (name, text))
	return 0

def getfromDB(text):
	global tagdb
	db = sqlite3.connect(tagdb)
	cur = db.cursor()
	text.replace('"', '\"')
	query = "SELECT tags FROM tags WHERE name IS ? COLLATE NOCASE;"
	cur.execute(query, (text,))
	table = cur.fetchall()
	retv = ""
	i = 0
	for item in table:
		retv += item[0]
		if i + 1 is not len(table):
			retv += ", "
		i += 1

	db.close()
	if retv is "" or retv is None:
		return 1
	return retv

@hook.command('tag')
def setTag(text, nick, host):
	if text is None or text is "":
		return
	if blacklist.bl_ret(nick) or blacklist.bl_ret(host):
		return
	if addtoDB(text) is 0:
		return "Tag added."
	return "Tag already exists."

@hook.command('tags')
def getTag(text, nick, host):
	if blacklist.bl_ret(nick) or blacklist.bl_ret(host):
		return
	retv = getfromDB(text)
	if retv is 1:
		return "No tags found for: " + text

	return "Tags for " + text + ": " + retv

#this is for searching by TAG, not keyword
@hook.command('tagged')
def getTagged(text, nick, host):
	if blacklist.bl_ret(nick) or blacklist.bl_ret(host):
		return
	global tagName
	retv = ""
	listv = []
	i = 0
	for item in tagName:
		if text.lower() == item[1].lower():
			listv.append(item[0])
	for item in listv:
		retv += item
		if i + 1 is not len(listv):
			retv += ", "
		i += 1
	if retv is "":
		return
	return "Tagged " + text + ": " + retv

@hook.command('untag')
def remTag(text, nick, host):
	if blacklist.bl_ret(nick) or blacklist.bl_ret(host):
		return
	result = delfromDB(text.split(' ',1)[0], text.split(' ',1)[1])
	if result is 0:
		return "Tag removed."
	return "Tag doesn't exist."

@hook.regex(r'\?(.*)$')
def regTag(match, nick, host):
	if blacklist.bl_ret(nick) or blacklist.bl_ret(host):
		return
	matchtext = match.group(0).lower()
	tag = matchtext.split('?',1)[-1]
	if tag is None:
		return
	retv = getfromDB(tag)
	if retv is 1:
#		return "No tags found for: " + tag
		#silently fail instead
		return

	return "Tags for " + tag + ": " + retv

@hook.command('droptags', permissions=["botcontrol"])
def dropAll(text):
	return "test"

@hook.command('droptagDB', permissions=["botcontrol"])
def dropTagDB():
	global tagdb
	db = sqlite3.connect(tagdb)
	cur = db.cursor()
	query = "DROP TABLE IF EXISTS tags"
	cur.execute(query)
	db.commit()

	query = "CREATE TABLE tags(name TEXT, tags TEXT);"
	cur.execute(query)
	db.commit()
	db.close()
	return "Table dropped."
