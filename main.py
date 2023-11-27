from telethon import TelegramClient, events

api_id = '20865934'  # Replace with your api_id
api_hash = '26f2be56f24fffb631180d7c07b92ea4'  # Replace with your api_hash
phone_number = '+77025344128'  # Replace with your phone number

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone_number)
        try:
            await client.sign_in(phone_number, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    # Now you can use client to send messages, interact, etc.

with client:
    client.loop.run_until_complete(main())
async def send_message():
    await client.send_message('bushpulbek', 'Hello! This is a testerf message.')
    
with client:
    client.loop.run_until_complete(send_message())
