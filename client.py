import asyncio

from config import HOST, PORT, ENCODING, BUFFER_SIZE

async def receive_messages(reader):

    while True:

        data = await reader.read(BUFFER_SIZE)

        if not data:
            break

        print(data.decode(ENCODING))

async def main():
    """
    Connect to server and send one message
    """

    reader, writer = await asyncio.open_connection(
        HOST,
        PORT
    )

    print("Connected to server")

    username = input("Enter your username: ")

    writer.write(
        username.encode(ENCODING)
    )

    await writer.drain() ##!!!!!

    asyncio.create_task(receive_messages(reader))
    
    #Send multiply messages

    while True:

        message = input("> ")

        if message == 'exit':
            break

        writer.write(message.encode(ENCODING))

        await writer.drain()
    
    writer.close()

    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())