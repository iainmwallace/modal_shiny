
import shlex
import subprocess
from pathlib import Path

import modal

image = modal.Image.debian_slim().pip_install("shiny")

app = modal.App(
    name="example-modal-shiny", image=image
)  


shiny_script_local_path = Path(__file__).parent / "app.py"
shiny_script_remote_path = Path("/root/app.py")

if not shiny_script_local_path.exists():
    raise RuntimeError(
        "app.py not found! Place the script with your shiny app in the same directory."
    )

shiny_script_mount = modal.Mount.from_local_file(
    shiny_script_local_path,
    shiny_script_remote_path,
)

@app.function(
    allow_concurrent_inputs=100,
    mounts=[shiny_script_mount],
)
@modal.web_server(8000)
def run():
    target = shlex.quote(str(shiny_script_remote_path))
    cmd = f"shiny run --host 0.0.0.0 -p 8000 {target}  "
    subprocess.Popen(cmd, shell=True)

