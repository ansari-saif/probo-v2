from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
import uvicorn

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store active connections per room
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, room_id: str):
        await websocket.accept()
        if room_id not in self.active_connections:
            self.active_connections[room_id] = []
        self.active_connections[room_id].append(websocket)

    def disconnect(self, websocket: WebSocket, room_id: str):
        if room_id in self.active_connections:
            if websocket in self.active_connections[room_id]:
                self.active_connections[room_id].remove(websocket)
            if not self.active_connections[room_id]:  # Remove room if empty
                del self.active_connections[room_id]

    async def broadcast(self, message: str, room_id: str):
        if room_id in self.active_connections:
            to_remove = []
            for connection in self.active_connections[room_id]:
                try:
                    await connection.send_text(message)
                except WebSocketDisconnect:
                    to_remove.append(connection)
                except Exception as e:
                    print(f"Error sending message: {e}")
                    to_remove.append(connection)

            # Clean up disconnected connections
            for conn in to_remove:
                self.disconnect(conn, room_id)

manager = ConnectionManager()

# WebSocket Endpoint with room support
@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await manager.connect(websocket, room_id)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Room {room_id}: {data}")
            await manager.broadcast(data, room_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, room_id)
        await manager.broadcast("Client left the room", room_id)
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Ensure disconnection on exit
        manager.disconnect(websocket, room_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
