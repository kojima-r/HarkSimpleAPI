import argparse


parser = argparse.ArgumentParser()
parser.add_argument("name", type=str, help="train/infer")
parser.add_argument(
    "--tf", type=str, default=None,  help="tf"
)
parser.add_argument(
    "--target", type=str, default=None,  help="target"
)
parser.add_argument(
    "--thresh", type=str, default=None,  help="target"
)
args = parser.parse_args()
# config
config_tmpl="""
base=$(cd $(dirname $0); pwd)

## basic setting
org_work=$base/work
work=$base/{name}
main=$base
project={name}
target="{target}"


## HARK setting ##
hark_tmpl="./localize_sep.n.tmpl"

hark_tf="{tf}"

hark_src_num=3
hark_thresh={thresh}
hark_lowest_freq=2200

hark_pause=1200
hark_min_interval_src=15
hark_lowest_freq_ghdss=1000
"""
config_str=config_tmpl.format(**{"name":args.name, "tf":args.tf, "target":args.target, "thresh":args.thresh})
fp=open("config/config_"+args.name+".sh","w")
fp.write(config_str)

