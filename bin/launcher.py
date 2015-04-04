import sys
import subprocess

import shared


def main(args, async=False, console=False):
    args = list(args)
    shared.setup()

    program = args.pop(0)

    args = [sys.executable, "-m", program] + args
    kwargs = dict()

    if console is False:
        CREATE_NO_WINDOW = 0x08000000
        kwargs["creationflags"] = CREATE_NO_WINDOW

    app = subprocess.Popen(args, **kwargs)

    if async is False:
        return app.communicate()


if __name__ == '__main__':
    args = sys.argv[1:]
    kwargs = dict()

    for flag in ("--console", "--async"):
        try:
            index = args.index(flag)
            kwargs[args.pop(index).strip("-")] = True
        except:
            pass

    main(args, **kwargs)
