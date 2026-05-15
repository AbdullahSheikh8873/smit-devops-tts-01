from fastapi import FastAPI
import json

app = FastAPI()

# Read = Get | Write = post

# localhost:8000/
@app.get("/")
def home():
    return {"message": "API is running"}





# def function_name(parameters):
#     return value

# def greet(name):
#     return "Hello " + name

# print(greet("Abdullah"))

def read_json():
    with open("server.json", "r") as file:
        json_data = json.load(file)
    return json_data

data = read_json()

@app.get ("/data")
def get_data():
    return data

# def write_json(data):
#     with open("server.json", "w") as file:
#         json.dump(data, file, indent=4)

# data = read_json()
# data["server"]["status"] = "stopped"
# write_json(data)

# print(read_json()["server"]["ip"])
