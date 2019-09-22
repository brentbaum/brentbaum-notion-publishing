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
        "%s words" % len(text.split()),
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
    # Get link by clicking on ... above collection.
    collection_link = "https://www.notion.so/2e831e83a61846ccbf184c0f00753549?v=0483f7a0d6ed4919a537bfd443a07022"
    collection_view = client.get_collection_view(collection_link)
    all_rows = list(collection_view.build_query().execute())
    print("Fetched all posts, formatting for consumption.")

    return [
        resolve_fields(post)
        for post in all_rows
        if post.get_property("published")
    ]


if __name__ == "__main__":
    print("start")
    try:
        os.mkdir("posts/")
    except:
        pass
    posts = get_blog_posts()
    print(len(posts), "posts found")
    for post in get_blog_posts():
        print("Writing post", post["slug"])
        filename = post["slug"] + "/index.md"
        os.mkdir("posts/" + post["slug"])
        with open("posts/" + filename, "w") as text_file:
            text_file.write(post["header"] + post["markdown"])
    print("Finished fetching posts.")
