



dict = { 0:[summary], 1:[], 2:[location, summary], 3:[desciption], 4:[summary], 5:[summary] }


def main():
    file = open(file, 'r')
    new_file = open(new_file, 'w')
    
    while 1:
        line = file.readline()
        
        if 'SUMMARY:' not in line:
            new_file.write(file)
            
        else:
            buffer = ''
            summary = ''
            location = ''
            description = ''
            
            i = 0
            
            for char in line[7:]:
                if char != '\n':
                    buffer += char
                    continue
                
                if buffer[0] == '-':
                    buffer == ''
                
                for 
                
    
    
    
        
        
        