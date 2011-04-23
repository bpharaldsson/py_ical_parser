
# python 3.2


dict = { 0:[summary], 1:[], 2:[location, summary], 3:[desciption], 4:[summary], 5:[summary] }


def main():
    file = sys.argv[1]
    new_file = sys.argv[2]
    
    file = open(file, 'r')
    new_file = open(new_file, 'w')

    while 1:
        line = file.readline()

        if 'SUMMARY:' not in line:
            new_file.write(line)

        else:
            summary     = []
            location    = []
            description = []

            words = line[7:].split('\n')

            for i, word in enum(words):
                if word[0] == '-': word = ''

                for list in dict[i]:
                    list.append(word)

            new_file.write('DESCRIPTION: ' + description)
            new_file.write('LOCATION: '    + location)
            new_file.write('SUMMARY: '     + ' '.join(summary))

    new_file.close()