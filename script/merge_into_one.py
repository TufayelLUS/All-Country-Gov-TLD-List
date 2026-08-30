import os

# NOTE: the txt files should be placed inside a folder named "domains" and running this code will merge the domains and subdomains into one input.txt file

skip_country = [
] # skip any tld as needed
limit_to_number = 0 # 0 = no limits, 1 = pick file containing the number of lines max given below
limits = 10000


with open('input.txt', mode='w', encoding='utf-8') as f:
    for ff in os.listdir('domains'):
        if ff.endswith('.txt') and not any(x in ff for x in skip_country):
            txt_f = open(os.path.join('domains', ff), mode='r', encoding='utf-8').read()
            lines = txt_f.split('\n')
            if limit_to_number and len(lines) < limits:
                f.write(txt_f + "\n")
            else:
                f.write(txt_f + "\n")

print("Done")
