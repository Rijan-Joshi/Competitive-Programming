#Setting Up PageRank Logic by myself 

import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000

def main():
    if (len(sys.argv) != 2):
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print("PageRank Results from Sampling (n={SAMPLES)")
    for page in sorted(ranks):
        print(f"    {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    for page in sorted(ranks):
        print(f"   {page}: {ranks[page]:.4f}")


def crawl(directory):

    pages = dict()

    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    #Exclude all external links out of the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

def transition_model(corpus, page, damping_factor):
    pass

def sample_pagerank():
    ...

def iterate_pagerank():
    pass