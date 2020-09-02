import csv
def clean_data() -> dict:
    
    with open('list_breeds.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        d = {}
        the_list = []
        for line in csv_reader:
            the_list.append(line)
            
        the_string = the_list[1][0]
        the_string = the_string.split(",")
            
        for element in the_string:
            first_strip = element.strip('<a title="')
            first_strip = first_strip.strip('</a>')
            first_split = first_strip.split('" href="')

            if len(first_split)== 2:
                first_split[1] = first_split[1].split('">', 1)[0]
                d[first_split[0]] = first_split[1]
    
    return d

if __name__ == "__main__":
    breeed_dictionary = clean_data()
    print(breeed_dictionary)