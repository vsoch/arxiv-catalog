# The Arxiv Catalog

Are you shopping for papers, based on their equations? This is a fun project
related to [arxiv-equations](https://www.github.com/vsoch/arxiv-equations)
to generate a rendering of the equations that are used in a research article.
For this first step, we just want to visualize summary metrics based on
categories, along with the rendered equations. For some future version,
we will go one step further and make these equations into pretty images
using [penrose](https://www.github.com/penrose/penrose).

## Collections

Each summary page I will represent as a collection, in the folder topics.
The input data to generate a table of summary metrics, organized with category in
rows and metric in columns, was created [by this script](), and then
the script to generate the yaml front end matter to parse into the collection
is [here]().

## Item Pages
The remaining content (the posts) includes all (N=?) of the individual articles in
the arxiv dump, each of which falls into one of the collections above. The script
[Generate](generatePage.py) was used to generate the yaml front end matter that
renders into the html/css page for a given article.
