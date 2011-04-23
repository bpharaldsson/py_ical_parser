def main():
    file = open('C:\\Users\\sc1\\Desktop\\timeedit.ics', 'r')

    new_file = open('C:\\Users\\sc1\\Desktop\\time2.ics', 'w')

    while 1:
        line = file.readline()

        if line == '': break
        if ':' not in line: continue
    
        if line[0:8] != 'SUMMARY:':
            new_file.write(line)

        else:
            summary     = []
            location    = []
            description = []
            dict = { 0:[summary], 1:[], 2:[location, summary], 3:[description], 4:[summary], 5:[summary] }
            translations = { 'F0006T' : 'Fysik', 'M0032M': 'Matte' }

            words = line[8:].split('\\n')

            for i, word in enumerate(words):
                word = translations.get(word, word)
                if '-' in word: word = ''

                for list in dict.get(i, []):
                    list.append(word)

            new_file.write('DESCRIPTION:' + ' '.join(description)    + '\n')
            new_file.write('LOCATION:'    + ' '.join(location)     + '\n')
            new_file.write('SUMMARY:'     + ' '.join(summary) + '\n')

            

    new_file.close()
    print('done')

if __name__ == '__main__':
    main()
