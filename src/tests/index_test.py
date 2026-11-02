import runpy
import unittest
from unittest.mock import patch


class TestIndex(unittest.TestCase):
    def test_paohjelma_suoritetaan_loppuun(self):
        with patch("builtins.print") as mock_print:
            runpy.run_module("index", run_name="__main__")

        self.assertGreater(mock_print.call_count, 0)
