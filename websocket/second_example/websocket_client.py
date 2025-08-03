import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        for i in range(5):
            message = f"Hello, server №{i}"
            print(f"Отправка сообщения, содержимое: {message}")
            await websocket.send(message)

        response = await websocket.recv()
        print(f"Получен ответ от сервера: {response}")


asyncio.run(client())
