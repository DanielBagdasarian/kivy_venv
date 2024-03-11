from hikkatl.utils import answer
from hikkatl.types import Message
from .. import loader

@loader.tds
class MyModule(loader.Module):
    """My module"""
    strings = {"name": "MyModule", "hello": "Hello world!"}

    @loader.command
    async def helloworld(self, message: Message):
        """Hello world"""
        await answer(message, self.strings("hello"))
