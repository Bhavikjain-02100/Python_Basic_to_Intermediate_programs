def update_scores(std_scor, n_std):
    std_scor.update(n_std)
    return std_scor

students = {'John': 85, 'Emma': 92}
new = {'Lucas': 78}
upd_std = update_scores(students, new)
print(upd_std)
