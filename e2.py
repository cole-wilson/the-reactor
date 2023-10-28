import os
import requests

os.chdir('emoji')
files = os.listdir('.')
for c, i in enumerate(files):
	name = i.strip('.png')
	r = requests.post(
		"https://hackclub.slack.com/api/emoji.add",
		files = {
			"image": open(name+'.png','rb').read(),
			"name": name,
			"mode": "data",
			"token":"XXXX",
			"_x_reason": "customize-emoji-add",
			"_x_mode": "online",
		},
		headers={}
	)
	print(f"{c}/{len(files)}", name, r.content)
	print()

"cookie":"b=.2ccrjogj240kta54ssajkwg90; shown_ssb_redirect_page=1; shown_download_ssb_modal=1; show_download_ssb_banner=1; no_download_ssb_banner=1; OptanonConsent=isIABGlobal=false&datestamp=Tue+Aug+03+2021+18%3A04%3A46+GMT-0700+(Pacific+Daylight+Time)&version=6.12.0&hosts=&consentId=2045d8c1-2fb6-4710-b879-e8bc76ea2d91&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false&geolocation=US%3BWA; OptanonAlertBoxClosed=2021-08-04T01:04:46.355Z; utm=%7B%22utm_source%22%3A%22in-prod%22%2C%22utm_medium%22%3A%22inprod-customize_link-slack_me%22%7D; d-s=1628098043"

{
	"d": "RoWpllkY1w9pw1j37a%2BbqnbPVbzDsmrOm%2FYIxBRfrQZFYg%2F7gBAGCizyEVX0TP474fAzD7PhoxDRJeui0Oz%2B9jAU1ZY360qf7HU2DcwGGKKeWis6epNQlHPYu6%2FZbh83GqwxbMmkU65fmhZtYsnIO8B0e%2FpZJH4IXokwSVSxmjk9JDiMUh92ww%3D%3D",
	"lc": "1627516039",
	"b": ".2ccrjogj240kta54ssajkwg90",
	"shown_ssb_redirect_page": "1",
	"shown_download_ssb_modal": "1",
	"show_download_ssb_banner": "1",
	"no_download_ssb_banner": "1",
	"OptanonConsent": "isIABGlobal": "false&datestamp": "Tue+Aug+03+2021+18%3A04%3A46+GMT-0700+(Pacific+Daylight+Time)&version": "6.12.0&hosts": "&consentId": "2045d8c1-2fb6-4710-b879-e8bc76ea2d91&interactionCount": "1&landingPath": "NotLandingPage&groups": "C0004%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent": "false&geolocation": "US%3BWA",
	"OptanonAlertBoxClosed": "2021-08-04T01:04:46.355Z",
	"utm": "%7B%22utm_source%22%3A%22in-prod%22%2C%22utm_medium%22%3A%22inprod-customize_link-slack_me%22%7D",
	"d-s": "1628098043"
 }
}
