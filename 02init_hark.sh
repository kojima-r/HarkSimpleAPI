#work=/export/vagrant/birds/birds_suzuki/localized_int_furu_0505_140_init1min2
#main=/home/vagrant/Service/WebAnnotationToolForBirds
#project=sample2

if [ $# != 1 ]; then
	echo "引数の数が間違っています！"
	exit 1
fi
name=$1
. config/config_${name}.sh


# run HARK
echo "... run HARK"
python setparam.py ${hark_tmpl} ${work} ${hark_src_num} ${hark_thresh} ${hark_lowest_freq} ${hark_pause} ${hark_min_interval_src} ${hark_lowest_freq_ghdss} ${hark_tf}
cd ${work}
echo $(pwd)
sh ./run.sh

cd ${main}
echo "cp ${work}/sep_files/*.wav  ./public/${project}/sep_files/"
rm ./public/${project}/sep_files/*
cp ${work}/sep_files/*.wav  ./public/${project}/sep_files/
cp ${work}/sep_files/*.png  ./public/${project}/sep_files/
cp config/config_${name}.sh ./public/${project}/config

