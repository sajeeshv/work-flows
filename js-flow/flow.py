from prefect import flow, task
import os
import subprocess

@task
def run_js_script():
    js_file = os.path.abspath("./js-flow/js-script/index.js")
    js_dir = os.path.dirname(js_file)

    if os.path.exists(js_file):
        print(f"{js_file} exists")
        # Ensure dependencies are installed
        subprocess.run(["npm", "install"], cwd=js_dir, check=True)
        
        result = subprocess.run(["node", js_file], capture_output=True, text=True)
        return result.stdout
    else:
        print(f"{js_file}not exist")
        return "JS file not found"
    

@flow
def js_workflow():
    output = run_js_script()
    print(f"JS output: {output}")


if __name__ == "__main__":
    js_workflow()