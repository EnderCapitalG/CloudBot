from cloudbot import hook
from cloudbot import blacklist

@hook.command('bladd', permissions=["botcontrol"])
@hook.command('blacklist', permissions=["botcontrol"])
def blacklist_add(text):
	retv = blacklist.bl_add(text)
	if retv is True:
		return "Added."
        else:
                return "Already exists."

@hook.command('bldel', permissions=["botcontrol"])
def blacklist_del(text):
	retv = blacklist.bl_del(text)
	if retv is True:
		return "Removed."

@hook.command('blcheck', permissions=["botcontrol"])
def blacklist_check(text):
	retv = blacklist.bl_ret(text)
	if retv is True:
		return True
	else:
		return False
