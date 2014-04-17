import StringIO
import csv

def printsums(names, row, column):
    result = '=SUM('
    for idx, name in enumerate(names):
        if idx != 0:
            result = result + ', '
        result = result + name + '!' + column + str(row)
    result = result + ')'
    return result

def main():
    print '--- PAYDAY 2 PROGRESS SPREADSHEET GENERATOR ---'

    names    = []
    letters  = ['B', 'C', 'D', 'E']
    skip     = [12, 18, 23]
    missions = ['Bank Heist PRO', 'Bank Heist: Cash', 'Bank Heist: Deposit', 'Bank Heist: Gold PRO',\
                'Diamond Store', 'Go Bank', 'Jewelry Store', 'Transport: Crossroads',\
                'Transport: Downtown', 'Transport: Harbor', 'Transport: Park', 'Transport: Underpass',\
                'Firestarter', 'Firestarter PRO', 'Rats', 'Rats PRO', 'Watchdogs',\
                'Watchdogs PRO', 'Big Oil PRO', 'Election Day', 'Election Day PRO',\
                'Framing Frame', 'Framing Frame PRO', 'Four Stores', 'Mallcrasher',\
                'Nightclub', 'Ukrainian Job PRO']

    # Get names from input
    print 'Enter the list of names you want to use, separated by commas:'
    rawnameslist = raw_input()
    for name in rawnameslist.split(','):
        names.append(name.strip())

    # Generate spreadsheet csv files
    # Main sheet
    print 'Writing data to \'pd2-progress.tsv\'...'
    fmain = open('pd2-progress.tsv', 'w')
    fmain.write('---------------------------------------------------------------------\n'\
                'MAIN SHEET\n'\
                'Copy everything below this line to the main sheet of the spreadsheet:\n'\
                '---------------------------------------------------------------------\n')

    fmain.write('Mission\tHard\tVery Hard\tOverkill\tDeath Wish\n')
    fmain.write('Progress:\t=SUM(B3:B32)/(' + str(len(names)) + '*27)\t'\
                           '=SUM(C3:C32)/(' + str(len(names)) + '*27)\t'\
                           '=SUM(D3:D32)/(' + str(len(names)) + '*27)\t'\
                           '=SUM(E3:E32)/(' + str(len(names)) + '*27)\n')

    for number in range(0, len(missions)):
        # Blank line to separate missions from different contractors
        if number in skip:
            fmain.write('\t\t\t\t\n')

        # Print row
        finalstring = str(missions[number])
        for letter in letters:
            finalstring = finalstring + '\t' + printsums(names, number+3, letter)
        finalstring = finalstring + '\n'

        fmain.write(finalstring)


    # Write individual sheet
    fmain.write('\n\n---------------------------------------------------------------------\n'\
                'INDIVIDUAL SHEET\n'\
                'Copy everything below this line to the sheets for each name:\n'\
                '---------------------------------------------------------------------\n')
    fmain.write('Mission\tHard\tVery Hard\tOverkill\tDeath Wish\n')
    fmain.write('Progress:\t=SUM(B3:B32)/27\t'\
                            '=SUM(C3:C32)/27\t'\
                            '=SUM(D3:D32)/27\t'\
                            '=SUM(E3:E32)/27\n')

    for number in range(0, len(missions)):
        # Blank line to separate missions from different contractors
        if number in skip:
            fmain.write('\t\t\t\t\n')
        finalstring = str(missions[number]) + '\t0\t0\t0\t0\n'
        fmain.write(finalstring)

    fmain.close()

if __name__ == "__main__":
    main()

