# Helper Functions for the casual Python enthusiast
# Logging (debug, console, data output)
# Error Messaging
# Print functions for better visualization.

import datetime as datetime
import os

# "Global" vars stored here
DateTimeNow = datetime.datetime.now()
DateTimeStamp = "_" + DateTimeNow
DebugLogFName = ""
DataOutFName = ""
ConsoleOutFName = ""
DebugLogDirectory = os.getcwd() + "\\"
DataOutDirectory = os.getcwd() + "\\"
ConsoleOutDirectory = os.getcwd() + "\\"
DateTimeNow = datetime.datetime.now()
DateTimeStamp = "_" + str(DateTimeNow)

# User Settings
LogDebugMessages = False
PrintDebugMessages = False
LogConsoleOutput = False
PrintConsoleOutput = True


def ExitError(mess):
    print("ERROR::" + mess)
    exit()
    return 0


# prints a message that can be overwritten unless next print() begins with \n
def PrintOver(mess, end=False):
    line = "\r" + str(mess)
    print(line, end="", flush=True)
    if end:
        print("\n")
    return 0


def DBG(mess):
    global DebugLogFName
    print("DBG(): " + mess)
    return


def Console(mess):
    global ConsoleOutFName
    print("Console(): " + mess)

    if PrintConsoleOutput:
        print(mess)

        if LogConsoleOutput:
            if ConsoleOutFName == "":
                DBG("No Console Output File specified, defaulting to ConsoleOut.txt")
                ConsoleOutFName = "ConsoleOut.txt"

            with open(ConsoleOutFName, 'a') as f:
                f.write(mess + "\n")

    return


# EOF
