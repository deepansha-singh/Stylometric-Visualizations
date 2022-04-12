# code preprocessing

import sys
sys.path.append('../')

from corpora.preprocessing import Preprocessing

rom1 = Preprocessing('rom1')
freq1 = rom1.preprocessing()

rom2 = Preprocessing('rom2')
freq2 = rom2.preprocessing()

score = "SocialSent-historical_2000"



# corpora processing

import shifterator

processing = shifterator.Shift(freq1, freq2, score, score, handle_missing_scores="exclude")

jsd_shift = shifterator.JSDivergenceShift(processing.type2freq_1, processing.type2freq_2)
jsd_shift.get_shift_graph(system_names=["rom1", "rom2"])

# entropy_shift = shifterator.EntropyShift(processing.type2freq_1, processing.type2freq_2)
# entropy_shift.get_shift_graph(system_names=['rom1', 'rom2'])