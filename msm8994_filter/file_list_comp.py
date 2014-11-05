import sys

kern_files = []

def main_func(file1, file2):
    fp1 = open(file1)
    fp2 = open(file2)
    
    
    fp1_list=[]
    line_num = 0
    for line in fp1:
        line_num = line_num + 1
        try:
            fp1_list.index(line)
            print(line)
        except:    
            fp1_list.append(line)
    print("line_num=%d" %(line_num))
    print("fp1_list line = %d" %(len(fp1_list)))

    fp2_list=[]
    line_num = 0
    for line in fp2:
        line_num = line_num + 1
        try:
            fp2_list.index(line)
        except:    
            fp2_list.append(line)
    print("line_num=%d" %(line_num))
    print("fp2_list line = %d" %(len(fp2_list)))
    
    for line in fp2_list:
        try:
            fp1_list.index(line)        
        except:
            print(line + "line + is not found in " + file1 + "but in " + file2)
            continue
            
    
    
    for line in fp1_list:
        try:
            fp2_list.index(line)
        except:
            print(line,end=" ")
            print(" is not found in " + file2 + "but in " + file1)
            continue
            
        
if __name__ == "__main__":
    print(sys.argv)
    main_func(sys.argv[1],sys.argv[2])
