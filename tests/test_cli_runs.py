import subprocess, sys, pathlib, json

DEMO = pathlib.Path(__file__).parent.parent / "src" / "demo_run.py"

def test_demo_script_exits_clean():
    result = subprocess.run([sys.executable, DEMO], timeout=15)
    assert result.returncode == 0 