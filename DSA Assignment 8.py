def can_swap_to_goal(s, goal):
    if len(s) != len(goal):
        return False

    diff_count = 0
    diff_indices = []

    for i in range(len(s)):
        if s[i] != goal[i]:
            diff_count += 1
            diff_indices.append(i)

        if diff_count > 2:
            return False

    return diff_count == 2 and s[diff_indices[0]] == goal[diff_indices[1]] and s[diff_indices[1]] == goal[diff_indices[0]]

# Example
s = "ab"
goal = "ba"
print(can_swap_to_goal(s, goal))  # Output: True
