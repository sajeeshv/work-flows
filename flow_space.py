import asyncio
import requests
import json
from prefect import task, flow

# Define a task
@task
def start_flow():
    print("Flow Started..!")
    spaces=asyncio.run(get_spaces())
    return spaces

@task
async def get_spaces():
    url = "https://api.ts-system/api/spaces"
    response = requests.get(url)
    data = response.json()
    return data
         

# Define the flow
@flow(name="flow-space")
def flow_space():
    result=start_flow()
    print('--------SPACES-----------')
    print(json.dumps(result, indent=4, sort_keys=True))
    print('-------------------------')
    return result

# if __name__ == "__main__":
#     flow_space()    
    