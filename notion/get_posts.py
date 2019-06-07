import json
import os
import re
from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2=os.environ["TOKEN"])

prefixes = {
    "header": "# ",
    "sub_header": "## ",
    "sub_sub_header": "### ",
    "bulleted_list": "+ ",
    "numbered_list": "1. ",
    "toggle": "[ ]",
    "quote": "> ",
}


def get_post_text(post):
    text = ""

    for child in post.children:
        if child.type == "page":
            text += get_post_text(child)
        if child.type == "image":
            pass
        else:
            prefix = prefixes.get(child.type, "")
            text += prefix + child.title + "\n\n"

    return text


def get_frontmatter(post, text):
    return """---
title: %s
date: "%s"
description: %s
---""" % (
        post["name"],
        post["publish_date"].start.isoformat(),
        "Word count: %s" % len(re.sub("\W+", "", text).split()),
    )


field_blacklist = ["publish_date"]


def resolve_fields(post_record):
    markdown = get_post_text(post_record)
    post = post_record.get_all_properties()
    header = get_frontmatter(post, markdown)

    return {
        **post,
        "publish_date": post["publish_date"].start.isoformat(),
        "updated": post["updated"].isoformat(),
        "markdown": markdown,
        "header": header,
    }


def get_blog_posts():
    page = client.get_block("https://www.notion.so/2e831e83a61846ccbf184c0f00753549")

    return [
        resolve_fields(post)
        for post in page.collection.get_rows()
        if post.get_property("published")
    ]


if __name__ == "__main__":
    try:
        os.mkdir("posts/")
    except:
        pass
    for post in get_blog_posts():
        filename = post["name"] + "/index.md"
        os.mkdir("posts/" + post["name"])
        with open("posts/" + filename, "w") as text_file:
            text_file.write(post["header"] + post["markdown"])
