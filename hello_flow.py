import asyncio
from prefect import task, flow
from prefect.filesystems import LocalFileSystem
# Define a task
@task
def say_hello():
    print("Hello, Prefecttt!")
    add_result=add(10,2)
    sub_result=subtract(add_result,2)
    end_result=end(sub_result)
    return end_result
@task
def add(a: int, b: int):
    return a+b
@task
def subtract(a: int, b: int):
    return a-b
@task
def end(a : int):
    return a          

# Define the flow
@flow(name="hello-flow")
def hello_flow():
    result=say_hello()
    return result
    
    