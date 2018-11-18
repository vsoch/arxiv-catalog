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

## Generation

### 1. Single Article Pages

Each paper from Arxiv was downloaded via the [bulk data access](https://arxiv.org/help/bulk_data), meaning upper level tars and then extracted .tar.gz for each article. This work was done in the [arxiv-equations](https://www.github.com/vsoch/arxiv-equations) repository to generate a pickle of each paper. The pickle includes a dictionary data structure that has the following:

 - tex: the raw latex, as a string
 - metadata: metadata retrieved from the arxiv api, by using the [arxiv](https://github.com/lukasschwab/arxiv.py) python wrapper. Added is a length (the length of the latex).
 - equations: is a complete listing of equations (and latex symbols) from the article, extracted with the regular expression `\\$.*?(?<!\\\\)\\$` run against the raw latex.

Using the script [generatePage.py](generatePage.py) we extract metadata and the 
equations to generate a markdown file with frontend matter including all of the 
above (except for the tex). Instead of the tex, in the content area we put a 
summary of the article. Each of these is saved into the [_posts](_posts) folder,
and will be rendered into a signle article template, the goal being to visualize
the equations in an article.
