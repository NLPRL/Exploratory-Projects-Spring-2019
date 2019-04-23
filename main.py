import os
import SSF_converter.SSF_to_Input as conv1
import SSF_converter.output_to_SSF as conv2
import morph_analyser.make_prediction as morph_analyser
import Pos_Tagger.final_predict_model as pos_tagger

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR+='/SSF_converter/'
main_file = BASE_DIR+"main_format.txt"
local_add = os.path.dirname(os.path.abspath(__file__))
pos_tagger_input_file = local_add+'/Pos_Tagger/sentinput.txt'


def main_format_writer(data):
	out_main_file = open(main_file, 'w', encoding='utf-8')
	for each in main_format_data:
		out_main_file.write('\t'.join(each)+'\n')
	out_main_file.write('\n')
	out_main_file.flush()
	out_main_file.close()
def block_maker():
	for  i in range(80):
		conv2.out_temp_file.write('-')
	conv2.out_temp_file.write('\n\n')
	conv2.out_temp_file.flush()

while 1:
	block_maker()
	print("Please enter your input :",end=' ')
	inp = input().split()
	conv2.out_temp_file.write('New Sentence = '+' '.join(inp)+'\n\n')	
	main_format_data = []
	for i  in range(1,len(inp)+1):
		temp = []
		temp.append(str(i))
		temp.append('open_bracket_here')
		main_format_data.append(temp)
		# out_main_file.write(str(i)+'\t'+'open_bracket_here\n')
		temp = []
		temp.append(str(i)+'.1')
		temp.append(str(i-1))
		temp.append(str(i))
		temp.append(inp[i-1])
		main_format_data.append(temp)
		# out_main_file.write(str(i)+'.1'+'\t'+str(i-1)+'\t'+str(i)+'\t'+inp[i-1]+'\n')
	# out_main_file.write('\n')
	# out_main_file.flush()
	output=	morph_analyser.main(inp)
	# print(output[0])
	j=0
	for i in range(len(output)):
		while main_format_data[j][1]=='open_bracket_here':
			j+=1
		main_format_data[j].append(output[i][0][2])
		main_format_data[j].append(output[i][0][1])
		main_format_data[j].append('')
		main_format_data[j].append(output[i][0][3])
		main_format_data[j].append(output[i][0][4])
		main_format_data[j].append(output[i][0][5])
		main_format_data[j].append(output[i][0][6])
		main_format_data[j].append(output[i][0][7])
		main_format_data[j].append('')
		main_format_data[j].append('')			
		j+=1
	# print(main_format_data)
	main_format_writer(main_format_data)
	conv2.out_temp_file.write('\t\t***Output after Morph Analyser***\n\n')
	conv2.func()
	block_maker()
	pos_tagger_input = open(pos_tagger_input_file, 'w', encoding='utf-8')
	# pos , gender , number, person, case ,tam
	for j in range(len(main_format_data)):
		if main_format_data[j][1]=='open_bracket_here':
			continue
		temp=main_format_data[j][3]
		for k in range(7,12):
			temp+='\t'+main_format_data[j][k]
		temp+='\n'
		pos_tagger_input.write(temp)
	pos_tagger_input.flush()
	pos_tagger_input.close()
	conv2.out_temp_file.write('\t\t***Output after POS Tagger***\n\n')	
	output = pos_tagger.pos_main()
	# print(output)
	i=0
	for j in range(len(main_format_data)):
		if main_format_data[j][1]=='open_bracket_here':
			continue
		main_format_data[j][4]=output[0][i]
		i+=1
	main_format_writer(main_format_data)
	conv2.func()
