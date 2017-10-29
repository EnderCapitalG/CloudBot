import sqlite3

bldb = "data/Blacklist.db"

def bl_add(string):
	global bldb
        if bl_ret(string):
                return False

	db = sqlite3.connect(bldb)
	cur = db.cursor()
	query = "CREATE TABLE IF NOT EXISTS blist (nick TEXT);"
	cur.execute(query)

	query = "INSERT INTO blist VALUES (?);"
	cur.execute(query, (string,))
	db.commit()
	db.close()
	return True

def bl_del(string):
	global bldb
	db = sqlite3.connect(bldb)
	cur = db.cursor()
	query = "DELETE FROM blist WHERE nick IS ? COLLATE NOCASE;"

	cur.execute(query, (string,))
	db.commit()
	db.close()
	return True

#return true or false if nick in db
def bl_ret(string):
	global bldb
	db = sqlite3.connect(bldb)
	cur = db.cursor()
	query = "SELECT * FROM blist;"
	cur.execute(query)
	nicks = cur.fetchall()

	for nick in nicks:
		if string.lower() in nick[0].lower():
			return True

	db.close()
	return False

#return array of all nicks in blacklist
def bl_list():
	return "Nothing here yet~"
