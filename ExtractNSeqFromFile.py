



def extract_first_N_Sent_from_File(input_file_path, out_file_out, num_of_lines):
    fin = open(input_file_path, 'r', encoding='utf-8')
    fout = open(out_file_out, 'w', encoding='utf-8')
    c = 0
    for line in fin:
        line = line.strip().replace('\n', '').strip()
        if c < num_of_lines:
            fout.write(line+'\n')
            fout.flush()
        c = c+1
    fout.close()
    fin.close()


if __name__ == '__main__':

    extract_first_N_Sent_from_File('./sent.en.txt', './demo.100.en.txt', num_of_lines=100)
    extract_first_N_Sent_from_File('./sent.de.txt', './demo.100.de.txt', num_of_lines=100)
