import unittest
from unittest.mock import MagicMock, patch
from compito.utils import get_commands

class TestGetCommands(unittest.TestCase):
    @patch('compito.utils.os')
    @patch('compito.utils.importlib')
    @patch('compito.utils.inspect')
    @patch('compito.utils.pkgutil')
    def test_get_commands(self, mock_pkgutil, mock_inspect, mock_importlib, mock_os):
        mock_os.walk.return_value = [('/path/to/package', ['subpackage'], ['module.py'])]
        mock_pkgutil.iter_modules.return_value = [(None, 'module', False)]

        mock_import_module = MagicMock()
        mock_importlib.import_module.side_effect = mock_import_module

        mock_getmembers = MagicMock()
        mock_inspect.getmembers.side_effect = mock_getmembers

        mock_command_class = MagicMock()
        mock_getmembers.return_value = [('Command', mock_command_class)]

        with patch('builtins.__import__'):
            commands = get_commands('/path/to/package')

        mock_os.walk.assert_called_once_with('/path/to/package')
        mock_pkgutil.iter_modules.assert_called_once_with(['/path/to/package'])
        mock_import_module.assert_called_once_with('module', fromlist='dummy')
        mock_inspect.getmembers.assert_called_once_with(mock_import_module(), predicate=inspect.isclass)
        mock_command_class.assert_called_once()

        self.assertEqual(commands, [mock_command_class])

if __name__ == '__main__':
    unittest.main()
