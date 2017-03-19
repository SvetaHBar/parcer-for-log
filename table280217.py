path ="C:\\Users\\svetah\\Desktop\\py\\logfile.txt"
path1 ="C:\\Users\\svetah\\Desktop\\py\\UpdaterServiceLog.txt"
string1 = "|ERROR|"
string2 = "STATISTICS"
Runtime = "Runtime"
DXver = "DesignXpertVersion"
TLver = "InstalledContentDbVersion"

import time
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
commands = {}  # empty dict for keep all relevant cmd and durations
versions = {} # empty dict for keep all basic data
column_name_list = ["command", "duration1", "duration2", "duration3"]


def is_basic_data_from_line(line):
    line_versions = line.split()
    if Runtime in line_versions or DXver in line_versions or TLver in line_versions:
        return True
        print "finally yes"
    else:
        return False


def is_cmd_duration_ivent_in_line(line):
    line_words = line.split()
    if string1 in line_words or string2 in line_words:
        return True
    else:
        return False

def decode_line(line_words):
    print line_words
    return line_words[1], line_words[3]

def get_version_from_line(version_type, line_words):
    try:
        version_type_index = line_words.index(version_type)  #this row return version type index
        if line_words[version_type_index + 1] == "=":
            return line_words[version_type_index + 2]
    except ValueError:
        pass
    return None

def unitest():
    print(get_version_from_line(Runtime, ["Runtime", "=", "18.0.0.17"]))

    #print line_versions
    #return line_versions[DXver] ,line_versions[Runtime], line_versions[TLver]


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

def collect_basic_data(path1):
    with open(path1) as inputfile1:
        for line in inputfile1:
           if is_basic_data_from_line(line):
               version = get_version_in_line(line.split())
               #Runtime, DXver, TLver = line.split()  # lo nahon , ki kol ereh be shura nefredet az zarih lishol im ereh v shura im ken ma osim
               if version in versions:
                   versions[Runtime].append(DXver)
               else:
                   versions[Runtimes].append(TLver)






# print function for debuging only

def print_table(cmds):
    print("{: >20} {: >20} {: >20} {: >20}".format(*column_name_list))
    print(cmds)
    for cmd, durations in cmds.items():
        normalized_durations = normalize_list(durations, 3)
        print("{: >20} {: >20} {: >20} {: >20}\n".format(cmd, normalized_durations[0], normalized_durations[1], normalized_durations[2]))
    for Runtime, DXver, TLver in versions.items():
        print("{: >20} {: >20} {: >20} {: >20}".format(Runtime, DXver, TLver +"\n"))


def normalize_list(original_list, target_len):
    normalized_list = original_list + target_len * ["N/A"]
    normalized_list = normalized_list[:target_len]
    return normalized_list

def create_output_file():
    with open('outputfile' + timestamp,'w+') as outputfile:
        for Runtime, DXver, TLver in versions.items():
            #outputfile.write("{: >20} {: >20} {: >20} {: >20}".format(Runtime, DXver, TLver +"\n")
            outputfile.write("{: >20} {: >20} {: >20} {: >20}".format(*column_name_list) + "\n") #print headers
                #outputfile.write("\t".join(column_name_list) + "\n")
        for cmd, durations in commands.items():
            normalized_durations = normalize_list(durations, 3)
            outputfile.write("{: >20} {: >20} {: >20} {: >20}\n".format(cmd, normalized_durations[0], normalized_durations[1], normalized_durations[2]))




def main():
    collect_data(path)
    collect_basic_data(path1)
    create_output_file()
    unitest()
if __name__ == '__main__':
    main()