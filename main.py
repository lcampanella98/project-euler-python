import problems
import sys
import inspect
import re
import math


cls_members = inspect.getmembers(sys.modules[problems.__name__], inspect.isclass)
all_problems = []
problem_pattern = r'Problem(\d+)$'
for t in cls_members:
    match = re.match(problem_pattern, t[0])
    if match:
        all_problems.append(int(match.group(1)))
all_problems.sort()
print('\nProject Euler Problems:\n')
cols = 4
for i in range(0, len(all_problems) // cols + 1):
    line = []
    j = i
    inc = len(all_problems) // cols + 1
    while j < len(all_problems):
        line.append(str(all_problems[j]))
        j += inc
    print('\t\t'.join(line))

no_choice = True
p = 0
while no_choice:
    try:
        p = all_problems.index(int(input('\nEnter your choice:\n')))
    except ValueError:
        print('Invalid choice.')
    else:
        no_choice = False
p_name = 'Problem' + str(all_problems[p])
chosen_problem = None
for name, obj in cls_members:
    if name == p_name:
        chosen_problem = obj()
        break

print("Running " + chosen_problem.name + "...\n")
chosen_problem.run()
