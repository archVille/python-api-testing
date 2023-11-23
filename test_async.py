import pytest
import asyncio
import websockets

async def test_websocket():
    uri = "wss://example.com/websocket"
    async with websockets.connect(uri) as websocket:
        await websocket.send("This is a test")
        response = await websocket.recv()
        assert response == "This is a test"