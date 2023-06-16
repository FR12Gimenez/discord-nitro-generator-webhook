import string
import random
import time
import crayons
from discord_webhook import *

def send():
    webhook = DiscordWebhook(url=webhookurl, content="https://discord.gift/" + code) # First part of the generating.
    response = webhook.execute()

print("discord.gg/nlboosts")


# SETTINGS
webhookurl = 'OWN WEBHOOK' 
changewh = input("\nDo you want to change the webhook URL? \n\nIf you already set the webhook URL in the files enter N.\nIf not, enter Y and generate a new webhook URL.\n(Y/N) > ")
if changewh == "y":
    webhookurl = input("You have chosen to change the web hook url, paste it here and press enter. > ")

amount = 0
amount = input("\nHow many codes would you like to be sent to your server? \n> ")

print("{}".format(crayons.blue('\n'+ amount +' code(s) will be generated and sent!')))
print("{}".format(crayons.blue('Closing session...')))

### WEBHOOK SENDER

for x in range(1, int(amount) + 1):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    send() # Makes strings and sends them.
    print("{}".format(crayons.magenta('\n> Generated code: ' + code + '\n- Code Number: %d' % (x))))
    print("{}".format(crayons.green('- Code sent!')))
    time.sleep(1.65) # Cooldown

### CLOSING

print('\nAll the codes have been sent.')
time.sleep(5)
