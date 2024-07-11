from pprint import pprint
import csv
import re
# читаем адресную книгу в формате CSV в список contacts_list
pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
substr = r"+7(\2)\3-\4-\5 \6\7"

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#print(contacts_list)

tmp_list = []
for i in contacts_list:
  t_name = ' '.join(i[:4]).split(' ')
  #print(full_name)
  result = [t_name[0], t_name[1], (t_name[3] if t_name[2] == '' else t_name[2]), i[3], i[4], re.sub(pattern, substr, i[5]), i[6]]
  #print(result)
  tmp_list.append(result)
#pprint(tmp_list)
tmp_rez = {}
for i in tmp_list:
  for name, surname, middle_name, organization, position, phone, email in tmp_list:
    key = (name, surname)
    if key not in tmp_list:
      tmp_rez[key] = [[name, surname, middle_name, organization, position, phone, email]]
    else:
      tmp_rez[key].append([name, surname, middle_name, organization, position, phone, email])
res_list= list(tmp_rez.values())
#print(res_list)



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(res_list)
