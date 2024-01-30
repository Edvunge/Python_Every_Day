test_git = {
    'janeth': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phila': ['python', 'haskell'],
}

for name, test in test_git.items():
    print("\n" + name.title() + " 's favorite languages are:")
    for test in test:
        print("\t" + test.title())
