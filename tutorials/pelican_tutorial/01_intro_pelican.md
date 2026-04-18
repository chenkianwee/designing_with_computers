# How Pelican Works Under the Hood 
This tutorial is best read together with my [Pelican blog post](../blogs/09_pelican.html) on why I use Pelican for my website.

# What is Pelican
This page provides a summary of the core concept of Pelican. You can read the full Pelican documentation <a href = https://docs.getpelican.com/ target = '_blank'>here</a>. Pelican is a static website generator. A static website serves pages using a fixed number of pre-built HTML, CSS and Javascript. It has no server-side processing and no database. Static pages loads very fast and is very responsive. It runs locally on your computer as all the pages are downloaded onto your browser when you visit the website. 

Pelican generates all the neccesary HTML, CSS and Javascript for your static website from your source files. In Pelican, the source files can be written either in markdown (.md) or reStructuredText (.rst). This is very convenient as Pelican can easily regenerate the website if you want to change the theme without affecting your content. 

# Structure of a Pelican Project
In a Pelican website there are two types of webpages; articles and pages.

- articles are chronological content such as a post and associated with a date.
- pages are used for content that does not change such as the About page.

The most basic of a Pelican project will contain folders and files as follows:

- **content**: folder containing all your source files.
- **output**: folder containing all the generated HTML, CSS and Javascript.
- **Makefile**: provide terminal commands to control Pelican using make tool. (not used in the tutorial)
- **pelicanconf.py**: configuration file to control the generation of the files in the output folder for preview website locally on your computer e.g. localhost:8000. 
- **publishconf.py**: imports all the settings in pelicanconf.py, settings here overwrites the pelicanconf.py settings when the website is published online e.g. https://example.com. 
- **tasks.py**: provide terminal commands to control Pelican using Python. (not used in the tutorial) 

## Settings
The default pelicanconf.py file as shown below contains the settings used by Pelican to generate the static website. Alot of the settngs are used by the theme to configure the website. For example the SITEURL is used by Pelican for routing purposes when linking pages in the website.

```
AUTHOR = 'me'
SITENAME = 'something'
SITEURL = ""
PATH = "content"
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'
```

Page level settings are specified in the source files. An example of an article page markdown is shown below with settings such as Title, Date and Category specified in the file followed by the content.

```
Title: My First Review
Date: 2010-12-03 10:20
Category: Review

Following is a review of my favorite mechanical keyboard.
```

All of the settings in the pelicanconf.py and publishconf.py (CAPS letters settings) and page level settings in the source files will be made accessible to Pelican and the theme when generating the static website. You can check all the available settings (in CAPS) <a href = "https://docs.getpelican.com/en/latest/settings.html" target = "_blank">here</a> and all the page level settings <a href = "https://docs.getpelican.com/en/latest/themes.html" target = "_blank">here</a>.

## Theme
As describe in the <a href = "https://docs.getpelican.com/en/latest/themes.html" target = "_blank">Pelican theme documentation</a>. The theme in Pelican uses the Jinja templating engine. Jinja templating allows the use of special placeholders in the template similar to writing Python code. The template is then used to render the final HTML. To create your own theme you will make changes to the templates. Many of the settings mentioned in the previous section is used in the Jinja templates. You can create new setting variables and refer to them in your template when customizing your own theme. 
 
