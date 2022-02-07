steps = []      # Actions
current = 14    # Goal state ()
while current != 1:
    parent = current//2  # Parent
    if current % (2*parent) == 1:   # Action from parent to current is Right
        steps.append("Right\t({} to {})".format(parent, current))
    else:   # Action from parent to current is Left
        steps.append("Left\t({} to {})".format(parent, current))
    current = parent    # Repeat for parent

for i in reversed(range(len(steps))):
    print(steps[i])
