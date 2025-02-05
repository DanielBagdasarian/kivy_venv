from hikkatl.types import Message
from .. import loader, utils


@loader.tds
class MyModule(loader.Module):
    """My module test"""
    strings = {"name": "MyModuleTest", "hello": "Hello world!"}
    strings_ru = {"hello": "Привет мир!"}
    strings_es = {"hello": "¡Hola mundo!"}
    strings_de = {"hello": "Hallo Welt!"}

    @loader.command(
        ru_doc="Привет мир!",
        es_doc="¡Hola mundo!",
        de_doc="Hallo Welt!",
        # ...
    )
    async def helloworldtest(self, message: Message):
        """Hello world test"""
        await utils.answer(message, self.strings("hello"))
