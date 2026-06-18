import asyncio

from config import HOST, PORT, BUFFER_SIZE, ENCODING

async def handle_client(reader, writer):
    """
    Handles one connected client
    """

    print("Client connected")

    #first message contains username

    username_data = await reader.read(BUFFER_SIZE)

    username = username_data.decode(ENCODING)

    print("User connected:", username)

    #persistent connection
    while True:
        
        print("Waiting...")

        data = await reader.read(BUFFER_SIZE)
        
        if not data:
            break

        message = data.decode(ENCODING)

        print(f"{username} : {message}")
    
    print("Connection closed")

    writer.close()

    await writer.wait_closed()


async def main():
    """
    creates TCP server
    """

    server = await asyncio.start_server(
        handle_client,
        HOST,
        PORT
    )

    print(f"Server started on {HOST}:{PORT}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())