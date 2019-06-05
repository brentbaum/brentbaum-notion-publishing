[ -e posts ] && rm -r posts
pipenv run python get_posts.py
[ -e blog/content/blog ] && rm -r blog/content/blog
cp -r posts blog/content/blog
cd blog
yarn build
