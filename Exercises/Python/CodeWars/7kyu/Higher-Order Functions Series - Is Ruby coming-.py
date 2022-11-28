def is_ruby_coming(lst):
    for i in lst:
        if i["language"] == "Ruby":
            return True
    return False