import sys
import platform
import os


def add_filename_to_list(file1,fp1_list):
    fp1 = open(file1)
    line_num = 0
    for line in fp1:
        line_num = line_num + 1
        line = line.strip()
        try:
            fp1_list.index(line)
            #print(line)
        except:    
            fp1_list.append(line)
            
    #print("line_num=%d" %(line_num))
    #print("fp1_list line = %d" %(len(fp1_list)))
    
    fp1.close()
    return fp1_list
    

            
        
if __name__ == "__main__":
    print(sys.argv)
    print(platform.system())
    source_code_file_path=sys.argv[1]
    
    """ add files to list """
    kern_files = []
    for filename in sys.argv[2:]:
        kern_files = add_filename_to_list(filename,kern_files)
    
    
    """ handle path split / and \
        note \ is expressed in '\\'
    """
    if("Windows" == platform.system()):
        platform_split_syn = '\\'
    else:
        """add later """
        pass
        
    example_line = kern_files[0]
    num1 = example_line.find('\\')
    num2 = example_line.find('/')
    
    if((num1 == -1) and (num2 > 0)):
        file_split_syn = '/'
    elif((num1 > 0) and (num2 == -1)):
        file_split_syn = '\\'
    else:
        print("Error: num1=%d num2=%d" %(num1,num2))
        print(example_line)
        sys.exit()
    
    if(platform_split_syn == file_split_syn):
        pass
    else:
        temp_list=[]
        for line in kern_files:
            strings = line.split(file_split_syn)
            temp_list.append(platform_split_syn.join(strings))
        kern_files = temp_list
    
    
    """ save to a file """
    outputfile = open('output.txt','w')
    
    if(source_code_file_path[-1] != platform_split_syn):
        source_code_file_path = source_code_file_path+platform_split_syn
        
    for line in kern_files:
        outputfile.write("%s%s\n" %(source_code_file_path,line))
    
    outputfile.close()
    
    print("finish. please check output.txt")