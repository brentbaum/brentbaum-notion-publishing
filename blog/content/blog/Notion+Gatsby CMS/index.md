---
title: Notion+Gatsby CMS
date: "2019-06-07T04:01:00"
description: Just a notion blog post
---Todos

### Goals

I want to publish my work more. A common theme I see among people that I respect is "working out in the open." There are many benefits of this, but my main motivators are helping others who encounter issues by posting googleable notes and building an audience by having content. The one requirement I have is: It must be as easy as possible to author and publish new content. I should feel no polish, length, or completeness pressure: these things will only matter after the first 100 articles anyway :)

With that in mind, I've chosen Notion as a publishing platform. It's one shortcut away (read: low barrier to entry for writing down new thoughts) and has a solid (private) API that should scale to the level of sophistication I need. 

I've given myself one week to complete this project. Here we go!

### Saturday night: Planning requirements & research

__Desired publishing flow:__

1. Create page to be published

1. Add link to page in "Sitemap" table. This table will contain any metadata necessary to make the page.

1. Run CI task (Can I use gitlab or netlify for this? Need to publish once a day)

This API should handle everything I need to do w/ notion: [https://pypi.org/project/notion/](https://pypi.org/project/notion/)

### Sunday night: POC

Install notion API, take two passes at ways to recursively pull content for the blog. Settled on a table of posts w/ a "Published" toggle. This API is really fun to work with!

My script (30 lines long) pulls down a notion page, finds a table on that page, pulls all rows in that table with `published:true`, then converts the page linked in those rows to markdown. 

Technical risk identified: Making custom UI widgets for every block type in Notion could get painful. I'm not quite sure how I would make that work with markdown, too. 

### Monday night: Blog

Gatsby is a wonderful piece of technology. It is easy to use, familiar (built on React), and creates a nice, polished end product. They have a starter kit that I think I can use to go from zero to blog in a couple hours.

Success! I had some nasty errors messages along the way and lost an hour experimenting with different dependency combinations. Turns out, I had an extra newline at the beginning of my frontmatter file. Who knew whitespace mattered?

At the end of the night, my project is looking 10x more real:

### Tuesday night: bash time

I have limited time tonight, so I'm going to focus on laying the groundwork for automatic site builds. At the end of the night, I have a 10 line build script that calls all the pieces I previously set up. 

### Wednesday night: Build automation

Finagling with Netlify getting build to run end to end. I had issues with running pipenv as netlify only supports pipenv w/ python 2.7. 

Finally succeeded after an hour of tweaking build configurations. This means I can deploy my site with a push of a button or of a commit. That said, the button is inside netlify, which is no good. Now it's time to enable publishing from within Notion. 

Netlify supports build webhooks, but they work based off POST, not GET. Time to stand up a basic page that fires a POST whenever it's loaded.

Success. It took a bit as I found out the hard way Gatsby balks at any page name that includes a dash (-). I now have a page `/trigger9d4b7db1` that triggers a build whenever visited. How do I lock this down so that only I can deploy?

Now, if only there was a way to get feedback in notion when a triggered deploy succeeds...

Woke up Thursday morning with a solution: Call a Netlify API with something that will only succeed on my account if I'm logged in. Duh!

### Thursday night:

I added a button to view recent netlify deploys on the "build trigger" screen. Eventually I'll want to mirror build status between netlify build and notion, but that's out of scope for this project.

I've added the ability to resolve page links 

Notion Publishing

