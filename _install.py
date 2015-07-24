"""Pyblish Installation Program

Usage:
    $ install --help

"""

import os
import sys
import time
import argparse
import datetime
import threading
import subprocess
from itertools import cycle

header = """
            ___________________
            \                 /
              \             /
                \         /
                  \     /
                    \ /
                     |
                     |
                     |
                     |
                     |

            Pyblish Installation

 This installation requires Python and Git
and will occupy at least 400 mb of disk space,
    whereof ~300 mb will be downloaded.

 The installation typically takes around 10-15
           minutes to complete.
"""


def main(globally, verbose, mock, mock_error, accept_defaults):
    """Primary installation procedure

    Arguments:
        globally (bool): Write permanent environment variables
        verbose (bool): Print a lot of output
        mock (bool): Fake the download
        mock_error (bool): Fake an error
        accept_defaults (bool): Do not require input

    """

    if not proceed(accept_defaults):
        sys.exit(1)

    if not has_requirements():
        sys.exit(2)

    print("")
    print("Downloading, this may take a while..")

    # Start animation
    if not verbose:
        data = {"finished": False}
        t = threading.Thread(target=animation, args=[data])
        t.daemon = True
        t.start()

    if mock:
        popen = subprocess.Popen(
            ["sleep", "2"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    else:
        popen = subprocess.Popen(
            ["git", "submodule", "update", "--init", "--recursive"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

    output = list()
    for line in iter(popen.stdout.readline, b""):
        output.append(line)
        if verbose:
            sys.stdout.write(line)

    popen.communicate()  # Wait to finish

    if not verbose:
        data["finished"] = True

    sys.stdout.write("\n\n")

    if mock_error:
        output = ["Ack!\n\r", "A mocked error\n\r", "\n\r", "Hmm\n\r"]

    if (popen.returncode != 0) or mock_error:
        if not accept_defaults:
            print("Error: Had some trouble, here are the 4 last lines..")
            print("")
            print("=" * 60)
            print("".join(output[-4:]))
            print("=" * 60)

            sys.stdout.write("\nPrint the full output? [y/N]: ")
            if raw_input().lower() in ("y", "yes"):
                print("")
                print("".join(output))
        else:
            print("".join(output))

        sys.exit(2)

    else:
        time.sleep(0.5)
        print("Download complete")
        time.sleep(1)

    sys.stdout.write("\nWriting environment variables..")
    dirname = os.path.abspath(os.path.dirname(__file__))
    integrations = os.path.join(dirname, "lib", "pyblish-x", "integrations")

    environment = {
        "PYTHONPATH": ";".join([
            os.path.join(dirname, "pythonpath"),
            os.path.join(integrations, "maya")
        ]),
        "HOUDINI_PATH": ";".join([
            "&",
            os.path.join(integrations, "houdini")
        ]),
        "NUKE_PATH": os.path.join(integrations, "nuke"),
        "HIERO_PATH": os.path.join(integrations, "hiero"),
    }

    for key, value in environment.iteritems():
        os.environ[key] = ";".join([value, os.environ.get(key, "")])

    if globally:
        sys.stdout.write(" globally..\n")
        for key in environment:
            try:
                subprocess.check_output(
                    ["setx", key, os.environ[key]],
                    env=os.environ
                )
            except subprocess.CalledProcessError:
                print("Error: Couldn't write environment variables globally")
                print("See installation guide for instructions on how to ")
                print("write them manually.")
                print("https://github.com/pyblish/pyblish-win/wiki")
                break

    else:
        sys.stdout.write("\n")

    sys.exit(0)


def has_requirements():
    try:
        popen = subprocess.Popen(
            ["where", "git"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        popen.communicate()
        assert popen.returncode == 0
    except:
        print("")
        print("Error: Installation requires Git")
        print("See installation guide for details, or use binary installer")
        print("https://github.com/pyblish/pyblish-win/wiki")
        return False
    return True


def animation(data):
    animation = cycle(['|.       |',
                       '|.       |',
                       '| .      |',
                       '|   .    |',
                       '|      . |',
                       '|       .|',
                       '|       .|',
                       '|      . |',
                       '|    .   |',
                       '| .      |',
                       '|.       |'])

    counter = 0
    start = datetime.datetime.now()
    print("")
    print("|        | Duration")
    print("|--------|-----------")
    while not data["finished"]:
        delta = datetime.datetime.now() - start
        d = {
            "percentage": ("%.2f %%" % counter).ljust(9),
            "duration": "%02d:%02d:%02ds" % (
                (delta.seconds / 60 / 60) % 24,
                (delta.seconds / 60) % 60,
                (delta.seconds) % 60)
        }

        frame = (animation.next() + " {duration}").format(**d)

        sys.stdout.write('\r')
        sys.stdout.write(frame)
        sys.stdout.flush()
        time.sleep(0.1)

        # Fake a percentage, to calm their minds.
        counter += 0.01
        if counter > 100:
            counter = 0


def proceed(accept_defaults):
    subprocess.call("cls", shell=True)
    print(header)
    if not accept_defaults:
        sys.stdout.write("Install Pyblish? [Y/n]: ")
        if raw_input().lower() not in ("", "y", "yes"):
            return False
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--global", action="store_true", dest="globally",
                        help="Set global environment variables")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Print a lot of information")
    parser.add_argument("-y", "--yes", action="store_true",
                        dest="accept_defaults", help="Accept defaults")
    parser.add_argument("--mock", action="store_true",
                        help="Do not actually download anything")
    parser.add_argument("--mock-error", action="store_true",
                        help="Mock an error")

    args = parser.parse_args()

    try:
        main(**args.__dict__)

    except KeyboardInterrupt:
        print("\nCancelled")
        sys.exit(0)

    except SystemExit as e:
        if e.code == 0:
            print("Entering subshell..")
            time.sleep(0.5)

            # Enter subshell where local variables are present.
            dirname = os.path.abspath(os.path.dirname(__file__))
            try:
                sys.exit(subprocess.call(
                    ["cmd", "/K", os.path.join(dirname, "subshell.bat")],
                    env=os.environ))
            finally:
                print("Leaving Pyblish installation program")

        elif e.code == 1:
            print("Aborted")

        else:
            print("")
            print("Installation failed..")
            print("Try the --verbose flag for more output")
            print("Or see --help for more options")
