from cloudbot import hook
from cloudbot import blacklist
import requests
import lxml.html

lastURL = ""

def pullkill(url):
	global lastURL
	lastURL = url
	req = requests.get(url).text
	html = lxml.html.fromstring(req)
	desc = html.xpath("//meta[@name='twitter:description']/@content")
	return desc[0]

@hook.regex(r'(.*:)//(zkillboard.com|www.zkillboard.com)(:[0-9]+)?(.*)')
def zkb(match, nick, host):
	if blacklist.bl_ret(nick) or blacklist.bl_ret(host):
		return
	global lastURL
	if match.group(0).lower() in lastURL:
		return
	return pullkill(match.group(0).lower())
