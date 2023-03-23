# Testing/Using helper functions
import Helpers
from Helpers import *


print("3... 2... 1... GO!\n")

DBG("Debugging not enabled.")
Console("Enabling Debugging now...")
Helpers.PrintDebugMessages = True
DBG("Debugging Enabled.")

print("\nYeah, feeling good about that! :) ")
