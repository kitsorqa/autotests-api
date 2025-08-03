import asyncio
import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for index in range(5):
            await websocket.send(f"Сообщение №{index + 1} пользователя: {message}", )


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket сервер был запущен")
    await server.wait_closed()


asyncio.run(main())
