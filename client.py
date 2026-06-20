import asyncio

from config import HOST, PORT, ENCODING, BUFFER_SIZE

async def receive_messages(reader):

    while True:
        try: #!!!!!!!

            data = await reader.read(BUFFER_SIZE)

            if not data:
                break

            print(data.decode(ENCODING))
        
        except: #!!!!!!
            break

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

async def send_messages(writer): #!!!!!!!!!!!
    """
    Send messages to server
    """

    while True:

        message = await asyncio.to_thread(
            input,
            "> "
        )

        if message.lower() == "exit":
            break

        writer.write(
            message.encode(ENCODING)
        )

        await writer.drain()

    writer.close()

    await writer.wait_closed()


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

    await writer.drain()

    asyncio.create_task(receive_messages(reader))
    
    #Send multiply messages

    receive_task = asyncio.create_task(
        receive_messages(reader)
    )

    send_task = asyncio.create_task(
        send_messages(writer)
    )

    await asyncio.gather(
        receive_task,
        send_task
    )

    # while True:

    #     message = input("> ")

    #     if message == 'exit':
    #         break

    #     writer.write(message.encode(ENCODING))

    #     await writer.drain()
    
    # writer.close()

    # await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())