from src.main.exceptions.commandlineexception import *
import unittest

class CommandLineExceptionTest(unittest.TestCase):

    def test_self(self):

        with self.assertRaises(UnsupportedCommandException):
            raise UnsupportedCommandException("message")


if __name__ == "__main__":
    unittest.main()