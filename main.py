from characterai import PyCAI
import config
import transs
import asyncio

banner = """
╔═╗╔═╗╦   ╦ ╦╔═╗╦╔═╗╦ ╦
║  ╠═╣║───║║║╠═╣║╠╣ ║ ║
╚═╝╩ ╩╩   ╚╩╝╩ ╩╩╚  ╚═╝
"""

clinetmain = PyCAI(config.Owner_ID)
char1 = config.bot_id_chat1
char2 = config.bot_id_chat2

def chat1():
    client = clinetmain
    chat = client.chat.get_chat(char1)

    if config.debug:
        print("[dbg] Successful Import of PYCAI and BOTID!")

    participants = chat['participants']
    tgt = participants[0]['user']['username'] if not participants[0]['is_human'] else participants[1]['user']['username']

    while True:
        if config.translate:
            messagein = input("You: ")
            message = transs.translain(messagein)
            data = client.chat.send_message(chat['external_id'], tgt, message)

            name = data['src_char']['participant']['name']
            text = data['replies'][0]['text']
            tted = transs.translaout(text)

            print(f"{name}: {tted}")
        else:
            message = input("You: ")
            data = client.chat.send_message(chat['external_id'], tgt, message)

            name = data['src_char']['participant']['name']
            text = data['replies'][0]['text']
            print(f"{name}: {text}")


async def chat2():
    print("[@] Wrong Way Buddy?, Chat2 Is Under construction")


if __name__ == "__main__":
    try:
        print(banner)
        if config.chat1:
            chat1()
        else:
            asyncio.run(chat2())

        if not config.chat2 or not config.chat1:
            print("[@] Make Sure You Enable Chat1/Chat2\n This My Reaction: (*_*)?")
        if config.chat2 or config.chat1:
            print("[@] Make sure you ONLY Activate ONE of Chat1/Chat2\n This My Reaction: (*_*)?")

    except Exception as e:
        print("[@] We Found Error:", e)
