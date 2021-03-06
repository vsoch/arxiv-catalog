#!/usr/bin/env python

# This script will read in a pickle that includes extracted metadata and 
# equations from an article, and general yaml (with front end matter) to
# render into a page.

import pickle
import operator
import frontmatter

input_pkl = sys.argv[1]
result = pickle.load(open(input_pkl,'rb'))

# result.keys()
# dict_keys(['equations', 'metadata', 'inputFile', 'latex', 'uid']

################################################################################
# ARTICLE TEMPLATE
################################################################################

template = frontmatter.load('article-template.md')

template.content = result['metadata']['summary']

# Add metadata to template, only specific fields
template.metadata['id'] = result['metadata']['id']
template.metadata['updated'] = result['metadata']['updated']
template.metadata['published'] = result['metadata']['published']

# Parse year, month, day
month = result['metadata']['published_parsed'].tm_mon
day = result['metadata']['published_parsed'].tm_mday
year = result['metadata']['published_parsed'].tm_year

template.metadata['published_month'] = month
template.metadata['published_day'] = day
template.metadata['published_year'] = year

template.metadata['title'] = result['metadata']['title']
template.metadata['search_query'] = result['metadata']['title_detail']['base']
template.metadata['title_detail'] = result['metadata']['title_detail']['value']

template.metadata['authors'] = result['metadata']['authors']
template.metadata['comment'] = result['metadata']['arxiv_comment']

# Parse links into list
links = []
for link in result['metadata']['links']:
    links.append(link['href'])

template.metadata['links'] = links
template.metadata['category'] = result['metadata']['arxiv_primary_category']['term']
template.metadata['topic'] = result['metadata']['arxiv_primary_category']['term']

# Tags
tags = []
for tag in result['metadata']['tags']:
    tags.append(tag['term'])

template.metadata['tags'] = tags
template.metadata['pdf_url'] = result['metadata']['pdf_url']
template.metadata['length'] = result['metadata']['length']
template.metadata['arxiv_url'] = result['metadata']['arxiv_url']

# Equations
raw =  [e.replace('\\\\','\\') for e in result['equations']]

# Let's count instead
equations = dict()
for e in raw:
    if e not in equations:
        equations[e] = 0
    equations[e] +=1

# Get total count to calculate percent
total = 0
for e,count in equations.items():
    total += count

# Let's make total width 900px

# Ensure is sorted
equation_list = []
for item in sorted(equations.items(), key=operator.itemgetter(1)):
    percent = item[1] / total
    pixels = round(percent * 900, 0)
    equation_list.append({'equation': item[0], 
                          'count': item[1], 
                          'pixels': pixels,
                          'percent': round(100*percent,2) })

# Greatest to least
equation_list.reverse()

template.metadata['equations'] = equation_list
template.metadata['equations_total'] = total

# Write to File
outfile = os.path.join('_posts', '%s-%02d-%02d-%s.md' %(year, month, day, result['uid'].replace('/','-')))
with open(outfile, 'w') as filey:
    filey.writelines(frontmatter.dumps(template))


################################################################################
# TOPIC TEMPLATE
################################################################################

topic = template.metadata['topic']
outfile = os.path.join('topics', '%s.md' %(topic))
if not os.path.exists(outfile):
    template = frontmatter.load('topic-template.md')
    template.metadata['title'] = topic
    template.metadata['topic'] = topic
    template.metadata['permalink'] = "/%s" %topic
    # TODO we should have some overall count here?
    with open(outfile, 'w') as filey:
        filey.writelines(frontmatter.dumps(template))

