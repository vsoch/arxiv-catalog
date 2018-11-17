# The Arxiv Catalog

Are you shopping for papers, based on their equations? This is a fun project
related to [arxiv-equations](https://www.github.com/vsoch/arxiv-equations)
to generate a rendering of the equations that are used in a research article.
For this first step, we just want to visualize summary metrics based on
categories, along with the rendered equations. For some future version,
we will go one step further and make these equations into pretty images
using [penrose](https://www.github.com/penrose/penrose).

## Summary Pages

The input data to generate a table of summary metrics, organized with category in
rows and metric in columns, was created [by this script]() and organized here.
The remaining steps included:

 1. [Generate]() a catalog calendar page to find papers by month and year within each category.
 2. [Generate](generatePage.py) a html/css page to link to the calendar page for the equations in a given article.
