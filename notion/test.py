from get_posts import client

page = client.get_block("https://www.notion.so/2e831e83a61846ccbf184c0f00753549")
posts = page.collection.get_rows()

linked_post = posts[4]
for child in linked_post.children:
    print(child.type)
    print(child.title)
    print(child.children)
