import os
file_in = "temp_SSF.txt"
error= "error.txt"
temp_file = "out.txt"

error1=open(error,'w',encoding='utf-8')
out_temp_file = open(temp_file, 'w', encoding='utf-8')
    
def file_writer(list_list):
    try:
        out_temp_file.write("\t".join(list_list)+'\n')
    except:
        error1.write("\t".join(list_list)+'\n')

def sentence_cleaner(sentence):
    group = []
    for word in sentence:
        if word[0]=='))':
            try:
                group.pop()
            except:
                pass
        elif word[1]=='((':
            try:
                group.append(word[2])
            except:
                pass
        else:
            atom = []
            atom.append(word[0])
            atom.append(word[1])
            try:
                atom.append(word[2])
                attribute_pair = word[3][7:-2].split(",")
                for each in attribute_pair:
                    atom.append(each)
                for each in group:
                    atom.append(each)
            except:
                pass
            file_writer(atom)
    out_temp_file.write('\n')

sentence_ = []
with open(file_in, 'r', encoding='utf-8') as f1:
    for line in f1:
        if line != '\n':
            pair = line.strip().split('\t')
            sentence_.append(pair)
        else:
            sentence_cleaner(sentence_)
            sentence_.clear()
sentence_cleaner(sentence_)