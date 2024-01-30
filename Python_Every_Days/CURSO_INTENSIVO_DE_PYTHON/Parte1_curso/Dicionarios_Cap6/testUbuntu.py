test_git = {
    'janeth': ['python', 'ruby'],
    'sarah': ['c'],
}

for name, test in test_git.items():
    print("\n" + name.title() + " 's favorite are:")
    for test in test:
        print("\t" + test.title())
