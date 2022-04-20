# code preprocessing

"""
using the preprocessing code
created in the 'corpora' module
to refine and fine-tune raw data
as downloaded from pure text files online.

Aim:
In this case study, we aim to analyze two popular
romance pieces of fiction, namely:
rom1 = The Problem With Forever (Jennifer L. Armentrout)
rom2 = It Ends With Us (Colleen Hoover)
for their respective degree of 'joy' expressed.

Database:
We incorporate the NRC Emotion score dictionary to account
for our reference values for words.
"""

import sys
sys.path.append('../')

from corpora.preprocessing import Preprocessing

rom1 = Preprocessing('rom1')
freq1 = rom1.preprocessing()

rom2 = Preprocessing('rom2')
freq2 = rom2.preprocessing()

score1 = "NRC-emotion_joy_English"
score2 = "NRC-emotion_sadness_English"


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

processing1 = shifterator.Shift(freq1, freq2, score1, score1, handle_missing_scores="exclude")

weighted_avg_shift = shifterator.WeightedAvgShift(processing1.type2freq_1, processing1.type2freq_2, processing1.type2score_1, processing1.type2score_2)

weighted_avg_shift.get_shift_graph(system_names=["rom1", "rom2"], detailed="True", filename="Case Study 1 - Joy")



processing2 = shifterator.Shift(freq1, freq2, score2, score2, handle_missing_scores="exclude")

weighted_avg_shift = shifterator.WeightedAvgShift(processing2.type2freq_1, processing2.type2freq_2, processing2.type2score_1, processing2.type2score_2)

weighted_avg_shift.get_shift_graph(system_names=["rom1", "rom2"], detailed="True", filename="Case Study 1 - Sadness")