def find_common_participants(first_str, second_str, split=','):
    first_set = set(first_str.split(split))
    second_set = set(second_str.split(split))

    result = list(first_set.intersection(second_set))
    result.sort()

    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, split='|'))
