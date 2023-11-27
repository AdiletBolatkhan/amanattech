from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
import asyncio

# First account
api_id_1 = '20865934'
api_hash_1 = '26f2be56f24fffb631180d7c07b92ea4'
phone_number_1 = '+77025344128'
client1 = TelegramClient('session_name_1', api_id_1, api_hash_1)

# Second account
api_id_2 = '25525581'
api_hash_2 = '8264205a15a7424a32e2054806d5f734'
phone_number_2 = '+77763855554'
client2 = TelegramClient('session_name_2', api_id_2, api_hash_2)

async def authorize_client(client, phone_number):
    await client.start(phone=phone_number)
    print("Client Created")
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        try:
            await client.sign_in(phone_number, input('Enter the code for ' + phone_number + ': '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password for ' + phone_number + ': '))

async def send_message_from_client1():
    await authorize_client(client1, phone_number_1)
    await asyncio.sleep(5)  # Wait for 5 seconds before sending the message
    await client1.send_message('bushpulbek', 'Hello! This is a testerf message.')

async def send_message_from_client2():
    await authorize_client(client2, phone_number_2)
    await client2.send_message('bushpulbek', 'heyyy')

async def main():
    await asyncio.gather(
        send_message_from_client1(),
        send_message_from_client2()
    )

with client1, client2:
    client1.loop.run_until_complete(main())
