from compito.command import AsyncCommand
from compito.scheduler import Scheduler


class AsyncEchoCommand(AsyncCommand):
    command_name = 'async_echo'
    help_text = 'Prints the given arguments.'
    scheduler = Scheduler.every_hour()

    def add_arguments(self, parser):
        parser.add_argument(
            '-m', '--message', dest='message', type=str, default='Hello world', help='The message to print.'
        )

    async def handle(self, message: str, **kwargs) -> None:
        print(message)
