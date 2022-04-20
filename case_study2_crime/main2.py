# code Preprocessing

"""
using the preprocessing code
created in the 'corpora' module
to refine and fine-tune raw data
as downloaded from pure text files online.

Aim:
In this case study, we aim to analyze two popular
romance pieces of fiction, namely:
crime1 = Gone Girl (Gillian Flynn)
crime2 = The ABC Murders (Agatha Christie)
for their respective degree of 'joy' expressed.

Database:
We incorporate the SocialSent historical score dictionaries
for both 1930 and 2000 as a decade to account
for our reference values for words.
"""

import sys
sys.path.append('../')

from corpora.preprocessing import Preprocessing

crime1 = Preprocessing('crime1')
freq1 = crime1.preprocessing()

crime2 = Preprocessing('crime2')
freq2 = crime2.preprocessing()

score1 = "SocialSent-historical_1930"
score2 = "SocialSent-historical_2000"



# corpora processing

"""
deriving from the code by the conceptualization paper
for generalized word-shift graphs,
we call upon the shifterator module to perform the
weighted average shift for the two novels.

Assumption:
The words that have not been accounted for
in the considered score dictionary,
do not add on as a major contribution,
thus, have been overlooked/ excluded.

Output:
By setting the detailed parameter as 'true',
we are asking for a detailed, delta parameter inclusive
shift graph figure.
"""

import shifterator

processing = shifterator.Shift(freq1, freq2, score1, score2, handle_missing_scores="exclude")

weighted_avg_shift = shifterator.WeightedAvgShift(processing.type2freq_1, processing.type2freq_2, processing.type2score_1, processing.type2score_2)

weighted_avg_shift.get_shift_graph(system_names=["crime1", "crime2"], detailed="True", filename="Case Study 2")