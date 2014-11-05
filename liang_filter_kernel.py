#!/usr/bin/env python
# encoding: utf-8

import re
import os
import sys,shutil

search_list = ['/nokia/be_nmp/groups/seaa_wa/hongklia/athena/kernel/include','/nokia/be_nmp/groups/seaa_wa/hongklia/athena/kernel/arch/arm/include', '/nokia/be_nmp/groups/seaa_wa/hongklia/athena/kernel/arch/arm/mach-msm/include']
#search_list = ['/nokia/be_nmp/groups/seaa_wa/hongklia/athena/kernel/include'] #,
#'/nokia/be_nmp/groups/seaa_wa/hongklia/athena/kernel/arch/arm/include', 
#'/nokia/be_nmp/groups/seaa_wa/hongklia/athena/kernel/arch/arm/include
#'/nokia/be_nmp/groups/seaa_wa/hongklia/athena/kernel/arch/arm/mach-msm/include']

def check_h_file(aa,dd,pp):
    new_file = open(aa)    
    for each in new_file:
        if re.search(r'^#include\s*<',each):
#            print("next will proc "+str(each)+" .")
            wav = re.split(r'\<|\>',each)            
            #get the head file name 
            hit_flag = 0
            for ipath in search_list:
                ss = ipath + '/' + wav[1]
                #print("Now check "+str(ss)+" !")      
                if not dd.__contains__(ss):                    
                    if os.path.exists(ss):                    
                        dd[ss] =1
                        hit_flag = 1
                        new_ss = "/nokia/be_nmp/groups/seaa_wa/hongklia/aol3g/"
                        new_ss = ss.replace('/nokia/be_nmp/groups/seaa_wa/hongklia/athena',new_ss)
                        bb = os.path.split(new_ss)
                        if not os.path.exists(bb[0]):
                            os.makedirs(bb[0])
                        shutil.copyfile(ss,new_ss) 
                        #print("now we just copy the head file "+str(ss)+" .") 
                        break
                else:
                    hit_flag = 1      
            #print(" the hit_flag now is         
            if hit_flag ==0:
                print("The serach for head file "+str(wav[1])+" fail!")  
                #sys.exit(1)
        elif re.search(r'^#include\s*\"',each):
#            print("Next will proc "+str(each)+" .")
            wav = re.split(r'\"',each) 
            new_ss1 = pp + '/' +  wav[1]
            #print("Next will proc "+str(new_ss1)+" .")
            bb = os.path.split(new_ss1)
            if not os.path.exists(bb[0]):
                os.makedirs(bb[0])
            if not dd.__contains__(new_ss1):
                dd[new_ss1] =1
                if os.path.exists(wav[1]):
                    shutil.copyfile(wav[1],new_ss1)    
                else:
                    print("the head is missing "+str(wav[1])+" .")      
    return dd                    
                     

file_object = open("System.map")
file_dict   = {}

for ln in file_object:
    head_dict = {}
    if re.search(r'\/\w+\.\w+', ln):
        wav= re.split(r'\s+',ln)
        wave_1 = re.split(r':',wav[3])                
        #wave_2 = re.split(r'KERNEL_OBJ\/',wave_1[0])
        if re.search(r'\/out\/target',wave_1[0]):
            wave_other = re.split(r'out\/target\/',wave_1[0])
            aa=wave_1[0].replace(wave_other[0],'/nokia/be_nmp/groups/seaa_wa/hongklia/athena/')
            #print("The new part is "+str(aa)+" .") 
            wave_1[0] = aa
        
        if not os.path.exists(wave_1[0]):
            print("we don't have this file")
            sys.exit(1)  
        else:
            old_path = os.getcwd()
            wave_2 = os.path.split(wave_1[0])
            os.chdir(wave_2[0])
            current_path = os.getcwd()
            ss = current_path + '/' + wave_2[1]
            #try to set it into dict and copy it later
            if not file_dict.__contains__(ss):
                file_dict[ss] =1 
                #generate the target path
                wave_new = re.split(r'\/hongklia\/athena\/',current_path)
                new_ss = "/nokia/be_nmp/groups/seaa_wa/hongklia/aol3g/"
                new_ss = new_ss + wave_new[1]
                if not os.path.exists(new_ss):
                    os.makedirs(new_ss)
                
                #combine for the target file name
                new_ss1 = new_ss + "/" + wave_2[1]
                #print("Now we copy the file is "+str(new_ss1)+".")
                #copy the file there
                shutil.copyfile(wave_2[1],new_ss1)
                #check the head file
                head_dict = check_h_file(wave_2[1],head_dict,new_ss)
            os.chdir(old_path)            
                
print("the size for the file is "+str(len(file_dict.keys()))+" .")

file_object.close()

