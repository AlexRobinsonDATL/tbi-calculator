import sys
from typing import Dict, List

from cx_Freeze import Executable, setup

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options: Dict[str, List[str]] = {"packages": [], "excludes": []}


base = "Win32GUI" if sys.platform == "win32" else None

executables = [Executable("tbi_calculator/app.py", base=base)]

setup(
    name="TBI Calculator",
    version="1.0",
    description="",
    options={"build_exe": build_options},
    executables=executables,
)
