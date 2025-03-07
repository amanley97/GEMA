# ----------------------------------------------------------------------------
# File: <__main__>.py
#
# Description:
# <Main to run gEMA as a module>.
#
# Contact:
# For inquiries, please contact Alex Manley (amanley97@ku.edu).
#
# License:
# This project is licensed under the MIT License. See the LICENSE file
# in the repository root for more information.
# ----------------------------------------------------------------------------

import argparse
from pathlib import Path
from gem5.utils.gema import *

parser = argparse.ArgumentParser("gEMA host")
parser.add_argument("port", help="Port to use for API", type=int)
parser.add_argument("--m5_override", help="Override directory for simulation output", required=False, type=Path)
args = parser.parse_args()

if __name__ == "__m5_main__":
    app = Gema(port=args.port, m5_override=args.m5_override)
    app.run()
