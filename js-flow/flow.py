# from prefect import flow, task
import os
import subprocess

# @task
def run_js_script():
    if os.path.exists(os.path.abspath("js-flow/js-script/index.js")):
        print(f"{os.path.abspath("js-flow/js-script/index.js")} exists")
    else:
        print(f"{os.path.abspath("js-flow/js-script/index.js")}not exist")
    result = subprocess.run(["node", os.path.abspath("js-flow/js-script/index.js")], capture_output=True, text=True)
    return result.stdout

# @flow
def js_workflow():
    output = run_js_script()
    print(f"JS output: {output}")


if __name__ == "__main__":
    js_workflow()