import asyncio
import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Было получено сообщение: {message}")
        response = f"Сервер получил: {message}"
        await websocket.send(response)


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket сервер был запущен")
    await server.wait_closed()


asyncio.run(main())
