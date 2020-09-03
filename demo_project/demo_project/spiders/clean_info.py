import csv


def clean_lists(lst:list)->list:
    list_clean = []
    for element in lst:
        if "\xa0" in element: 
            y = element.replace(u'\xa0', ' ')
            list_clean.append(y.strip("<li>"))
        elif "\n" in element: 
            y = element.rstrip('\n')
            list_clean.append(y.strip("</li>\"\n"))

        elif "</li>" in element: 
            y = element.strip("</li>")
            list_clean.append(y.strip("</li>\""))
        else:
            list_clean.append(element.strip("<li>"))

    return list_clean




with open('info.csv','r') as csv_file:
    d = {}
    for line in csv_file:
        print(type(line))
        lst = line.split(",")
        print(lst)
        
        if ("<p>" in line and "</p>" in line):
            lst = line.split(',\"')
            #Cleaning Lifestyle
            lifestyle = lst[0]
            ll = lifestyle.strip('<p>')
            y = ll.replace(u'\xa0', ' ')
            lifestyle_final = y.strip('</p>')
            
            #Cleaning Health Problems
            healthP = lst[1]
            hl = healthP.split("</li>,")
            clean_hl = clean_lists(hl)

            #Cleaning Other Diseases
            OtherD = lst[2]
            dl = OtherD.split("</li>,")
            clean_dl = clean_lists(dl)
        


            # print(lifestyle_final)
            # print("----")
            # print(clean_hl )
            # print("----")
            # print(clean_dl)
            # print("----")
        
        else:
            headings = clean_lists(line.split(','))

    d[headings[0]] = lifestyle_final
    d[headings[1]] = clean_hl
    d[headings[2]] = clean_dl

    print(d)

            

        

    # # csv_file.close()

    with open('final_info.csv', 'w', newline='') as file:
        # field_names = headings
        writer = csv.DictWriter(file, headings)
        writer.writeheader()
        writer.writerow(d)





        
            






