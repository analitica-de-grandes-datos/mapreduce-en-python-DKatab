#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        fields = line.strip().split('   ')
        letter=fields[0]
        date=fields[1]
        value=fields[2]
        
        sys.stdout.write("{}\t{}\t{}\n".format(letter,date,value))