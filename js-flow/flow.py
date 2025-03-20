from prefect import flow, task
import os
import subprocess

@task
def run_js_script():
    print("JS script PATH",os.path.abspath("./js-flow/js-script/index.js"))
    if os.path.exists(os.path.abspath("./js-flow/js-script/index.js")):
        print("File or directory exists")
    else:
        print("File or directory does not exist")
    result = subprocess.run(["node", "run",os.path.abspath("./js-flow/js-script/index.js")], capture_output=True, text=True)
    return result.stdout

@flow
def js_workflow():
    output = run_js_script()
    print(f"JS output: {output}")


if __name__ == "__main__":
    js_workflow()