import csv

with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['user_id', 'user_name', 'comment_qty'])
    writer.writerow([4535, 'alex', 490])
    writer.writerow([5496, 'sam', 96])
    writer.writerow([84033, 'jimmy', 9522])


with open('test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for line in reader:
        print(line)
