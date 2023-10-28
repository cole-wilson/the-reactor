import os
import re
import time
import logging
import requests

logger = logging.getLogger('my-logger')
logger.setLevel(logging.DEBUG)

os.system('pip3 install python-Levenshtein')

from fuzzywuzzy import fuzz, process

try:
	from slack_bolt import App
except ModuleNotFoundError:
	os.system('pip3 install slack_bolt')
	from slack_bolt import App

from slack_sdk import WebClient, errors

client = WebClient(token=os.environ['TOKEN'])
emoji = list(client.emoji_list().data['emoji'].keys())
r = requests.get("https://a.slack-edge.com/bv1-9/gantry-vendors.c67bd4e.min.js")
emoji.extend(re.findall(r':i\.t\("(\w*?)"\)', r.content.decode()))



app = App(
	token=os.environ.get("TOKEN"),
	signing_secret=os.environ.get("SIGNING_SECRET")
)



@app.event("message")
def main(event):
	if event['channel'] in [
		"C0M8PUPU6"
	]: return
	if 'text' not in event: return
	# start_time = time.time()
	words = event['text'].split()
	for word in words:
		word = word.lower()
		word = re.sub(r"[^a-zA-Z0-9 -+]", "", word)
		candidates = []
		for e in emoji:
			ratio = fuzz.ratio(e, word)
			if ratio > 70:
				candidates.append((ratio, e))
				continue
		if len(candidates) < 1:
			print("NO MATCH", word, event['channel'])
			continue
		reaction = max(candidates, key=lambda i:i[0])[1]
		if word in emoji: reaction = word
		print(word, f":{reaction}:", event["channel"], sep="->")
		try:
			client.reactions_add(
				channel=event['channel'],
				timestamp=event['ts'],
				name=reaction
			)
		except errors.SlackApiError:
			pass
	# end_time = time.time() - start_time
	# print(end_time)

@app.event("reaction_added")
def handle_reaction_added_events(event):
	if event['user'] != 'U02A9RUSS3E' and event['reaction'] == 'react':
		ts = event['item']['ts']
		messages = client.conversations_history(
			channel = event['item']['channel']
		).data['messages']
		message = [*filter(
			lambda i: i['ts'] == ts,
			messages
		)][0]
		main({
			"channel": event['item']['channel'],
			"ts": ts,
			"text": message['text']
		})

	elif event['user'] != 'U02A9RUSS3E' and event['reaction'] == 'x':
		print(event)
		reacted = client.reactions_get(
			channel=event['item']['channel'],
			timestamp=event['item']['ts']
		).data['message']['reactions']
		reacted = filter(lambda i: 'U02A9RUSS3E' in i['users'], reacted)
		reacted = list(map(lambda i: i['name'], reacted))
		print(reacted)
		for reaction in reacted:
			client.reactions_remove(
				name = reaction,
				timestamp = event['item']['ts'],
				channel=event['item']['channel'],
			)
		

if __name__ == "__main__":
	app.start(port=int(os.environ.get("PORT", 3000)))