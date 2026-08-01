import os
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))

os.environ["MYTM_PORT"] = "8876"
os.environ["MYTM_DB"] = os.path.join(HERE, "demo_cockpit.db")
os.environ["MYTM_SKIP_GCAL"] = "1"
os.environ["ANTHROPIC_API_KEY"] = ""

SERVER = r"C:\Claude\Franz\MyTM\system\mytm_server.py"
runpy.run_path(SERVER, run_name="__main__")
