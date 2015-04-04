import sys
import subprocess

from shared import setup_environment


def main(args):
    args = list(args)
    setup_environment()

    program = args.pop(0)
    executable = sys.executable

    args = [executable, "-m", program] + args
    app = subprocess.Popen(args)

    return app.communicate()


if __name__ == '__main__':
    main(sys.argv[1:])
