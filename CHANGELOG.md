## Changelog

## 1.0.9
Added in my own code since the main bot is no longer actively maintained.
 * agdq.py - Works for both AGDQ and SGDQ events, polls the current game, upcoming games and has a basic search. Was one of the first scripts I really wrote out so it's probably terrible.
 * NewComic.py - This has been ported from one bot to another then another, I finally rewrote it somewhat (cleaned up variable names) and added in some more features like drop shadows on text and random backgrounds/characters.
 * runescape.py - Polls for full player count from the runescape server, I might look into trying to parse each type of player (new/old RS) apart
 * tag.py - Add tags to keywords, can call up a keyword by .tags word or ?word
 * tfw.py - Scrapes channels for any use of "tfw" and then grabs the sentence and stores it for later recallying with .tfw
 * Title.py - Gets the title of webpages except those marked in the source to skip over, as other plugins generally handle those.

 * CORE CHANGE: Added a blacklist feature, currently dependant on botcontrol flag on a user. This includes cloudbot/blacklist.py and also plugins/blacklist_pl.py; you can add both nicks and addresses to the database and check against both in a function.

### 1.0.8
This update is pretty big. Be warned.
 * Improved flip command.
 * Added new time command that gets time for location.
 * Added locate command that locates a place on Google Maps.
 * Change weather command to use new location API from the two above.
 * Added more kill messages.
 * Revamp lastfm with more commands and better memory.
 * Add new poll command. Still not perfect.
 * Replaced old dictionary plugin with new Wordnik plugin.
 * Revamped Soundcloud command.
 * Revamped chatbot command.
 * Switched back to google search.
 * Added new issafe plugin.
 * And a whole lot of minor tweaks and fixes.

### 1.0.7.1
 * Security fixes.

### 1.0.7
 * Added new "Would you rather" plugin.

### 1.0.6
 * Added pig latin translator, requires new *nltk* module
 * Added reminder command
 * Added new periodic hook (does not support reloading properly yet, so use with caution)
 * Added priority sorting to sieve hooks
 * Started work on new documentation for 1.1
 * Did some minor internal refactoring

**1.0.5** - Fix geoip for queries with no region, fix youtube bug, add flip command

**1.0.4** - Adjust ratelimiter cleanup task, add octopart API key, fix brainfuck, sort mcstatus output.

**1.0.3** - More minor changes to plugins, fixed rate-limiting properly, banished SCP to CloudBotIRC/Plugins, added wildcard support to permissions (note: don't use this yet, it's still not entirely finalized!)

**1.0.2** - Minor internal changes and fixes, banished minecraft_bukget and worldofwarcraft to CloudBotIRC/Plugins

**1.0.1** - Fix history.py tracking

**1.0.0** - Initial stable release
