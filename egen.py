import os
import shutil

# try:
# 	from slack_bolt import App
# except ModuleNotFoundError:
# 	os.system('pip3 install slack_bolt')
# 	from slack_bolt import App

# from slack_sdk import WebClient, errors

# client = WebClient(token=os.environ['TOKEN'])
# emoji = client.emoji_list().data['emoji']
# for i in filter(lambda i: 'alphabet-white-' in i, emoji):
# 	os.system(f"wget {emoji[i]} -O emoji/{i.replace('alphabet-white-', '')}_1.png")
os.chdir('emoji')
for c1, i in enumerate(list(os.listdir('.'))):
	for n in range(2, 401):
		print(i, n)
		try:
			shutil.copy(i, i[:-5] + str(n) + '.png')
		except:
			pass
