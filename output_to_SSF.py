import os
import queue

file_in = "out.txt"
error= "error_out.txt"
temp_file = "temp_out.txt"

error1=open(error,'w',encoding='utf-8')
out_temp_file = open(temp_file, 'w', encoding='utf-8')
    
def file_writer(list_list):
    try:
        out_temp_file.write("\t".join(list_list)+'\n')
    except:
        error1.write("\t".join(list_list)+'\n')

def print_close_brackets():
    try:
        out_temp_file.write('\t'+'))'+'\n')
    except:
        error1.write('Unable to write in file'+'\n')

def print_open_brackets(pos,tag):
    try:
        out_temp_file.write(pos+'\t'+'(('+'\t'+tag+'\n')
    except:
        error1.write('Unable to write in file at'+pos+'\n')

def main_call(word):
    output = []
    output.append(word[0])
    output.append(word[3])
    output.append(word[4])
    tmp=','.join(word[5:13])
    tmp='<fs af='+tmp+'>'
    output.append(tmp)
    file_writer(output)

def sentence_builder(sentence):
    bracket_sequence = queue.Queue(maxsize=100) 
    open_till=0
    count_open=0
    count_close=0
    for word in sentence:
        if word[1]=='open_bracket_here':
            bracket_sequence.put(word[0])
        else:
            new_close=int(word[1])-count_close
            open_till-=new_close
            for num in range(new_close):
                print_close_brackets()
            new_open=int(word[2])-count_open
            total_new=bracket_sequence.qsize()
            count_open=int(word[2])
            count_close=int(word[1])
            open_till+=total_new
            for itr in range(total_new):
                print_open_brackets(bracket_sequence.get(),word[12+open_till-itr])
            main_call(word)
    for num in range(count_open-count_close):
        print_close_brackets()
    out_temp_file.write('\n')

sentence_ = []
with open(file_in, 'r', encoding='utf-8') as f1:
    for line in f1:
        if line != '\n':
            pair = line.strip().split('\t')
            sentence_.append(pair)
        else:
            sentence_builder(sentence_)
            sentence_.clear()
sentence_builder(sentence_)