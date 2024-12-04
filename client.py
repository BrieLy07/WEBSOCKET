import asyncio
import websockets

async def communicate():
    uri = "ws://localhost:8765"  # Dirección del servidor
    async with websockets.connect(uri) as websocket:
        # Enviar un mensaje al servidor
        message = input("Escribe un mensaje para enviar al servidor: ")
        await websocket.send(message)

        # Recibir la respuesta del servidor
        response = await websocket.recv()
        print(f"Servidor respondió: {response}")

if __name__ == "__main__":
    asyncio.run(communicate())
