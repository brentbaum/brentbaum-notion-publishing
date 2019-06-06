pip3 install pipenv

echo "Starting build"
cd notion
pipenv install
[ -e notion/posts ] && rm -r notion/posts
echo "Get posts"
pipenv run python get_posts.py
cd ../
[ -e blog/content/blog ] && rm -r blog/content/blog
cp -r notion/posts blog/content/blog
cd blog
echo "Build frontend site"
yarn build
