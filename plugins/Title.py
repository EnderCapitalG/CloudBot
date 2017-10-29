#Made for cloudbot
#Created by ender.capitalg@gmail.com

import requests
from lxml.html import fromstring
from cloudbot import blacklist
from cloudbot import hook

#basic spam protection
lastURL = ''

header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36' }

@hook.regex(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
def titlec(match, nick, host):
	global lastURL, header
	matchtext = match.group(0).lower()
	if blacklist.bl_ret(nick) or blacklist.bl_ret(host):
		return
	if 'twitch.tv' in matchtext or 'zkillboard' in matchtext:
		return
	elif 'youtube.com' in matchtext or 'youtu.be' in matchtext:
		return
	elif 'twitter.com' in matchtext or 'https://t.co' in matchtext:
		return
	elif 'ebin.pw' in matchtext or 'csgoani.me' in matchtext:
		return
	elif 'xkcd.com' in matchtext:
		return
	
	#to discard pictures
	picture = matchtext.rsplit('.',1)[-1]
	if 'jpg' in picture or 'png' in picture or 'gif' in picture or 'webm' in picture or 'mp4' in picture or 'webm' in picture:
		return

	if matchtext in lastURL:
		return
	lastURL = matchtext
	req = requests.get(match.group(0), headers=header)
	tree = fromstring(req.content)
	title = tree.findtext('.//title')
	title = title.replace('\n', '').replace('\r', '').lstrip(' ')
	return title
