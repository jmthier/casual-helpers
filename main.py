# Testing/Using helper functions

# Imports
from Helpers import CommandLine_Handler, IO_Handler
import time

vLevels = {0, 1, 2}

def main():
    """main() for testing the Helpers() file."""

    io = IO_Handler()

    # check all verbosity levels
    for vl in vLevels:
        io.verbosity = vl
        print(f"Verbosty set to {vl}")
        io.out("L2 detail -> Start with a DBG statement", 2, dbg=True)
        io.out("L2 detail -> but doesn't have to be...", 2)
        io.out("L1 detail -> we started main()", 1)
        io.out("L0 detail -> Beginning Test of Helpers.py", 0)
        time.sleep(2)

    print("Verbosity Test Complete")
    time.sleep(3)

    print("Verbosity back to max(2) for the rest of the tests.")
    IO_Handler.verbosity = 2
    print("Starting Countdown")
    sec = 5
    while sec > 0:
        io.over_write(f"Countdown: {sec}", end=False)
        time.sleep(1)
        sec -= 1
    io.over_write(f"Countdown: {sec}", end=True)

    print("Format Check:")
    io.out("This should be normal text", 0)
    io.out("YELLOW", 0, style="YELLOW")
    io.out("GREEN", 0, style="GREEN")
    io.out("BLUE", 0, style="BLUE")
    io.out("RED", 0, style="RED")
    io.out("CYAN", 0, style="CYAN")
    io.out("PURPLE", 0, style="PURPLE")
    io.out("BOLD", 0, style="BOLD")
    io.out("UNDERLINE", 0, style="UNDERLINE")
    io.out("ITALIC", 0, style="ITALIC")
    io.out("DIM", 0, style="DIM")
    io.out("This should already be back to regular, but just in case...", 0)
    io.out("BASIC", 0, style="BASIC")
    print("io.out() testing complete")
    time.sleep(10)

    return


# Catch all
if __name__ == "__main__":
    print(f"Testing in 3...2...1...")
    main()
    print(f"\n............Test complete!")

# EOF
