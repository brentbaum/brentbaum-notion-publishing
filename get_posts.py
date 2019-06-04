import json
import os
from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2=os.environ["TOKEN"])

prefixes = {"header": "# ", "sub_header": "## ", "sub_sub_header": "### ", "bulleted_list": "+ ", "numbered_list": "1. ", "toggle": "[ ]", "quote": "> "}

def get_post_text(post):
    children = [{"text": child.title, "type": child.type} for child in post.children]
    text = ""

    for child in children:
        prefix = prefixes.get(child["type"], "")
        text += prefix + child["text"] + "\n\n"

    return text

field_blacklist = ["publish_date"]
def resolve_fields(post_record):
    post = post_record.get_all_properties()
    formatted_post = {
        **post,
        "updated": post["updated"].isoformat(),
        "markdown": get_post_text(post_record)
    }
    return {k: v for k, v in formatted_post.items() if k not in field_blacklist}

def get_blog_posts():
    page = client.get_block("https://www.notion.so/2e831e83a61846ccbf184c0f00753549")

    return [resolve_fields(post) for post in page.collection.get_rows() if post.get_property('published')]


print(json.dumps(get_blog_posts()))
