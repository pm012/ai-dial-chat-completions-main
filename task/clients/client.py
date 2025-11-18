import os
from aidial_client import Dial, AsyncDial

from dotenv import load_dotenv
from task.clients.base import BaseClient
from task.constants import DIAL_ENDPOINT
from task.models.message import Message
from task.models.role import Role


class DialClient(BaseClient):

    def __init__(self, deployment_name: str):
        super().__init__(deployment_name)
        load_dotenv()
        self.api_key = os.getenv("DIAL_API_KEY", "")
        self.base_url = os.getenv("DIAL_API_BASE", "")
        
        # Documentation: https://pypi.org/project/aidial-client/ (here you can find how to create and use these clients)
        # 1. Create Dial client
        dial_client = Dial(api_key=self.api_key, base_url=self.base_url)
        
        # 2. Create AsyncDial client
        async_dial_client = AsyncDial(api_key=self.api_key, base_url=self.base_url)

    def get_completion(self, messages: list[Message]) -> Message:
        #TODO:
        # 1. Create chat completions with client
        response = self.client.create_chat_completion(
            deployment_name=self.deployment_name,
            messages=[message.to_dict() for message in messages]
        )
        #    Hint: to unpack messages you can use the `to_dict()` method from Message object
        # 2. Get content from response, print it and return message with assistant role and content
        # 3. If choices are not present then raise Exception("No choices in response found")
        raise NotImplementedError

    async def stream_completion(self, messages: list[Message]) -> Message:
        #TODO:
        # 1. Create chat completions with async client
        #    Hint: don't forget to add `stream=True` in call.
        # 2. Create array with `contents` name (here we will collect all content chunks)
        # 3. Make async loop from `chunks` (from 1st step)
        # 4. Print content chunk and collect it contents array
        # 5. Print empty row `print()` (it will represent the end of streaming and in console we will print input from a new line)
        # 6. Return Message with assistant role and message collected content
        raise NotImplementedError
