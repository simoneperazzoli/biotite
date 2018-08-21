# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.

from typing import Optional, List
from subprocess import Popen
from .application import Application

class LocalApp(Application):
    def __init__(self, bin_path: str, mute: bool = True) -> None: ...
    def set_options(self, options: List[str]) -> None: ...
    def set_exec_dir(self, exec_dir: str) -> None: ...
    def set_std_out_file(self, file_path: str) -> None: ...
    def get_process(self) -> Popen: ...
    def get_exit_code(self) -> int: ...
    def run(self) -> None: ...
    def is_finished(self) -> bool: ...
    def wait_interval(self) -> float: ...
    def evaluate(self) -> None: ...
    def clean_up(self) -> None: ...
