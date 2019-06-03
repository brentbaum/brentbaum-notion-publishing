import inspect
import json
import os
import sys

from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2=os.environ["TOKEN"])


page = client.get_block("https://www.notion.so/Wisdom-7344a9530e374b468967b11859c31b30")
space = client.get_space(page.space_info['spaceId'])

print(space.pages)
print(page.space_info)

def serializable(obj):
    try:
        return json.dumps(obj)
    except TypeError:
        return None

def get_block_dict(block):
    blacklist = ["children", "parent"]

    attributes = [a for a in inspect.getmembers(block) if not a[0].startswith('__') and a[0] not in blacklist]
    properties = [a for a in attributes if not callable(a[1]) and serializable(a[1])]

    block_dict = dict(properties)
    if hasattr(block, "children"):
        block_dict["children"] = [get_block_dict(child) for child in block.children]

    return block_dict

# print("The old title is:", page.title)
pages = []
for page_id in space.pages:
    page = client.get_block(page_id)
    pages.append(get_block_dict(page))
str = json.dumps(pages)
print(str)

with open("output.txt", "w") as text_file:
    text_file.write(str)

# serialized = get_block_dict(page)
# print(serialized)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
# page.title = "The title has now changed, and has *live-updated* in the browser!"