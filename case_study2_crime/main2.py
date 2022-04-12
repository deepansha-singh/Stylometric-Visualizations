# code preprocessing

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

import shifterator

processing = shifterator.Shift(freq1, freq2, score1, score2, handle_missing_scores="exclude")

weighted_avg_shift = shifterator.WeightedAvgShift(processing.type2freq_1, processing.type2freq_2, processing.type2score_1, processing.type2score_2)

weighted_avg_shift.get_shift_graph(system_names=["crime1", "crime2"], detailed="True", filename="Case Study 2")