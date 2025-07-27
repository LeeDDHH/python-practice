# utils/find.py
def find_one(data_list, condition_fn):
    for i, d in enumerate(data_list):
        if condition_fn(d):
            return i
    return None


def find_all(data_list, condition_fn):
    return [i for i, d in enumerate(data_list) if condition_fn(d)]
