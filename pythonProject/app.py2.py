def group_names(names):
    #  numbers of groups
    num_groups = 6
    max_names_per_group = 6

    #  the loop issuing names  lists
    for i, name in enumerate(names):
        grouped_names[i % 6].append(name)

    return grouped_names


def main():
    # Accept input  list of names from the user
    names = []
    print("Enter names one by one, and type 'done' when finished:")
    while True:
        name = input()
        if name.lower() == 'done':
            break
        names.append(name)

    # names of Groups
    grouped_names = group_names(names)

    # Display the final loop
    for i, group in enumerate(grouped_names, 1):
        print(f"Group {i}: {group}")


if __name__ == "__main__":
    main()
