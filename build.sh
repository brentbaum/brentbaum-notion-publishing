echo "Starting build"
cd notion
[ -e notion/posts ] && rm -r notion/posts
echo "Get posts"
python get_posts.py
cd ../
[ -e blog/content/blog ] && rm -r blog/content/blog
cp -r notion/posts blog/content/blog
cd blog
echo "Build frontend site"
yarn build
