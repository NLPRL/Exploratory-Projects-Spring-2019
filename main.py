import os
import SSF_converter.SSF_to_Input as conv1
import SSF_converter.output_to_SSF as conv2
import morph_analyser.make_prediction as morph_analyser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR+='/SSF_converter/'
main_file = BASE_DIR+"main_format.txt"


def main_format_writer(data):
	out_main_file = open(main_file, 'w', encoding='utf-8')
	for each in main_format_data:
		out_main_file.write('\t'.join(each)+'\n')
	out_main_file.write('\n')
	out_main_file.close()

while 1:
	print("Please enter your input :",end=' ')
	inp = input().split()
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
	print(output[0])
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
	print(main_format_data)
	main_format_writer(main_format_data)
	conv2.func()
