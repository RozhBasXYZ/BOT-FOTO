import requests, re, bs4, json, os, time, random
parser = bs4.BeautifulSoup
ses = requests.Session()
os.system("clear")

coki = input("[!] cookie : ")
token = re.search('(\["EAAG\w+)', ses.get("https://business.facebook.com/business_locations",cookies={"cookie": coki}).text).group(1).replace('["','')
os.system("clear")
def waktu():
    total_second = 5 * 60 + 0
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'\r[!] delay  : 00:{mins:02d}:{secs:02d} menit', end='')
        time.sleep(1)
        total_second -= 1

def get_id():
	try:
		main = parser(ses.get(f"https://m.facebook.com/home.php?",cookies={"cookie": coki}).text, "html.parser")
		for x in main.find_all("a",href=True):
			if "photo.php" in str(x):
				id_post = str(x.get("href")).split("=")[1].replace("&id","")
				id_akun = str(x.get("href")).split("=")[2].replace("&set","")
				nama = ses.get(f"https://graph.facebook.com/{id_akun}?access_token={token}",cookies={"cookie": coki}).json()["name"].upper()
				break
	except: id_post = ""; nama = ""; id_akun = ""
	return id_post, nama, id_akun

def komen():
	try:
		id, nama, uid = get_id()
		date = {
		    "FileFormat": "4",
		    "FontSize": "70",
		    "Integer12": "on",
		    "Integer13": "on",
		    "Integer9": "0",
		    "LogoID": "5",
		    "Text": nama
		}
		foto = "http"+ses.post("https://cooltext.com/PostChange",data=date).json()["renderLocation"].split("https")[1]
		bz = ses.post(f"https://graph.facebook.com/{id}/comments?method=post&attachment_url={foto}&message=@[{uid}:]&access_token={token}",cookies={"cookie":coki}).json()
		if "id" in str(bz):
			print(f"\r[!] status : sukses\n[!] link   : m.facebook.com/{uid}_{id}\n[!] foto   : {foto} ")
			waktu(); print("\r")
			print("-"*30)
	except Exception as e:pass

while True: komen()