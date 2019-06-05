cd notion
[ -e notion/posts ] && rm -r notion/posts
pipenv run python get_posts.py
cd ../
[ -e blog/content/blog ] && rm -r blog/content/blog
cp -r notion/posts blog/content/blog
cd blog
yarn build
