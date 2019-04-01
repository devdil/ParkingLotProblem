import unittest
import os

class InteractiveTest(unittest.TestCase):

    def test_interactive(self):
        console_output = os.system('DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )";python $DIR/../../../main/main.py < $DIR/../interactive_input.txt')

        absolute_current_path = os.path.dirname(os.path.abspath(__file__))

        with open(absolute_current_path+'/../interactive_expected_ouput.txt', 'r') as f:
            expected_console_output = "".join(f.readlines())

            self.assertEqual(expected_console_output, console_output)


if __name__ == "__main__":
    unittest.main()