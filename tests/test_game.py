import unittest
import StringIO
import sys
from demonata import demonata

def test_game_starts():
  capturedOutput = StringIO.StringIO()
  sys.stdout = capturedOutput
  demonata.main()
  sys.stdout = sys.__stdout__
  assert capturedOutput.getvalue() == "Welcome to Demonata\n"
