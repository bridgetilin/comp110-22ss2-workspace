def dict_transform(a: dict[int, list[int]]) -> dict[int, list[int]]:
    for key in a: 
        for i in range(len(a[key])):
            a[key][i] *= key
    return a

def average_grades(grades: dict[str, list[int]]) -> dict[str, float]:
    averages: dict[str, float]
    for student in grades:
        total: int = 0 
        for grade in grades[student]: 
            total += grade
        averages[student] = total / len(grades[student])
    return averages