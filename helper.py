def helper(work):
    work_in_memory = work

    def helper(work):
        return f"I will help u with {work_in_memory}, after what we do {work}"
    return helper

helper = helper("homework")
print(helper("cleaning garden"))
print(helper("study"))