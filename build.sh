pipenv run python get_posts.py
rm -r blog/content/blog
cp -r posts blog/content/blog
cd blog
yarn build
netlify deploy
