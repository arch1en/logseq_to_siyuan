import json
import time

#region General

# Done
def json_object_generator(json_data):
    """
    Recursively iterate through a JSON object or list of JSON objects and yield each object.
    
    Args:
        json_data: A JSON object, list of JSON objects, or any nested structure containing JSON objects.
    
    Yields:
        Each JSON object found in the structure.
    """
    if isinstance(json_data, dict):
        yield json_data
        for value in json_data.values():
            yield from json_object_generator(value)
    elif isinstance(json_data, (list, tuple)):
        for item in json_data:
            yield from json_object_generator(item)


# Done
def flatten_json_objects(objects_list):
    """
    Flatten the JSON objects in the data.
    """
    result = []
    for i in objects_list:
        generator = json_object_generator(i)
        for j in generator:
            result.append(j)
    
    return result
    
# Done
def consolidate_json_objects(objects_list):
    result = {}

    generator = json_object_generator(objects_list)
    for j in generator:
        if "point" not in j:
            for k,v in j.items():
                if v is None:
                    result[k] = v
                elif isinstance(v, int):
                    result[k] = v
                elif "point" not in v:
                    result[k] = v

    return result

#region Logseq

class Logseq:
    def __init__(self):
        self.data = None
        pass

    # Done
    def load_data(self):
        with open('input.json', 'r', encoding="utf8") as file:
            # Loads data as JSON Object.
            self.data = json.load(file)

    # Done
    def extract_block_list(self):
        for k, v in self.data.items():
            if k == "blocks":
                return v


#region SiYuan

class SiYuan:
    def __init__(self):
        pass

    # Returns dict.
    # Key - Node ID
    # Value - Node object
    def load_data():
        pass


#region Main

logseq = Logseq()
logseq.load_data()

block_list = logseq.extract_block_list()
flattened = consolidate_json_objects(block_list)


with open('output.json', 'w', encoding="utf8") as file:
    json.dump(flattened, file, ensure_ascii=False, indent=4)
