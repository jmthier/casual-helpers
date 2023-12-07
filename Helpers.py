# Helper Functions for the casual Python enthusiast
# Logging (debug, console, data output)
# Error Messaging
# Print functions for better visualization.

from datetime import datetime
import os
import argparse

class bTextOptions:
    """constants for print() colors and styles"""

    class Color:
        """basic colors"""
        BASIC = '\033[0m'
        PURPLE = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        YELLOW = '\033[093m'
        RED = '\033[91m'
        GREEN = '\033[92m'

    class Style:
        """basic styles"""
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        DIM = '\033[2m'
        ITALIC = '\033[3m'

class CommandLine_Handler:
    """Class for Command Line Argument Handling"""

    io = None
    args = None

    def __init__(self, io):
        parser = argparse.ArgumentParser(prog="Bonfire Fodder",
                                         description="Interacting with Bonfire development boards",
                                         epilog="Comments?? haha")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-v", "--verbosity",
                            help="1, 2, or 3 levels of output verbosity.  [-v][-vv][-vvv]",
                            action="count",
                            default=0)
        group.add_argument("-s", "--silent",
                            help="no output at all",
                            action="store_true",)
        parser.add_argument("-l", "--log",
                            help="If used, output will be logged to a text file in the current working directory",
                            action="store_true")
        parser.add_argument("-a", "--app",
                            help="Run the shell app, user can try and try again.",
                            action="store_true")
        parser.add_argument("-r", "--run",
                            help="Runs a specific app specified after the argument",
                            default="")
        parser.add_argument("-f", "--finddevices",
                            help="This will scan the PC for any connected Bonfire devices",
                            action="store_true")

        self.io = io
        self.args = parser.parse_args()
        self.io.verbosity = self.args.verbosity
        self.io.silent = self.args.silent

    def parse_args(self):
        # Decide what to do based on command line args

        if self.args.log:
            self.io.LogOutput = True
            # self.io.LogFName = "DebugLog_" + DateTimeStart.strftime("%Y%m%d_%H%M") + ".txt"
            self.io.out("-l/-log flag received.", 1)

        if self.args.finddevices:
            self.io.out("-f/--finddevices flag received", 1)

        if self.args.app:
            self.io.out("-a/--app flag received", 1)

        if self.args.run:
            self.io.out("-r/--run flag received", 1)

        return self.args


class IO_Handler:
    """Class for better IO for files, visuals formatting, etc."""

    silent = False
    verbosity = 0
    LogOutput = False
    LogFName = ""
    DataOutFName = ""
    LogDirectory = os.getcwd() + "\\"
    DataOutDirectory = os.getcwd() + "\\"

    @property
    def start_date_time(self):
        """Returns the date and time the value was initialized (should be at program start)"""
        return self._start_date_time

    def __init__(self):
        self.log_directory = os.getcwd() + "\\"
        self.data_out_directory = os.getcwd() + "\\"
        self._start_date_time = datetime.now()

    def out(self, mess, v_level, dbg=False, style=None, overwrite=None):
        """overloading print().  outputs [mess] when verbosity >= v_level"""
        # Suggested v_level uses:
        #  0 - status messages (e.g., "scanning devices" or "progress - 85%")
        #  1 - program flow indications (e.g., "initializing X" or "creating output file OutFile.txt")
        #  2 - detailed variable status (e.g., "running function X() with args (Y)(Z)")

        if dbg:
            mess = "[DBG] :: " + mess

        match style:
            case "RED":
                style = bTextOptions.Color.RED
            case "BLUE":
                style = bTextOptions.Color.BLUE
            case "CYAN":
                style = bTextOptions.Color.CYAN
            case "YELLOW":
                style = bTextOptions.Color.YELLOW
            case "GREEN":
                style = bTextOptions.Color.GREEN
            case "PURPLE":
                style = bTextOptions.Color.PURPLE
            case "BOLD":
                style = bTextOptions.Style.BOLD
            case "UNDERLINE":
                style = bTextOptions.Style.UNDERLINE
            case "DIM":
                style = bTextOptions.Style.DIM
            case "ITALIC":
                style = bTextOptions.Style.ITALIC
            case None:
                style = bTextOptions.Color.BASIC
            case _:
                style = bTextOptions.Color.BASIC

        timestamp_string = ""
        if self.LogOutput:
            now = datetime.now()
            timestamp_string = "[" + now.strftime("%d/%m/%Y %H:%M:%S") + "] "
            if self.LogFName == "":
                print(f"{bTextOptions.Color.YELLOW}WARNING: No log filename specified, "
                      f"defaulting to Log_<date_time>.txt{bTextOptions.Color.BASIC}")
                self.LogFName = "Log_" + self.start_date_time.strftime("%Y%m%d_%H%M") + ".txt"

        if not self.silent:
            # silent flag not set in arguments
            if self.verbosity >= v_level:
                # User wants to see it
                if overwrite is None:
                    print(f"{style}{mess}{bTextOptions.Color.BASIC}", flush=True)
                else:
                    print(f"{style}{mess}{bTextOptions.Color.BASIC}", end="", flush=True)

                if self.LogOutput:
                    with open(self.LogFName, 'a') as f:
                        f.write(timestamp_string + mess + "\n")

        return

    def exit_error(self, mess):
        mess = "ERROR::" + mess
        self.out(mess, v_level=0, style="RED")
        exit()

    # prints a message that can be overwritten unless next print() begins with \n
    def over_write(self, mess, end=False):
        """Function for Copying over the previous line of output"""
        line = "\r" + str(mess)
        self.out(line, 1, overwrite=True)
        if end:
            print("\n")

        return 0

# EOF
