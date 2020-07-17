name=$1
target=$2
tf=$3
thresh=$4
cd `dirname $0`

filename_tf=`basename ${tf}`
python scripts/make_config.py ${name} --tf ${filename_tf} --target ${target} --thresh ${thresh}

cfg=config/config_${name}.sh
echo -n "" >log/${name}.txt
sh ./01create_project.sh ${name} >> log/${name}.txt 2>&1
sh ./02init_hark.sh ${name} >> log/${name}.txt 2>&1
cp log/${name}.txt public/${name}/log.txt
