base=$(cd $(dirname $0); pwd)

## basic setting
org_work=$base/work
work=$base/testtest
main=$base
project=testtest
target="audio/test_rectf00.wav"


## HARK setting ##
hark_tmpl="./localize_sep.n.tmpl"

hark_tf="tamago_rectf.zip"
#hark_tf="dacho_geotf_v3.zip"
#hark_tf="microcone_rectf.zip"

hark_src_num=3
hark_thresh=29.5
hark_lowest_freq=2200
hark_ch="&lt;Vector&lt;int&gt;&gt;"

hark_pause=1200
hark_min_interval_src=15
hark_lowest_freq_ghdss=1000

