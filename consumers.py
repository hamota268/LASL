import json
from channels.generic.websocket import AsyncWebsocketConsumer
from lasl.ml_predictor import predict_from_keypoints

class TranslateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        keypoints = data.get('keypoints', [])
        result = predict_from_keypoints(keypoints)
        await self.send(text_data=json.dumps(result))