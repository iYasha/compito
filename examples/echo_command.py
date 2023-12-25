from compito.command import Command


class EchoCommand(Command):
    command_name = 'echo'
    help_text = 'Prints the given arguments.'

    def add_arguments(self, parser):
        parser.add_argument('message', type=str, default='Hello world', help='The message to print.')

    def handle(self, message: str, **kwargs) -> None:
        print(message)
