# Stylometric Visualisations

Stylometry is the statistical perusal of the difference in the diction of different wordsmiths. Its modern-day applications include literary studies, information retrieval, and many more.

There are many statistical measures available for analyzing a given text. However, most of them only consider the number of times a word appears in the text and, at most, their surprisals. Many formulae do not consider the context of word usage, its meaning, or even how the word intent changes through the years. These formulae are incomplete; in a sense, to minimize a text into just one number is astonishingly abstract but they are still popularly used.

Recently there has been a shift in the stylometric field from statistical analysis to visualization. Word shift graphs are the new trend. They are more effective as they consider all the factors that formulas did not, and also because the human brain is better at visualizing.

To understand the working of these graphs, we reviewed a few case studies, namely:

• 'Sentiment peculiarities of Moby Dick and U.S. urban parks'

• 'Information content of 280-character tweets,' 

• 'Employment diversity and urban resilience during the Great Recession'

• 'Average sentiment comparison of speeches by two United States presidents: Lyndon B. Johnson (1963–1969) and George W. Bush (2001–2009).' 

Afterwards, we set out to form our corpora and scrutinize them to get meaningful information.
We undertook this study to understand the shift mentioned above better.


## Shifterator

The Shifterator package provides functionality for constructing **word shift graphs**, vertical bart charts that quantify *which* words contribute to a pairwise difference between two texts and *how* they contribute. By allowing you to look at changes in how words are used, word shifts help you to conduct analyses of sentiment, entropy, and divergence that are fundamentally more interpretable.


## Documentation

[The documentation](https://shifterator.readthedocs.io/en/latest/) details how to create various kinds of word shift graphs with Shifterator, and includes a detailed cookbook for how to interpret, visualize, and work with word shifts.


See the following paper for more details on word shifts, and please cite it if you use them in your work:

> Gallagher, R. J., Frank, M. R., Mitchell, Lewis, Schwartz, A. J., Reagan, A. J., Danforth, C. M., Dodds, P. S. (2021). [Generalized Word Shift Graphs: A Method for Visualizing and Explaining Pairwise Comparisons Between Texts](https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-021-00260-3). *EPJ Data Science*, 10(4).
