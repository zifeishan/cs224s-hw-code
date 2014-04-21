tidigits=/afs/ir/class/cs224s/hw/hw3/data/TIDIGITS
train_cmd="run.pl"
decode_cmd="run.pl"


steps/align_si.sh --nj 4 --cmd "$train_cmd" \
  data/train data/lang exp/mono0a exp/mono0a_ali

steps/train_deltas.sh --cmd "$train_cmd" \
   $1 $2 data/train data/lang exp/mono0a_ali exp/tri1


utils/mkgraph.sh data/lang exp/tri1 exp/tri1/graph
steps/decode.sh --nj 10 --cmd "$decode_cmd" \
     exp/tri1/graph data/test exp/tri1/decode


# Getting results [see RESULTS file]
echo "=== Word Error Rates ==="
for x in exp/*/decode*; do [ -d $x ] && grep WER $x/wer_* | utils/best_wer.sh; done
echo "=== Sentence Error Rates ==="
for x in exp/*/decode*; do [ -d $x ] && grep SER $x/wer_* | utils/best_wer.sh; done

#exp/mono0a/decode/wer_17:%SER 3.67 [ 319 / 8700 ]
#exp/tri1/decode/wer_19:%SER 2.64 [ 230 / 8700 ]
