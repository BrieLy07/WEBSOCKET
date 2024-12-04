import asyncio
import websockets

async def echo(websocket, path):
    try:
        async for message in websocket:
            print(f"Mensaje recibido: {message}")
            # Envía una respuesta al cliente
            await websocket.send(f"Servidor: Recibí tu mensaje -> {message}")
    except websockets.exceptions.ConnectionClosedOK:
        print("Conexión cerrada correctamente.")
    except Exception as e:
        print(f"Error inesperado: {e}")

async def main():
    print("Iniciando servidor en ws://localhost:8765...")
    async with websockets.serve(echo, "localhost", 8765):
        print("Servidor WebSocket corriendo y esperando conexiones.")
        await asyncio.Future()  # Mantiene el servidor activo

if __name__ == "__main__":
    asyncio.run(main())
