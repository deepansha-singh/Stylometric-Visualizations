# code preprocessing

import sys
sys.path.append('../')

from corpora.preprocessing import Preprocessing

rom1 = Preprocessing('rom1')
freq1 = rom1.preprocessing()

rom2 = Preprocessing('rom2')
freq2 = rom2.preprocessing()

score = "NRC-emotion_joy_English"



# corpora processing

import shifterator

processing = shifterator.Shift(freq1, freq2, score, score, handle_missing_scores="exclude")

weighted_avg_shift = shifterator.WeightedAvgShift(processing.type2freq_1, processing.type2freq_2, processing.type2score_1, processing.type2score_2)

weighted_avg_shift.get_shift_graph(system_names=["rom1", "rom2"], detailed="True", filename="Case Study 1")