def find_shared_tags(tags1: str, tags2: str) -> set:
    tags1_list = tags1.split(",")
    tags2_list = tags2.split(",")

    tags1_clean = []
    for tag in tags1_list:
        tags1_clean.append(tag.strip())

    tags2_clean = []
    for tag in tags2_list:
        tags2_clean.append(tag.strip())

    tags1_set = set(tags1_clean)
    tags2_set = set(tags2_clean)

    shared = tags1_set & tags2_set
    return shared
