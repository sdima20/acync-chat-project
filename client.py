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

    print("Message sent")

    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())