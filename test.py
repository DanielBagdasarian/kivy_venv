from hikkatl.types import Message
from .. import loader, utils


@loader.tds
class MyModule(loader.Module):
    """My module"""
    strings = {
        "name": "MyModuleTest",
        "hello": "Hello world!"
    }

    async def test(self, message: Message):
        """Hello world test"""
        await utils.answer(message, strings["hello"])
