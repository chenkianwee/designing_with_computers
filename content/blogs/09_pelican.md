Title: How I Developed My Website Using Python Pelican
Description: Using Python Pelican for developing my website documenting my research and open-source projects. 
Date: 2026-04-04
Authors: Kian Wee Chen
Status: draft
Duration: xx mins
Category: Tutorial

I have been using Jekyll with Github pages for my website. Jekyll is a great static site generator with many great themes available. I was quite happy with my Jekyll site. However, Jekyll is written in Ruby, I am much more comfortable with Python. I get really nervous about breaking something whenever I want to change the underlying theme. I chose Jekyll previously cause of the availability of great looking themes, which is not exactly the case with Pelican. I finally found the time and the determination to make the transition to Pelican recently. Unfortunately, after searching around online, Pelican still faces the same issues of lacking good looking themes. I will have to dive into Pelican and customize it for my website.

# Learning and Understanding Pelican
The first thing to do here is to understand Pelican. Pelican has a decent <a href="https://docs.getpelican.com/en/latest/index.html" target="_blank">documentation site</a>. The site's Getting Started provide basic installation, create a project and site generation guides. It is useful to go through them and have a sense of the Pelican workflow. However, I feel there are not sufficient materials for beginners like me who wants to build a good looking website for documenting my works. I search online and found two good tutorials <a href="https://inventwithpython.com/blog/pelican-tutorial.html" target="_blank">here</a> and <a href="https://mosaid.xyz/articles/complete-tutorial--creating-categories-and-subcategories-using-pages-in-pelican-2.html" target="_blank">here</a>, that really help me with understanding Pelican, and of course I used LLMs like Gemini to help with the learning. Consider going through the tutorials. 

- Pelican concept articles and pages
- pelicanconf.py and publishconf.py

# Tutorial 1: Minimal Site with Landing, Blog Index and About Pages
[Pelican tutorial 1](../pelican_tutorial/01_start.html)

# Publishing to Github Pages
- git submodule your theme 
```
git submodule add https://github.com/username/solo_proto_workshop_bootstrap5.git themes/solo_proto_workshop_bootstrap5
git add .
git commit -m "Add Bootstrap 5 workshop theme as submodule"
git push origin main
```
- through this workflow you can have two git repo within a project 
    - you will need to commit the submodules independently, cd into the submodule and do the commit 
    - then commit again in the main repo

- github workflow action 
```
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: true  # <--- THIS IS CRITICAL
          fetch-depth: 0    # Fetch all history for submodules
```

- Custom Domain: If you use a custom domain (e.g., research.yourname.com), make sure your SITEURL in publishconf.py reflects that, and you have a CNAME file in your content/extra/ folder.

- cname file is just a text file with your domain name example.com

- put the cname file in content/extra/CNAME

- add the following to the pelicanconf.py
```
# Tell Pelican to look in 'content/extra' for additional files
STATIC_PATHS = ['images', 'extra/CNAME']

# Tell Pelican to place the CNAME file in the root of the output folder
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
```

- SITEURL: Make sure your SITEURL in publishconf.py matches the domain in your CNAME file:

- [instructions for custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)