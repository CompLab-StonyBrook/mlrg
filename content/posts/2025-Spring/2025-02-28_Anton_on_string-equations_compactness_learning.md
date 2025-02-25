Title: Anton on string equations, compactness and learning (02/28)
Author: Anton Hampe
Date: 2024-02-24

For the first session, Anton will be revisiting [Jeff's session on equational learning](https://complab-stonybrook.github.io/mlrg/news/2024-fall/jeff-on-learning-transducers-0920.html) from last semester.

Jeff pointed out two challenges with this new approach to learning transductions:

1. finding a method to identify characteristic samples which is independent of the class of transductions to be learned

2. finding a computationally tractable algorithm for solving equations

In this session we will learn about results from two subfields of computer science that offer solutions to these challenges.

The first challenge can be tackled by realizing that the set of possible left-hand sides for such a system of equations will always be a regular (even local) language.
This lets us exploit a property of languages called [compactness](https://scholar.google.com/scholar?cluster=17932744912598753020&hl=de&as_sdt=0,5) which says that any language has a finite subset which differentiates the same string morphisms as the whole language. 
In the case of regular languages there is an [efficient algorithm](https://scholar.google.com/scholar?cluster=8987949344652779872&hl=de&as_sdt=0,5) for constructing such sets.

The second challenge is rooted in the fact that the problem of solving a such equation is already NP-complete.
The solution lies in identifying what exactly makes the hard cases hard. 
The field of parametrized complexity is all about finding additional parameters for problems which are intractable when only the size of the input is considered. 
A problem is fixed-parameter tractable when fixing such additional parameters results in a tractable problem with respect to input size. 
There are two types of parametrizations that are particularly promising for our problem: one based in [structure](https://scholar.google.com/scholar?cluster=8302488406971799490&hl=de&as_sdt=0,5) and one in [bounding output delay/epenthesis](https://scholar.google.com/scholar?cluster=16324329046130129306&hl=de&as_sdt=0,5). 
Another handy fact is that we can collapse our systems of equations into single equations with a polynomial blow up in size using some [tricks](https://scholar.google.com/scholar?cluster=3610505661209871121&hl=de&as_sdt=0,5).
