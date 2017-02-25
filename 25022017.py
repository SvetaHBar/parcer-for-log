path ="C:\\Users\\Sveta\\Desktop\\py\\logfile.txt"
string1 = "|ERROR|"
string2 = "STATISTICS"
string3 = "Command"
string4 = "dx version"
import time
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
commands = {}  # empty dict for keep all relevant cmd and durations
column_name_list = ["command", "duration1", "duration2", "duration3"]
table = ['<htm><body><table border = "1">']

def is_cmd_duration_ivent_in_line(line):
    line_words = line.split()
    if string1 in line_words or string2 in line_words:
        return True
    else:
        return False


def decode_line(line_words):
    print(line_words)
    return line_words[1], line_words[3]

def collect_data(path):
    with open(path) as inputfile:
        for line in inputfile:
            if is_cmd_duration_ivent_in_line(line):
                cmd, duration = decode_line(line.split())
                if cmd in commands:
                    commands[cmd].append(duration)
                else:
                    commands[cmd] = [duration]
         #collect_data(path)


# print function for debuging only

def print_table(cmds):
    #print( "\t".join(column_name_list))
    print("{: >20} {: >20} {: >20} {: >20}".format(*column_name_list))
    #    print "{: >20} {: >20} {: >20} {: >20}".format(*"\t".join(column_name_list))
    print(cmds)
    for cmd, durations in cmds.items():
        normalized_durations = normalize_list(durations, 3)
        print("{: >20} {: >20} {: >20} {: >20}\n".format(cmd, normalized_durations[0], normalized_durations[1], normalized_durations[2]))
        #print "{: >20} {: >20} {: >20} {: >20}".format(*([cmd] + durations))
        #print ("\t".join([cmd] + durations))

print_table(commands)        # call to print_table function

def normalize_list(original_list, target_len):
    normalized_list = original_list + target_len * ["N/A"]
    normalized_list = normalized_list[:target_len]
    return normalized_list



def create_output_file():
    with open('outputfile' + timestamp,'w+') as outputfile:
        outputfile.write("{: >20} {: >20} {: >20} {: >20}".format(*column_name_list) + "\n")
        #outputfile.write("\t".join(column_name_list) + "\n")     #print headers
        for cmd, durations in commands.items():
            normalized_durations = normalize_list(durations, 3)
            outputfile.write("{: >20} {: >20} {: >20} {: >20}\n".format(cmd, normalized_durations[0], normalized_durations[1], normalized_durations[2]))
            #outputfile.write("{: >20} {: >20} {: >20} {: >20}".format(*([cmd] + duration))+ "\n")
            #outputfile.write("\t".join([cmd] + duration) + "\n")



def main():
    collect_data(path)
    create_output_file()
if __name__ == '__main__':
    main()