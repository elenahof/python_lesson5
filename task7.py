import json

report = []
with open('task_7.txt', 'r') as file:
    text = file.read()
    file.seek(0)
    profits = {}
    prof = {}
    profit_sum = 0
    for row in file:
        items = row.split(' ')
        profit = int(items[2]) - int(items[3])
        if profit > 0:
            prof.update({items[0]: profit})
            profit_sum += profit
        profits.update({items[0]: profit})
    report.append(profits)
    report.append({'average_profit': (profit_sum / len(prof))})

with open('task_7.json.tmp', 'w') as json_file:
    json.dump(report, json_file, ensure_ascii=False)

json_report = json.dumps(report, ensure_ascii=False)

print(f"Original list:\n{text}\n")
print(f"Loss-making companies:\n{report}\n")
print(f"JSON-format:\n{json_report}")