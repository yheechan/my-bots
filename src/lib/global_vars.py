import os
from pathlib import Path

curr_script = Path(__file__).resolve()
lib_dir = curr_script.parent
src_dir = lib_dir.parent

MAIN_DIR = src_dir.parent

RESULTS_DIR = MAIN_DIR / "results"
if not RESULTS_DIR.exists():
    RESULTS_DIR.mkdir()

LOG_DIR = RESULTS_DIR / "logs"
if not LOG_DIR.exists():
    LOG_DIR.mkdir()


SLACK_TOKEN = os.environ["SLACK_TOKEN"]
