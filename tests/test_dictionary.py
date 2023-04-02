from __init__ import *
from src.dictionary import *

# Mock user input to 'q'
with mock.patch("builtins.input", return_value="q"):
    # Call the script
    dictionary()
    # Check that the script has exited without errors
    # (no output means the test passed)