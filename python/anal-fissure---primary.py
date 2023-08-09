# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"7739300.0","system":"readv2"},{"code":"J530.11","system":"readv2"},{"code":"J530000","system":"readv2"},{"code":"J530100","system":"readv2"},{"code":"J544.00","system":"readv2"},{"code":"1089.0","system":"med"},{"code":"10905.0","system":"med"},{"code":"12665.0","system":"med"},{"code":"15210.0","system":"med"},{"code":"18337.0","system":"med"},{"code":"1979.0","system":"med"},{"code":"62790.0","system":"med"},{"code":"928.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anal-fissure-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anal-fissure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anal-fissure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anal-fissure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
