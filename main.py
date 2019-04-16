import SSF_converter.SSF_to_Input as conv1
import SSF_converter.output_to_SSF as conv2
import morph_analyser.make_prediction as morph_analyser

main_file = "main_format.txt"
out_main_file = open(main_file, 'w', encoding='utf-8')

while 1:
	print("Please enter your input :",end=' ')
	inp = input().split()
	for i  in range(1,len(inp)+1):
		out_main_file.write(str(i)+'\t'+'open_bracket_here\n')
		out_main_file.write(str(i)+'.1'+'\t'+str(i-1)+'\t'+str(i)+'\t'+inp[i-1]+'\n')
	out_main_file.flush()
	output=	morph_analyser.main(inp)
	print(output)
