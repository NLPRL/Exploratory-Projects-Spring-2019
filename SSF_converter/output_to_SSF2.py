import os
import queue
import SSF_converter.output_to_SSF as conv2

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR+='/'
# file_in = BASE_DIR+"main_format.txt"
# error= BASE_DIR+"error_conv2.txt"
# temp_file = "SSF.txt"

# error1=open(error,'w',encoding='utf-8')
# out_temp_file = open(temp_file, 'w', encoding='utf-8')
    
def file_writer(list_list):
    try:
        conv2.out_temp_file.write("\t".join(list_list)+'\n')
    except:
        conv2.error1.write("\t".join(list_list)+'\n')

def print_close_brackets():
    try:
        conv2.out_temp_file.write('\t'+'))'+'\n')
    except:
        conv2.error1.write('Unable to write in file'+'\n')

def print_open_brackets(pos,tag):
    try:
        conv2.out_temp_file.write(str(pos[0])+'\t'+'(('+'\t'+tag+'\n')
    except:
        conv2.error1.write('Unable to write in file at'+pos+'\n')


def main_call(pos,word):
    output = []
    output.append(str(pos[0])+'.'+str(pos[1]))
    try:
        output.append(word[3])
        output.append(word[4])
        tmp=','.join(word[5:12])
        tmp='<fs af='+tmp+'>'
        output.append(tmp)
    except:
        pass
    file_writer(output)

def sentence_builder(sentence):
    # bracket_sequence = queue.Queue(maxsize=100) 
    open_till=0
    # count_open=0
    # count_close=0
    pos = [0,0]
    for word in sentence:
        if word[1]=='open_bracket_here':
            continue
        else:
            if word[12][0] != 'I':
                pos[0]+=1
                pos[1]=0
                for num in range(open_till):
                    print_close_brackets()
                open_till=1
                if word[12][0]=='O':
                    print_open_brackets(pos,word[12])
                else:
                    print_open_brackets(pos,word[12][2:]) 
            else:
                pos[1]+=1
            main_call(pos,word)
    for num in range(open_till):
        print_close_brackets()
    conv2.out_temp_file.write('\n')
    conv2.out_temp_file.flush()


def func():
    sentence_ = []
    with open(conv2.file_in, 'r', encoding='utf-8') as f1:
        for line in f1:
            if line != '\n':
                pair = line.strip().split('\t')
                sentence_.append(pair)
            else:
                sentence_builder(sentence_)
                sentence_.clear()
    sentence_builder(sentence_)