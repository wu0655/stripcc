#add warning
1. copy stripcc and kernel.conf to /KERNEL/PATH
2. run ./stripcc -f kernel.conf ---->output is exclue_file_list.txt


#compile
1. drivers/video/msm/mdss/sii6400/Makefile
2. scripts/gcc-wrapper.py

make xxx 2>&1 | tee 1.log

#parse
python3 kernel_file_filter.py 3.log  ---output is compiled_files.txt
python3 gen_file_list.py /KERNEL/PATH compiled_files.txt exclue_file_list.txt ---->output is output.txt

#test
#remove the files which are not used in kernel

#recompile


#recover the souce files
git checkout *.c
git checkout *.h
.
.
.
