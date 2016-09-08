import sys
with open('/folder/'+sys.argv[1]) as f:
    with open('/folder/'+sys.argv[2], 'w') as out_file:
        for line in f:
            line_length = int(line[:6])
            segment_part = int(line[7:12])
            start = 13
            end = 13 + segment_part - 1
            while (end < line_length):
                out_file.write(line[start-1:end-6] + '\n')
                start = end + 1
                end = start + int(line[start-6:start-1]) - 1
