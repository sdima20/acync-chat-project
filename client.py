import asyncio

from config import HOST, PORT, ENCODING

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