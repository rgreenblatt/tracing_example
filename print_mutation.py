import inspect
from forbiddenfruit import curse


nesting_level = 0

whitelist = set()


def set_whitelist(whitelist_in):
    global whitelist
    whitelist = whitelist_in


def should_print():
    global nesting_level
    if nesting_level > 0:
        return False
    try:
        nesting_level += 1
        return inspect.stack()[2].filename in whitelist
    finally:
        nesting_level -= 1


orig_append = list.append


def my_append(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_append(self, *args, **kwargs)
    if is_print:
        print(f"<list_append> {old} -> {self}")

    return out


orig_extend = list.extend


def my_extend(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_extend(self, *args, **kwargs)
    if is_print:
        print(f"<list_extend> {old} -> {self}")

    return out


orig_remove = list.remove


def my_remove(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_remove(self, *args, **kwargs)
    if is_print:
        print(f"<list_remove> {old} -> {self}")

    return out


orig_insert = list.insert


def my_insert(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_insert(self, *args, **kwargs)
    if is_print:
        print(f"<list_insert> {old} -> {self}")

    return out


orig_pop = list.pop


def my_pop(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_pop(self, *args, **kwargs)
    if is_print:
        print(f"<list_pop> {old} -> {self}")

    return out


orig_reverse = list.reverse


def my_reverse(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_reverse(self, *args, **kwargs)
    if is_print:
        print(f"<list_reverse> {old} -> {self}")

    return out


orig_sort = list.sort


def my_sort(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_sort(self, *args, **kwargs)
    if is_print:
        print(f"<list_sort> {old} -> {self}")

    return out


orig_dict_pop = dict.pop


def my_dict_pop(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_dict_pop(self, *args, **kwargs)
    if is_print:
        print(f"<dict_pop> {old} -> {self}")

    return out


orig_dict_popitem = dict.popitem


def my_dict_popitem(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_dict_popitem(self, *args, **kwargs)
    if is_print:
        print(f"<dict_popitem> {old} -> {self}")

    return out


orig_dict_update = dict.update


def my_dict_update(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_dict_update(self, *args, **kwargs)
    if is_print:
        print(f"<dict_update> {old} -> {self}")

    return out


orig_set_add = set.add


def my_set_add(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_set_add(self, *args, **kwargs)
    if is_print:
        print(f"<set_add> {old} -> {self}")

    return out


orig_set_remove = set.remove


def my_set_remove(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_set_remove(self, *args, **kwargs)
    if is_print:
        print(f"<set_remove> {old} -> {self}")

    return out


orig_set_update = set.update


def my_set_update(self, *args, **kwargs):
    is_print = should_print()
    if is_print:
        old = str(self)
    else:
        old = None
    out = orig_set_update(self, *args, **kwargs)
    if is_print:
        print(f"<set_update> {old} -> {self}")

    return out


def activate():
    curse(list, "append", my_append)
    curse(list, "extend", my_extend)
    curse(list, "remove", my_remove)
    curse(list, "insert", my_insert)
    curse(list, "pop", my_pop)
    curse(list, "reverse", my_reverse)
    curse(list, "sort", my_sort)
    curse(dict, "pop", my_dict_pop)
    curse(dict, "popitem", my_dict_popitem)
    curse(dict, "update", my_dict_update)
    curse(set, "add", my_set_add)
    curse(set, "remove", my_set_remove)
    curse(set, "update", my_set_update)
