def coding_mad_libs():
    print("Welcome to Coding Mad Libs! Fill in the blanks with coding-related words.\n")

    # Collect inputs
    language = input("Enter a programming language: ")
    data_type = input("Enter a data type (e.g., int, string): ")
    function_name = input("Enter a funny function name: ")
    bug_type = input("Enter a type of bug (e.g., syntax, logic): ")
    emotion = input("Enter an emotion: ")
    tool = input("Enter a coding tool or library: ")
    action_verb = input("Enter a coding action verb (e.g., debug, refactor): ")
    error_message = input("Enter a fake error message: ")

    # The coding story
    story = f"""
    One day, I decided to code in {language}, my favorite language.
    I declared a variable using the {data_type} data type and named it 'chaos_mode'.
    Then I wrote a function called '{function_name}()' which was supposed to print 'Hello, World!'.

    But instead, it introduced a {bug_type} bug into my codebase.
    I felt extremely {emotion}, so I took a break and opened {tool} for help.
    After hours of trying to {action_verb} the code, I finally fixed it.

    When I ran the code again, it printed: '{error_message}'.
    I gave up and became a professional meme maker instead.
    """

    print("\nHere's your Coding Mad Libs story:")
    print(story)

# Run the game
coding_mad_libs()
