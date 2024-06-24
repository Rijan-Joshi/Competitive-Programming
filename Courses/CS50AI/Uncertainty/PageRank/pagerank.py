import os
import random
import re
import sys
import numpy as np
from collections import Counter

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    transition_model = dict()
    p_inside = damping_factor/len(corpus[page]) + ((1-damping_factor)/len(corpus))
    p_outside = (1-damping_factor)/len(corpus)
    
    for key in corpus:
        if key in corpus[page]:
            transition_model[key] = p_inside
        else:
            transition_model[key] = p_outside
    
    return transition_model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    #Getting all the pages as states from the corpus
    states = list(corpus.keys())

    #Selecting the starting state randomly from the given html pages from the corpus
    start_state = random.choice(states)
    current_state = start_state

    #Keeping track of the sampled_state
    sampled_state = [start_state]

    #Keeping track of the count
    count_tracker = Counter()
    count_tracker[start_state] += 1

    while len(sampled_state) < n:        
        #Getting the probabilities considering the damping factor
        transition = transition_model(corpus, current_state, damping_factor)
        
        #Getting the states and weights from transition model
        states = list(transition.keys())
        weights = list(transition.values())

        next_state = np.random.choice(states, p = weights)

        current_state = next_state
        sampled_state.append(current_state)
        count_tracker[str(current_state)] += 1 

    pagerank = {page: count/n for page, count in count_tracker.items()}
    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = dict()
    d = damping_factor
    N = len(corpus)

    #Initializing all pages to the pagerank of 1/N
    for page in corpus:
        pagerank[page] = 1/N
    
    def pr(page):
        current_pagerank = pagerank[page]
        pagerank[page] = (1-d)/N + d * second(page)

        while abs(current_pagerank - pagerank[page]) > 0.001:
            pr(page)

    def second(p):
        for filename in corpus:
            if p in corpus[filename]:
                return pagerank[filename]/len(corpus[filename])

    for page in corpus:
        pagerank[page] = pr(page)

if __name__ == "__main__":
    main()
