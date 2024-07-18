import csv

list_of_matches = []


with open('matches .csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        list_of_matches.append(row)

# uniq seasons
# which season with max num of matches in list_of_matches
# which team won by max run
# which team won by closest margin by Runs 
# which team is most successful
seasons = []

count = 0
for i in list_of_matches:
    if count == 0:
        count += 1
        continue
    if i[1] not in seasons:
        seasons.append(i[1])

print(len(seasons))

team_won_max_runs = ''
curr = 0
count = 0
for i in list_of_matches:
    if count == 0:
        count += 1
        continue
    if int(i[11]) > int(curr):
        curr = i[11]
        team_won_max_runs = i[10]

print(team_won_max_runs)

count = 0
closest_margin = 100000000
team_with_closest_margin = []
for i in list_of_matches:
    if count == 0:
        count += 1
        continue 

    if int(i[11]) < int(closest_margin):
        team_with_closest_margin.clear()
        if i[10] not in team_with_closest_margin:
            team_with_closest_margin.append(i[10])
            

        closest_margin = i[11]
    elif int(i[11]) == int(closest_margin):
        if i[10] not in team_with_closest_margin:
            team_with_closest_margin.append(i[10])
print(team_with_closest_margin)
print(curr)



