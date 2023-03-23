# Helper Functions for the casual Python enthusiast
# Logging (debug, console, data output)
# Error Messaging
# Print functions for better visualization.

import datetime as datetime
import os

# "Global" variables stored here
DateTimeStart = datetime.datetime.now()
DebugLogFName = ""
DataOutFName = ""
ConsoleOutFName = ""
DebugLogDirectory = os.getcwd() + "\\"
DataOutDirectory = os.getcwd() + "\\"
ConsoleOutDirectory = os.getcwd() + "\\"

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
    global PrintConsoleOutput

    if PrintConsoleOutput:
        line = "\r" + str(mess)
        print(line, end="", flush=True)
        if end:
            print("\n")
    return 0


# handling a debug print statement in logging or console according to vars
def DBG(mess):
    global DebugLogFName
    mess = "[DBG] :: " + mess

    if PrintDebugMessages:
        print(mess)

    if LogDebugMessages:
        now = datetime.datetime.now()
        TimeStamp_string = "[" + now.strftime("%d/%m/%Y %H:%M:%S") + "] "

        if DebugLogFName == "":
            print("No Debug Log File specified, defaulting to DebugLog_<date_time>.txt")
            DebugLogFName = "DebugLog_" + DateTimeStart.strftime("%Y%m%d_%H%M") + ".txt"

        with open(DebugLogFName, 'a') as f:
            f.write(TimeStamp_string + mess + "\n")
    return


# Use this instead of print to handle if/where the output is shown
def Console(mess):
    global ConsoleOutFName

    if PrintConsoleOutput:
        print(mess)

    if LogConsoleOutput:
        now = datetime.datetime.now()
        TimeStamp_string = "[" + now.strftime("%d/%m/%Y %H:%M:%S") + "] "

        if ConsoleOutFName == "":
            print("No Console Output File specified, defaulting to ConsoleOut_<date_time>.txt")
            ConsoleOutFName = "ConsoleOut_" + DateTimeStart.strftime("%Y%m%d_%H%M") + ".txt"

        with open(ConsoleOutFName, 'a') as f:
            f.write(TimeStamp_string + mess + "\n")
    return


# EOF
