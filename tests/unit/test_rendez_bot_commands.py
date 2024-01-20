import subprocess
import unittest


class TestRendezBotCommands(unittest.TestCase):
    def test_call_command_line_help(self):
        command = ["rendez_bot --help"]
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
