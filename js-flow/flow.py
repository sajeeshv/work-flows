from prefect import flow, task
import subprocess

@task
def run_js_script():
    result = subprocess.run(["node", "run", "index.js"], capture_output=True, text=True)
    return result.stdout

@flow
def js_workflow():
    output = run_js_script()
    print(f"JS output: {output}")