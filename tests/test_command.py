import sys
import unittest
from argparse import ArgumentParser

from command_executor.command import Command
from command_executor.scheduler import Scheduler, _Scheduler


class EchoCommand(Command):
    command_name = 'echo'
    scheduler = Scheduler.every_minute()

    def handle(self, *args, **kwargs) -> None:
        sys.stdout.write(kwargs['message'])

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument('-m', '--message', type=str)


class TestCommand(unittest.TestCase):

    def setUp(self):
        self.echo_command = EchoCommand()

    def test_scheduler(self):
        assert isinstance(self.echo_command.scheduler, _Scheduler)

