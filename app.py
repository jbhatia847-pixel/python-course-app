import streamlit as st
import io
import contextlib
from pathlib import Path

# Define project root directory relative to this file
BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "images" / "Shikshaa Simple Learn.jpeg"
# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Python Course for Beginners",
    page_icon="🐍",
    layout="wide"
)

# --- CUSTOM CSS ANIMATIONS ---
st.markdown("""
<style>
    /* 1. Animated Gradient Text for Main Title */
    .animated-title {
        background: linear-gradient(-45deg, #FF4B4B, #4B8BBE, #FFE873, #2E7D32);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 6s ease infinite;
        font-size: 2.8rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 2. Fade & Slide Up Animation for Headers & Content */
    .fade-in-up {
        animation: fadeInUp 0.8s ease-out forwards;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* 3. Subtle Typing / Pulse Glow for Subheaders */
    .sub-glow {
        color: #FAFAFA;
        border-left: 4px solid #4B8BBE;
        padding-left: 10px;
        animation: borderGlow 3s infinite alternate;
    }

    @keyframes borderGlow {
        from { border-color: #4B8BBE; }
        to { border-color: #FFE873; }
    }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if "current_topic" not in st.session_state:
    st.session_state.current_topic = None

if "should_scroll" not in st.session_state:
    st.session_state.should_scroll = False

# --- TOP SECTION (HEADER & LOGO) ---
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.image("images/Shikshaa Simple Learn.jpeg", use_container_width=True)

# Animated Main Title
st.markdown("<h1 class='animated-title'>Python Course for Absolute Beginners</h1>", unsafe_allow_html=True)
st.divider()

# --- HELPER FUNCTION: INTERACTIVE CODE PLAYGROUND ---
def python_playground(default_code="# Write your Python code here\nprint('Hello from Shikshaa!')", key_suffix="main"):
    st.markdown("<h3 class='sub-glow'>💻 Interactive Playground</h3>", unsafe_allow_html=True)
    
    # User code input box
    user_code = st.text_area(
        "Edit and run your code:",
        value=default_code,
        height=200,
        key=f"code_input_{key_suffix}"
    )

    # Run button
    if st.button("▶️ Run Code", key=f"run_btn_{key_suffix}"):
        st.markdown("**Output:**")
        
        # Buffer to capture print() output
        output_buffer = io.StringIO()
        
        try:
            # Redirect standard output to buffer and execute code safely
            with contextlib.redirect_stdout(output_buffer):
                exec(user_code, {"__builtins__": __builtins__})
            
            output_text = output_buffer.getvalue()
            
            if output_text:
                st.code(output_text, language="text")
            else:
                st.info("Code executed successfully with no output.")
                
        except Exception as e:
            # Display execution errors
            st.error(f"Execution Error: {e}")

# --- INTERACTIVE INTRODUCTION SECTION ---
st.markdown("<div class='fade-in-up'>", unsafe_allow_html=True)
st.header("Introduction to the Course")

# Warm Welcome Callout
st.info(
    "👋 **Welcome to Python!** Whether you want to automate tasks, build web apps, "
    "or dive into data science, this course is designed specifically for complete beginners. "
    "No prior coding experience required!"
)

st.image("images/What Does a Web Developer Do (and How Do I Become One)_.jpeg")
st.markdown("</div>", unsafe_allow_html=True)

# Personalization Selectbox
st.subheader("Let's Personalize Your Journey")
user_goal = st.selectbox(
    "What is your primary goal for learning Python?",
    [
        "Select an option...",
        "Build web apps & websites",
        "Automate repetitive daily tasks",
        "Learn Data Science & AI",
        "Just exploring out of curiosity",
    ]
)

if user_goal != "Select an option...":
    st.success(f"Great choice! Python is the perfect language for **{user_goal.lower()}**. We've got you covered!")

st.write("") # Layout spacer

# --- TABBED COURSE OVERVIEW & STANDALONE COMPILER ---
st.subheader("📚 Course Navigation")

tab1, tab2, tab3 = st.tabs(["💡 Why Python?", "🗺️ Start any topic", "⚡ Python Playground"])

with tab1:
    st.markdown("""
    * **Super Simple Syntax:** Python reads almost like plain English.
    * **In-Demand Skill:** Used by tech giants like Google, Netflix, and NASA.
    * **Versatile:** Build anything from basic scripts to machine learning models.
    """)

with tab2:
    # Helper to generate topic expanders with auto-scroll triggers
    def create_topic_item(topic_name):
        with st.expander(topic_name):
            if st.button(f"Start Lesson: {topic_name}", key=f"btn_{topic_name}"):
                st.session_state.current_topic = topic_name
                st.session_state.should_scroll = True  # Set scroll flag

    # Topic Items List
    create_topic_item("1. What Is Programming?")
    create_topic_item("2. Setting Up Python")
    create_topic_item("3. Your First Python Code")
    create_topic_item("4. print()")
    create_topic_item("5. Understanding Code")
    create_topic_item("6. What Is a Variable?")
    create_topic_item("7. Basic Data Types")
    create_topic_item("8. Basic Math")
    create_topic_item("9. Assignment")
    create_topic_item("10. input()")
    create_topic_item("11. if statement")
    create_topic_item("12. Comparison Operators")
    create_topic_item("13. else")
    create_topic_item("14. elif")
    create_topic_item("15. Combining Conditions")
    create_topic_item("16. while Loop")
    create_topic_item("17. for Loop")
    create_topic_item("18. break")
    create_topic_item("19. continue")
    create_topic_item("20. Understanding Strings")
    create_topic_item("21. String Slicing")
    create_topic_item("22. Basic String Methods")
    create_topic_item("23. f-Strings")
    create_topic_item("24. What Is a List?")
    create_topic_item("25. Basic List Methods")
    create_topic_item("26. Looping Through Lists")
    create_topic_item("27. Why Functions?")
    create_topic_item("28. Creating and Calling Functions")
    create_topic_item("29. Parameters")
    create_topic_item("30. What Is a Dictionary?")
    create_topic_item("31. Understanding Errors")
    create_topic_item("32. try / except")
    create_topic_item("33. Exception Patterns")
    create_topic_item("🟢 Project 1 — Calculator")
    create_topic_item("🟢 Project 2 — Number Guessing Game")
    create_topic_item("🟢 Project 3 — Rock Paper Scissors")
    create_topic_item("🟢 Project 4 — Quiz Game")
    create_topic_item("🟢 Project 5 — To-Do List")

with tab3:
    st.write("Use this standalone compiler to test out any custom Python code anytime!")
    python_playground(key_suffix="tab_compiler")



# ============================================================
# MASTER BEGINNER COURSE ENGINE — LESSONS 11–33 + PROJECTS
# ============================================================

LESSONS_11_TO_33 = {11: {'title': 'if statement',
      'intro': 'An `if` statement runs a block of code only when its condition is true.',
      'sections': [('Why do we need if?',
                    'Programs often need to decide whether something should happen.',
                    'is_ready = True\n\nif is_ready:\n\tprint("Start the game!")',
                    None),
                   ('The basic structure',
                    'An if statement has `if`, a condition, a colon, and an indented block.',
                    'if condition:\n\t# code to run',
                    None),
                   ('True condition',
                    'When the condition is True, the indented code runs.',
                    'has_key = True\n\nif has_key:\n\tprint("Open the door")',
                    None),
                   ('False condition',
                    'When the condition is False, Python skips that indented block.',
                    'has_key = False\n\nif has_key:\n\tprint("Open the door")',
                    None),
                   ('Indentation',
                    'Indentation tells Python which statements belong to the if block.',
                    'game_ready = True\n\nif game_ready:\n\tprint("Start")\n\tprint("Have fun!")',
                    None),
                   ('The colon',
                    'The colon is required after the condition.',
                    'if is_ready:\n\tprint("Go!")',
                    None),
                   ('Important separation',
                    'We are using Boolean values here. Comparison operators such as `>` and `==` are taught '
                    'next.',
                    'is_alive = True\n\nif is_alive:\n\tprint("Player is alive")',
                    None)],
      'practice': ['Create `has_key = True` and print a message inside an if block.',
                   'Create `lights_on = False` and observe that the block is skipped.',
                   'Create `game_started = True` and print two indented lines.'],
      'challenge': 'Create a `game_ready` variable and start the game only when it is True.',
      'challenge_code': 'game_ready = True\n\nif game_ready:\n\tprint("Game started!")',
      'quiz': [('What does if do?',
                ['Runs a block when a condition is true',
                 'Repeats forever',
                 'Creates a list',
                 'Defines a function'],
                'Runs a block when a condition is true'),
               ('What ends the if condition line?', [':', ';', '.', ','], ':'),
               ('What shows that code belongs to the if block?',
                ['Indentation', 'Capital letters', 'Quotation marks', 'A comma'],
                'Indentation'),
               ('What happens when the condition is False?',
                ['The block is skipped', 'The block always runs', 'The program loops', 'Python closes'],
                'The block is skipped')],
      'next': 12,
      'next_title': 'Comparison Operators',
      'next_desc': 'Next you will learn how Python compares values using operators such as >, <, >=, <=, ==, '
                   'and !=.'},
 12: {'title': 'Comparison Operators',
      'intro': 'Comparison operators compare values and produce a Boolean result: `True` or `False`.',
      'sections': [('Greater than `>`',
                    'Checks whether the left value is greater than the right.',
                    '10 > 5',
                    'Result: True'),
                   ('Less than `<`',
                    'Checks whether the left value is smaller than the right.',
                    '3 < 8',
                    'Result: True'),
                   ('Greater than or equal `>=`',
                    'True when the left value is greater than or equal to the right.',
                    '10 >= 10',
                    'Result: True'),
                   ('Less than or equal `<=`',
                    'True when the left value is smaller than or equal to the right.',
                    '10 <= 10',
                    'Result: True'),
                   ('Equal to `==`',
                    'Checks whether two values are equal. This is different from assignment `=`.',
                    '10 == 10',
                    'Result: True'),
                   ('Not equal `!=`', 'Checks whether two values are different.', '10 != 5', 'Result: True'),
                   ('Using comparisons with if',
                    'A comparison can be used as the condition of an if statement.',
                    'score = 75\n\nif score >= 50:\n\tprint("Passed")',
                    None),
                   ('Comparing strings',
                    'Strings can also be compared for equality.',
                    'name = "Alex"\nprint(name == "Alex")',
                    'The result is True.')],
      'practice': ['Write `10 > 7` and predict the result.',
                   'Write `4 <= 4` and predict the result.',
                   'Compare a `score` variable with 50 using `>=`.',
                   'Compare two names using `==`.',
                   'Check whether two numbers are different using `!=`.'],
      'challenge': 'Create a `health` variable and print whether it is greater than zero.',
      'challenge_code': 'health = 10\nprint(health > 0)',
      'quiz': [('Which means greater than?', ['>', '<', '==', '!='], '>'),
               ('Which means equal to?', ['=', '==', '>=', '<='], '=='),
               ('What is 5 < 10?', ['True', 'False'], 'True'),
               ('What is 5 != 5?', ['True', 'False'], 'False'),
               ('What does = mean?',
                ['Assignment', 'Comparison', 'Greater than', 'Less than'],
                'Assignment')],
      'next': 13,
      'next_title': 'else',
      'next_desc': 'Next you will learn how to provide a second path when an if condition is false.'},
 13: {'title': 'else',
      'intro': 'The `else` block runs when the condition in an `if` statement is false.',
      'sections': [('Why else?',
                    'It gives your program a second path.',
                    'has_key = True\n\nif has_key:\n\tprint("Open")\nelse:\n\tprint("Find the key")',
                    None),
                   ('Basic structure',
                    '`else` comes after the indented if block and also ends with a colon.',
                    'if condition:\n\t# True path\nelse:\n\t# False path',
                    None),
                   ('When if is true',
                    'Only the if block runs.',
                    'is_raining = False\n'
                    '\n'
                    'if is_raining:\n'
                    '\tprint("Take an umbrella")\n'
                    'else:\n'
                    '\tprint("No umbrella needed")',
                    None),
                   ('When if is false',
                    'The else block runs instead.',
                    'is_raining = True\n'
                    '\n'
                    'if is_raining:\n'
                    '\tprint("Take an umbrella")\n'
                    'else:\n'
                    '\tprint("No umbrella needed")',
                    None),
                   ('Exactly one path',
                    'In a simple if/else pair, one of the two branches runs.',
                    None,
                    None),
                   ('Indentation matters',
                    'Both branches need their own indented code.',
                    'if has_key:\n\tprint("Open")\nelse:\n\tprint("Closed")',
                    None)],
      'practice': ['Use if/else with `has_key`.',
                   'Use if/else with `game_over`.',
                   'Make an open/closed door program.'],
      'challenge': 'Create a treasure-door program that prints one message when the player has a key and '
                   'another when they do not.',
      'challenge_code': 'has_key = False\n'
                        '\n'
                        'if has_key:\n'
                        '\tprint("Door opened!")\n'
                        'else:\n'
                        '\tprint("Find the key!")',
      'quiz': [('What does else handle?',
                ['The false path', 'The true path', 'A loop', 'A function'],
                'The false path'),
               ('Does else need a condition?', ['No', 'Yes', 'Only with loops', 'Only with input'], 'No'),
               ('What follows else?', [':', ';', '.', ','], ':'),
               ('How many branches are in simple if/else?', ['Two', 'One', 'Three', 'Zero'], 'Two')],
      'next': 14,
      'next_title': 'elif',
      'next_desc': 'Next you will learn how to test another condition using `elif`.'},
 14: {'title': 'elif',
      'intro': '`elif` means “else if” and lets Python test another condition when earlier conditions were '
               'false.',
      'sections': [('Why elif?',
                    'Use it when a program has more than two possible cases.',
                    'level = 2\n\nif level == 1:\n\tprint("Easy")\nelif level == 2:\n\tprint("Normal")',
                    None),
                   ('Basic structure',
                    'An elif chain starts with if, followed by one or more elif blocks and optionally else.',
                    'if condition1:\n'
                    '\t# first case\n'
                    'elif condition2:\n'
                    '\t# second case\n'
                    'else:\n'
                    '\t# final case',
                    None),
                   ('Python checks in order',
                    'Python checks the chain from top to bottom and uses the first matching branch.',
                    None,
                    None),
                   ('Multiple elif blocks',
                    'There can be several elif branches.',
                    'day = 2\n'
                    '\n'
                    'if day == 1:\n'
                    '\tprint("Monday")\n'
                    'elif day == 2:\n'
                    '\tprint("Tuesday")\n'
                    'elif day == 3:\n'
                    '\tprint("Wednesday")',
                    None),
                   ('elif without else',
                    'The final else is optional.',
                    'choice = "map"\n'
                    '\n'
                    'if choice == "sword":\n'
                    '\tprint("Sword")\n'
                    'elif choice == "map":\n'
                    '\tprint("Map")',
                    None),
                   ('Practical example',
                    'Elif is useful for several levels of a game or several menu choices.',
                    'score = 80\n'
                    '\n'
                    'if score >= 90:\n'
                    '\tprint("A")\n'
                    'elif score >= 75:\n'
                    '\tprint("B")\n'
                    'elif score >= 50:\n'
                    '\tprint("C")\n'
                    'else:\n'
                    '\tprint("D")',
                    None)],
      'practice': ['Create a three-level difficulty system.',
                   'Make a weekday example with several elif branches.',
                   'Create an if/elif/else menu.'],
      'challenge': 'Build a traffic-light decision with red, yellow, and green cases.',
      'challenge_code': 'light = "yellow"\n'
                        '\n'
                        'if light == "red":\n'
                        '\tprint("Stop")\n'
                        'elif light == "yellow":\n'
                        '\tprint("Get ready")\n'
                        'else:\n'
                        '\tprint("Go")',
      'quiz': [('What does elif mean?', ['Else if', 'End loop', 'Equal if', 'Else input'], 'Else if'),
               ('Where does elif go?',
                ['Between if and else', 'Before if', 'After else', 'Instead of print'],
                'Between if and else'),
               ('Can there be several elif blocks?', ['Yes', 'No', 'Only one', 'Only in loops'], 'Yes'),
               ('What happens after a branch matches?',
                ['The remaining chain is skipped',
                 'All branches run',
                 'The program loops',
                 'Python restarts'],
                'The remaining chain is skipped')],
      'next': 15,
      'next_title': 'Combining Conditions',
      'next_desc': 'Next you will learn `and`, `or`, and `not`.'},
 15: {'title': 'Combining Conditions',
      'intro': 'Python can combine conditions with `and`, `or`, and `not`.',
      'sections': [('and',
                    'With `and`, every connected condition must be true.',
                    'has_key = True\nis_ready = True\n\nif has_key and is_ready:\n\tprint("Enter")',
                    None),
                   ('or',
                    'With `or`, at least one connected condition must be true.',
                    'has_sword = False\nhas_bow = True\n\nif has_sword or has_bow:\n\tprint("Can attack")',
                    None),
                   ('not',
                    '`not` reverses a Boolean value.',
                    'game_over = False\n\nif not game_over:\n\tprint("Keep playing")',
                    None),
                   ('Truth table idea',
                    'For `and`, think ALL. For `or`, think ANY. For `not`, think opposite.',
                    None,
                    None),
                   ('Parentheses',
                    'Parentheses can make complex conditions easier to read.',
                    'if (has_key and is_ready) or has_map:\n\tprint("Continue")',
                    None),
                   ('Game example',
                    'Combining conditions is useful for doors, attacks, inventory rules, and more.',
                    'health = 100\nhas_key = True\n\nif health > 0 and has_key:\n\tprint("Enter the castle")',
                    None)],
      'practice': ['Combine two Boolean values with `and`.',
                   'Combine two Boolean values with `or`.',
                   'Use `not` with a Boolean.',
                   'Create a game rule with two conditions.'],
      'challenge': 'Let a player enter a castle only when they have a key and are alive.',
      'challenge_code': 'has_key = True\nalive = True\n\nif has_key and alive:\n\tprint("Enter the castle")',
      'quiz': [('Which requires all conditions to be true?', ['and', 'or', 'not', 'else'], 'and'),
               ('Which needs at least one true condition?', ['or', 'and', 'not', 'elif'], 'or'),
               ('What is not True?', ['False', 'True', 'None', '0'], 'False'),
               ('What can help group a combined condition?',
                ['Parentheses', 'Quotes', 'Commas', 'Semicolons'],
                'Parentheses')],
      'next': 16,
      'next_title': 'while Loop',
      'next_desc': 'Next you will learn how to repeat code while a condition remains true.'},
 16: {'title': 'while Loop',
      'intro': 'A `while` loop repeats its block while its condition is true.',
      'sections': [('Why while?',
                    'A while loop is useful when repetition depends on a condition.',
                    'count = 1\n\nwhile count <= 3:\n\tprint(count)\n\tcount = count + 1',
                    None),
                   ('Basic structure',
                    'A while loop has a condition, colon, and indented body.',
                    'while condition:\n\t# repeated code',
                    None),
                   ('The condition controls repetition',
                    'Python checks the condition before each repetition.',
                    'is_playing = True\n\nwhile is_playing:\n\tprint("Playing")\n\tis_playing = False',
                    None),
                   ('Counters',
                    'Changing a counter is a common way to make a loop eventually stop.',
                    'lives = 3\n\nwhile lives > 0:\n\tprint(lives)\n\tlives = lives - 1',
                    None),
                   ('Infinite loops',
                    'If the condition never becomes false, the loop may continue forever.',
                    'count = 1\n'
                    '\n'
                    '# Be careful: do not forget to change count.\n'
                    'while count <= 3:\n'
                    '\tprint(count)\n'
                    '\tcount = count + 1',
                    None),
                   ('Common mistakes',
                    'Remember the colon, indentation, and a changing value or another exit condition.',
                    None,
                    None)],
      'practice': ['Print 1 to 5 using while.',
                   'Count down from 5 to 1.',
                   'Make a loop that repeats three times.'],
      'challenge': 'Create a countdown from 3 to 1 and then print Go!.',
      'challenge_code': 'count = 3\n\nwhile count > 0:\n\tprint(count)\n\tcount = count - 1\n\nprint("Go!")',
      'quiz': [('What does while do?',
                ['Repeats while a condition is true', 'Runs once', 'Creates a function', 'Creates a list'],
                'Repeats while a condition is true'),
               ('What can happen if the condition never becomes false?',
                ['Infinite loop', 'Automatic stop', 'Syntax change', 'Nothing'],
                'Infinite loop'),
               ('What ends the while condition line?', [':', ';', '.', ','], ':'),
               ('Which part repeats?',
                ['Indented body', 'Only keyword', 'Only condition', 'File name'],
                'Indented body')],
      'next': 17,
      'next_title': 'for Loop',
      'next_desc': 'Next you will learn another common way to repeat code: the `for` loop.'},
 17: {'title': 'for Loop',
      'intro': 'A `for` loop goes through items in a sequence or numbers in a range.',
      'sections': [('Why for?',
                    'Use a for loop when you want to process each item or a known range.',
                    'for number in range(5):\n\tprint(number)',
                    None),
                   ('Loop variable',
                    'The loop variable receives the current item on each repetition.',
                    'for name in ["Alex", "Mia", "Sam"]:\n\tprint(name)',
                    None),
                   ('range()',
                    '`range()` creates a sequence of numbers for the loop.',
                    'for number in range(1, 6):\n\tprint(number)',
                    'This prints 1 through 5.'),
                   ('Start and stop',
                    'The stop value is not included.',
                    'for number in range(2, 5):\n\tprint(number)',
                    'This prints 2, 3, 4.'),
                   ('Looping over a list',
                    'A for loop can directly visit list items.',
                    'items = ["Sword", "Key", "Potion"]\n\nfor item in items:\n\tprint(item)',
                    None),
                   ('Common mistakes',
                    'Remember the colon, indentation, and that `range(5)` starts at 0.',
                    None,
                    None)],
      'practice': ['Print 0 through 4.',
                   'Print 1 through 10.',
                   'Loop through an inventory list.',
                   'Print Hello five times.'],
      'challenge': 'Create a list of three enemies and print each enemy name with a for loop.',
      'challenge_code': 'enemies = ["Slime", "Wolf", "Goblin"]\n\nfor enemy in enemies:\n\tprint(enemy)',
      'quiz': [('What does a for loop commonly do?',
                ['Repeats for each item', 'Checks one condition', 'Stops a program', 'Handles errors'],
                'Repeats for each item'),
               ('What does range(5) start with?', ['0', '1', '5', '-1'], '0'),
               ('Is the stop value included?', ['No', 'Yes', 'Only sometimes', 'Always'], 'No'),
               ('What identifies the current item?',
                ['Loop variable', 'File name', 'Function name', 'Colon'],
                'Loop variable')],
      'next': 18,
      'next_title': 'break',
      'next_desc': 'Next you will learn how to stop a loop early with `break`.'},
 18: {'title': 'break',
      'intro': '`break` immediately stops the loop that contains it.',
      'sections': [('Why break?',
                    'Use break when the loop should end before it naturally finishes.',
                    'for number in range(10):\n\tif number == 5:\n\t\tbreak\n\tprint(number)',
                    None),
                   ('break stops everything in the loop',
                    'Once break runs, Python leaves that loop.',
                    'for item in ["key", "coin", "exit"]:\n\tif item == "exit":\n\t\tbreak\n\tprint(item)',
                    None),
                   ('break in while',
                    'break can also leave a while loop.',
                    'while True:\n\tprint("Running once")\n\tbreak',
                    None),
                   ('break with a search',
                    'A common pattern is to stop when the wanted item is found.',
                    'items = ["coin", "potion", "key"]\n'
                    '\n'
                    'for item in items:\n'
                    '\tif item == "key":\n'
                    '\t\tprint("Key found!")\n'
                    '\t\tbreak',
                    None),
                   ('Use it carefully',
                    'Know exactly when the break condition can happen so the loop behavior is predictable.',
                    None,
                    None)],
      'practice': ['Stop a loop when it reaches 3.',
                   'Stop when the item is `exit`.',
                   'Use break in a while loop.'],
      'challenge': 'Search an item list and stop as soon as the player finds a key.',
      'challenge_code': 'items = ["coin", "potion", "key", "map"]\n'
                        '\n'
                        'for item in items:\n'
                        '\tif item == "key":\n'
                        '\t\tprint("Found it!")\n'
                        '\t\tbreak',
      'quiz': [('What does break do?',
                ['Stops the loop', 'Skips one iteration', 'Starts a loop', 'Creates a list'],
                'Stops the loop'),
               ('Can break be used in a for loop?',
                ['Yes', 'No', 'Only with strings', 'Only with numbers'],
                'Yes'),
               ('Can break be used in a while loop?',
                ['Yes', 'No', 'Only once', 'Only in functions'],
                'Yes')],
      'next': 19,
      'next_title': 'continue',
      'next_desc': 'Next you will learn how to skip one loop iteration with `continue`.'},
 19: {'title': 'continue',
      'intro': '`continue` skips the rest of the current loop iteration and moves to the next one.',
      'sections': [('Why continue?',
                    'Use continue when one item should be skipped but the loop should keep going.',
                    'for number in range(5):\n\tif number == 2:\n\t\tcontinue\n\tprint(number)',
                    None),
                   ('break vs continue',
                    'Break ends the loop. Continue only skips the current iteration.',
                    None,
                    None),
                   ('continue with a list',
                    'You can skip unwanted items while processing a list.',
                    'for item in ["coin", "skip", "key"]:\n\tif item == "skip":\n\t\tcontinue\n\tprint(item)',
                    None),
                   ('continue in while',
                    'In while loops, make sure the condition can still change.',
                    'number = 0\n'
                    '\n'
                    'while number < 4:\n'
                    '\tnumber = number + 1\n'
                    '\tif number == 2:\n'
                    '\t\tcontinue\n'
                    '\tprint(number)',
                    None),
                   ('Common mistake',
                    'Skipping the update of a while-loop counter can create an infinite loop.',
                    None,
                    None)],
      'practice': ['Skip the number 3.',
                   'Skip an item called `potion`.',
                   'Compare break and continue by running small examples.'],
      'challenge': 'Print numbers 1 to 5 but skip 3.',
      'challenge_code': 'for number in range(1, 6):\n\tif number == 3:\n\t\tcontinue\n\tprint(number)',
      'quiz': [('What does continue do?',
                ['Skips the current iteration',
                 'Stops the loop',
                 'Starts a new program',
                 'Creates a variable'],
                'Skips the current iteration'),
               ('Which stops the entire loop?', ['break', 'continue', 'for', 'range'], 'break'),
               ('Which keeps the loop running?', ['continue', 'break', 'else', 'print'], 'continue')],
      'next': 20,
      'next_title': 'Understanding Strings',
      'next_desc': 'Next you will explore strings and the text they store.'},
 20: {'title': 'Understanding Strings',
      'intro': 'Strings are values used to store text. You will learn how text is represented and measured.',
      'sections': [('What is a string?',
                    'Text written inside quotation marks is a string.',
                    'name = "Anmol"\ngreeting = \'Hello\'',
                    None),
                   ('Single and double quotes',
                    'Both single and double quotation marks can create strings.',
                    'a = "Hello"\nb = \'Hello\'',
                    None),
                   ('Spaces are characters',
                    'Spaces inside the string are part of the stored text.',
                    'message = "Hello Python World"',
                    None),
                   ('Empty strings', 'A string can contain zero characters.', 'message = ""', None),
                   ('String length',
                    '`len()` gives the number of characters in a string.',
                    'word = "Python"\nprint(len(word))',
                    'The answer is 6.'),
                   ('Text vs number',
                    'Quotation marks make text; without them, a numeric literal is a number.',
                    'a = "15"\nb = 15',
                    None),
                   ('Strings in programs',
                    'Strings are used for names, messages, game titles, menus, and much more.',
                    'game = "Somnium"\nprint(game)',
                    None)],
      'practice': ['Create three string variables.',
                   'Print the length of a word.',
                   'Create an empty string.',
                   'Create a game title as a string and print it.'],
      'challenge': 'Create a game title, player name, and welcome message as strings, then print them.',
      'challenge_code': 'game = "Somnium"\n'
                        'player = "Arion"\n'
                        'message = "Welcome to the forest!"\n'
                        '\n'
                        'print(game)\n'
                        'print(player)\n'
                        'print(message)',
      'quiz': [('What is a string?', ['Text', 'Only numbers', 'A loop', 'A dictionary'], 'Text'),
               ('Which is a string?', ['"Hello"', '25', '3.14', 'True'], '"Hello"'),
               ('What does len() give?',
                ['Number of characters', 'The type', 'The last character', 'Always True'],
                'Number of characters')],
      'next': 21,
      'next_title': 'String Slicing',
      'next_desc': 'Next you will learn how to access characters and take sections of strings.'},
 21: {'title': 'String Slicing',
      'intro': 'Python uses indexes and slices to access parts of a string.',
      'sections': [('Indexes start at 0',
                    'The first character is at index 0.',
                    'word = "Python"\nprint(word[0])',
                    'Result: P'),
                   ('Access another character',
                    'Use the index inside square brackets.',
                    'word = "Python"\nprint(word[1])',
                    'Result: y'),
                   ('Negative indexes',
                    'Negative indexes count backward from the end.',
                    'word = "Python"\nprint(word[-1])',
                    'Result: n'),
                   ('Basic slicing',
                    'A slice uses `start:stop`, and the stop index is not included.',
                    'word = "Python"\nprint(word[0:2])',
                    'Result: Py'),
                   ('Start or stop can be omitted',
                    'Use `[:3]` for the beginning or `[2:]` for the rest.',
                    'word = "Python"\nprint(word[:3])\nprint(word[2:])',
                    None),
                   ('Step',
                    'A third value can tell Python how far to move between characters.',
                    'word = "Python"\nprint(word[::2])',
                    None),
                   ('Reverse a string',
                    'A step of `-1` reads characters backwards.',
                    'word = "Python"\nprint(word[::-1])',
                    'Result: nohtyP')],
      'practice': ['Print the first character of `Python`.',
                   'Print the first three characters.',
                   'Print the last character.',
                   'Reverse a word using slicing.'],
      'challenge': 'Take a game title, print its first three characters, and then print it backwards.',
      'challenge_code': 'title = "Somnium"\nprint(title[:3])\nprint(title[::-1])',
      'quiz': [('What is the first index?', ['0', '1', '-1', '2'], '0'),
               ('Is the stop index included in a slice?', ['No', 'Yes', 'Only sometimes', 'Always'], 'No'),
               ('What does [::-1] do?',
                ['Reverse the string', 'Delete it', 'Find length', 'Convert to int'],
                'Reverse the string')],
      'next': 22,
      'next_title': 'Basic String Methods',
      'next_desc': 'Next you will learn common tools for changing and checking text.'},
 22: {'title': 'Basic String Methods',
      'intro': 'String methods are built-in tools for working with text.',
      'sections': [('upper()', 'Makes letters uppercase.', 'name = "anmol"\nprint(name.upper())', None),
                   ('lower()', 'Makes letters lowercase.', 'name = "ANMOL"\nprint(name.lower())', None),
                   ('strip()',
                    'Removes whitespace from the beginning and end.',
                    'name = "  Alex  "\nprint(name.strip())',
                    None),
                   ('replace()',
                    'Replaces one piece of text with another.',
                    'message = "I like cats"\nprint(message.replace("cats", "games"))',
                    None),
                   ('split()',
                    'Splits text into pieces and returns a list.',
                    'text = "red blue green"\nprint(text.split())',
                    None),
                   ('startswith()',
                    'Checks whether text starts with specific characters.',
                    'name = "Anmol"\nprint(name.startswith("An"))',
                    None),
                   ('endswith()',
                    'Checks whether text ends with specific characters.',
                    'file_name = "game.py"\nprint(file_name.endswith(".py"))',
                    None),
                   ('Methods use parentheses',
                    'A method is called with parentheses after its name.',
                    'name.upper()',
                    None)],
      'practice': ['Make a word uppercase.',
                   'Make a word lowercase.',
                   'Remove extra spaces.',
                   'Replace one word with another.',
                   'Split a sentence into words.'],
      'challenge': 'Clean a player name by removing extra spaces and converting it to uppercase.',
      'challenge_code': 'player = "  arion  "\n'
                        'player = player.strip()\n'
                        'player = player.upper()\n'
                        'print(player)',
      'quiz': [('Which method makes text uppercase?',
                ['upper()', 'lower()', 'strip()', 'split()'],
                'upper()'),
               ('Which removes surrounding whitespace?',
                ['strip()', 'upper()', 'replace()', 'split()'],
                'strip()'),
               ('Which replaces text?', ['replace()', 'split()', 'lower()', 'upper()'], 'replace()'),
               ('Which can check the ending of a string?',
                ['endswith()', 'upper()', 'strip()', 'replace()'],
                'endswith()')],
      'next': 23,
      'next_title': 'f-Strings',
      'next_desc': 'Next you will learn a clean way to put variable values into text.'},
 23: {'title': 'f-Strings',
      'intro': 'f-strings make it easy to create messages that include variable values.',
      'sections': [('Why f-strings?',
                    'Programs often need a sentence that contains changing values.',
                    'name = "Alex"\nscore = 100',
                    None),
                   ('Basic syntax',
                    'Put `f` before the opening quote and values inside `{}`.',
                    'name = "Alex"\nprint(f"Hello, {name}!")',
                    None),
                   ('Multiple values',
                    'More than one value can be placed inside the same f-string.',
                    'name = "Alex"\nscore = 100\nprint(f"{name} scored {score} points.")',
                    None),
                   ('Simple expressions',
                    'Expressions can be placed inside braces.',
                    'score = 40\nbonus = 10\nprint(f"Total: {score + bonus}")',
                    None),
                   ('Formatting decimals',
                    'A format such as `:.2f` can show two decimal places.',
                    'price = 12.5\nprint(f"Price: {price:.2f}")',
                    None),
                   ('Game-style status',
                    'f-strings are useful for player HUD text and status messages.',
                    'name = "Arion"\n'
                    'health = 100\n'
                    'level = 5\n'
                    'print(f"{name} | HP: {health} | Level: {level}")',
                    None)],
      'practice': ['Print a greeting containing a name.',
                   'Print a player name and score in one sentence.',
                   'Print a level message.',
                   'Put a small calculation inside an f-string.'],
      'challenge': 'Create a player status line containing name, health, level, and score.',
      'challenge_code': 'name = "Arion"\n'
                        'health = 100\n'
                        'level = 3\n'
                        'score = 500\n'
                        '\n'
                        'print(f"{name} | HP: {health} | Level: {level} | Score: {score}")',
      'quiz': [('What letter starts an f-string?', ['f', 's', 'x', 'p'], 'f'),
               ('Where do values go?',
                ['Curly braces', 'Square brackets', 'Only parentheses', 'After the period'],
                'Curly braces'),
               ('Can one f-string contain several values?',
                ['Yes', 'No', 'Only numbers', 'Only strings'],
                'Yes')],
      'next': 24,
      'next_title': 'What Is a List?',
      'next_desc': 'Next you will learn how to store multiple values in a list.'},
 24: {'title': 'What Is a List?',
      'intro': 'A list stores multiple values together in an ordered collection.',
      'sections': [('Creating a list',
                    'Lists use square brackets with items separated by commas.',
                    'items = ["Sword", "Key", "Potion"]',
                    None),
                   ('Lists of numbers', 'A list can store numbers too.', 'scores = [10, 20, 30, 40]', None),
                   ('List order',
                    'Items keep their order, and each position has an index.',
                    'items = ["Sword", "Key", "Potion"]\nprint(items[0])',
                    'Result: Sword'),
                   ('List length',
                    'Use `len()` to find how many items are in a list.',
                    'items = ["Sword", "Key", "Potion"]\nprint(len(items))',
                    'Result: 3'),
                   ('Changing an item',
                    'A list item can be replaced using its index.',
                    'items = ["Sword", "Key", "Potion"]\nitems[1] = "Map"',
                    None),
                   ('Lists can store different types',
                    'Python lists can contain different kinds of values, although related values are often '
                    'clearer.',
                    'player = ["Arion", 100, True]',
                    None),
                   ('Common mistakes',
                    'Remember square brackets and remember that indexes start at 0.',
                    None,
                    None)],
      'practice': ['Create a list of three games.',
                   'Create a list of five numbers.',
                   'Print the first item.',
                   'Change one item.',
                   'Find the list length.'],
      'challenge': 'Create an inventory with four items and print the first item.',
      'challenge_code': 'inventory = ["Sword", "Potion", "Key", "Map"]\nprint(inventory[0])',
      'quiz': [('Which brackets create a list?', ['[]', '()', '{}', '<>'], '[]'),
               ('What is the first list index?', ['0', '1', '-1', '2'], '0'),
               ('Which function gives list length?', ['len()', 'type()', 'print()', 'range()'], 'len()')],
      'next': 25,
      'next_title': 'Basic List Methods',
      'next_desc': 'Next you will learn common methods for adding and removing list items.'},
 25: {'title': 'Basic List Methods',
      'intro': 'List methods let you add, remove, find, sort, and reorder items.',
      'sections': [('append()',
                    'Adds an item to the end.',
                    'items = ["Sword", "Key"]\nitems.append("Potion")',
                    None),
                   ('insert()',
                    'Adds an item at a specific index.',
                    'items = ["Sword", "Potion"]\nitems.insert(1, "Key")',
                    None),
                   ('remove()',
                    'Removes the first matching value.',
                    'items = ["Sword", "Key", "Potion"]\nitems.remove("Key")',
                    None),
                   ('pop()',
                    'Removes and returns an item, usually from the end.',
                    'items = ["Sword", "Key", "Potion"]\nitem = items.pop()',
                    None),
                   ('clear()', 'Removes all items.', 'items = ["Sword", "Key"]\nitems.clear()', None),
                   ('index() and count()',
                    '`index()` finds a position; `count()` counts matching values.',
                    'items = ["Potion", "Key", "Potion"]\n'
                    'print(items.index("Key"))\n'
                    'print(items.count("Potion"))',
                    None),
                   ('sort() and reverse()',
                    'These change the order of suitable list values.',
                    'numbers = [3, 1, 2]\nnumbers.sort()\nnumbers.reverse()',
                    None)],
      'practice': ['Append a new inventory item.',
                   'Remove an item.',
                   'Pop the last item.',
                   'Count repeated items.',
                   'Sort a list of numbers.'],
      'challenge': 'Build an inventory, add a potion, remove the key, and print the final list.',
      'challenge_code': 'inventory = ["Sword", "Key"]\n'
                        'inventory.append("Potion")\n'
                        'inventory.remove("Key")\n'
                        'print(inventory)',
      'quiz': [('Which adds to the end?', ['append()', 'remove()', 'clear()', 'index()'], 'append()'),
               ('Which removes a matching value?', ['remove()', 'append()', 'count()', 'sort()'], 'remove()'),
               ('Which removes and returns an item?', ['pop()', 'clear()', 'index()', 'reverse()'], 'pop()'),
               ('Which counts occurrences?', ['count()', 'sort()', 'insert()', 'append()'], 'count()')],
      'next': 26,
      'next_title': 'Looping Through Lists',
      'next_desc': 'Next you will combine lists with for loops.'},
 26: {'title': 'Looping Through Lists',
      'intro': 'A for loop can visit every item in a list one by one.',
      'sections': [('Basic loop',
                    'The loop variable receives each item in order.',
                    'items = ["Sword", "Key", "Potion"]\n\nfor item in items:\n\tprint(item)',
                    None),
                   ('Numbers',
                    'The same idea works with number lists.',
                    'scores = [10, 20, 30]\n\nfor score in scores:\n\tprint(score)',
                    None),
                   ('Loop with a condition',
                    'You can check each item as you loop.',
                    'items = ["coin", "key", "potion"]\n'
                    '\n'
                    'for item in items:\n'
                    '\tif item == "key":\n'
                    '\t\tprint("Found key")',
                    None),
                   ('Building a total',
                    'A variable can collect information while the loop runs.',
                    'scores = [10, 20, 30]\n'
                    'total = 0\n'
                    '\n'
                    'for score in scores:\n'
                    '\ttotal = total + score\n'
                    '\n'
                    'print(total)',
                    None),
                   ('Processing game items',
                    'Loops are a natural way to inspect inventories, enemies, quests, and other collections.',
                    None,
                    None)],
      'practice': ['Print every item in an inventory.',
                   'Print every score in a scores list.',
                   'Find a specific item.',
                   'Add all numbers in a list.'],
      'challenge': 'Loop through three enemies and print each enemy name.',
      'challenge_code': 'enemies = ["Slime", "Wolf", "Goblin"]\n\nfor enemy in enemies:\n\tprint(enemy)',
      'quiz': [('What does the loop variable receive?',
                ['Each item', 'The whole file', 'Only the first item', 'Only the length'],
                'Each item'),
               ('Can if be inside a for loop?', ['Yes', 'No', 'Only strings', 'Only numbers'], 'Yes'),
               ('What is a common reason to loop through a list?',
                ['Process each item', 'Create VS Code', 'Change the OS', 'Open a folder'],
                'Process each item')],
      'next': 27,
      'next_title': 'Why Functions?',
      'next_desc': 'Next you will learn why functions help organize larger programs.'},
 27: {'title': 'Why Functions?',
      'intro': 'Functions organize code into reusable pieces with meaningful names.',
      'sections': [('The repetition problem',
                    'Without functions, repeated actions may need repeated code.',
                    'print("Welcome")\nprint("Welcome")\nprint("Welcome")',
                    None),
                   ('A named block',
                    'A function groups related instructions under a name.',
                    'def greet():\n\tprint("Welcome")',
                    None),
                   ('Reuse',
                    'Once defined, the same function can be called whenever needed.',
                    'def greet():\n\tprint("Welcome")\n\ngreet()\ngreet()',
                    None),
                   ('Organization', 'Functions break a large program into understandable tasks.', None, None),
                   ('Action-oriented names',
                    'Names like `open_door()` or `start_game()` make code easier to read.',
                    'def open_door():\n\tprint("Door opened")',
                    None),
                   ('Definitions do not run automatically',
                    'Defining a function creates it; calling it runs it.',
                    'def say_hello():\n\tprint("Hello")\n\nsay_hello()',
                    None)],
      'practice': ['Identify repeated code that could become a function.',
                   'Write a function name for opening a chest.',
                   'Write a simple function that prints a message.'],
      'challenge': 'Create `start_game()` and call it once.',
      'challenge_code': 'def start_game():\n\tprint("Game started!")\n\nstart_game()',
      'quiz': [('Why use functions?',
                ['Reuse and organize code', 'Only to print', 'Only to create lists', 'Only to make loops'],
                'Reuse and organize code'),
               ('What does def do?',
                ['Defines a function', 'Runs a loop', 'Compares values', 'Reads input'],
                'Defines a function'),
               ('What makes a function run?',
                ['Calling it', 'Naming it', 'Saving the file', 'Indenting it only'],
                'Calling it')],
      'next': 28,
      'next_title': 'Creating and Calling Functions',
      'next_desc': 'Next you will learn the exact syntax for defining and calling your own functions.'},
 28: {'title': 'Creating and Calling Functions',
      'intro': 'Now you will learn the exact syntax used to define and call functions.',
      'sections': [('def',
                    'The `def` keyword begins a function definition.',
                    'def greet():\n\tprint("Hello")',
                    None),
                   ('Function name',
                    'Choose a clear name followed by parentheses.',
                    'def start_game():\n\tprint("Start!")',
                    None),
                   ('Colon and indentation',
                    'The colon begins the function body, and the body is indented.',
                    'def start_game():\n\tprint("Start!")\n\tprint("Good luck!")',
                    None),
                   ('Calling a function',
                    'Write the function name followed by parentheses to run it.',
                    'def greet():\n\tprint("Hello")\n\ngreet()',
                    None),
                   ('Calling multiple times',
                    'A function can be called more than once.',
                    'def jump():\n\tprint("Jump!")\n\njump()\njump()',
                    None),
                   ('Functions and variables',
                    'A function can use values available when it runs.',
                    'player = "Arion"\n\ndef show_player():\n\tprint(player)\n\nshow_player()',
                    None)],
      'practice': ['Create `greet()`.',
                   'Create `open_chest()`.',
                   'Call a function three times.',
                   'Create a function with two print statements.'],
      'challenge': 'Create `checkpoint_reached()` and call it twice.',
      'challenge_code': 'def checkpoint_reached():\n'
                        '\tprint("Checkpoint reached!")\n'
                        '\n'
                        'checkpoint_reached()\n'
                        'checkpoint_reached()',
      'quiz': [('Which keyword defines a function?', ['def', 'func', 'function', 'make'], 'def'),
               ('What runs a function?',
                ['Calling its name with parentheses', 'Writing def again', 'Deleting it', 'Using print only'],
                'Calling its name with parentheses'),
               ('Where does the function body go?',
                ['Indented under the definition', 'Before def', 'Outside the file', 'Inside comments'],
                'Indented under the definition')],
      'next': 29,
      'next_title': 'Parameters',
      'next_desc': 'Next you will learn how to send information into functions using parameters.'},
 29: {'title': 'Parameters',
      'intro': 'Parameters let a function receive information each time it is called.',
      'sections': [('Why parameters?',
                    'They make a function flexible instead of tied to one fixed value.',
                    'def greet():\n\tprint("Hello Alex")',
                    None),
                   ('Creating a parameter',
                    'Write the parameter name inside the function parentheses.',
                    'def greet(name):\n\tprint(name)',
                    None),
                   ('Passing an argument',
                    'The value supplied during a function call is an argument.',
                    'def greet(name):\n\tprint(name)\n\ngreet("Alex")',
                    None),
                   ('Multiple parameters',
                    'Functions can receive several pieces of information.',
                    'def show_player(name, score):\n\tprint(name)\n\tprint(score)',
                    None),
                   ('Different calls',
                    'The same function can be called with different arguments.',
                    'def greet(name):\n\tprint(f"Hello, {name}!")\n\ngreet("Alex")\ngreet("Mia")',
                    None),
                   ('Clear parameter names',
                    'Parameter names should describe the data they receive.',
                    'def attack(damage):\n\tprint(damage)',
                    None)],
      'practice': ['Create a function with a name parameter.',
                   'Create a function with a score parameter.',
                   'Create a function with two parameters.',
                   'Call the same function with different values.'],
      'challenge': 'Create `player_status()` with `name` and `health` parameters.',
      'challenge_code': 'def player_status(name, health):\n'
                        '\tprint(f"{name} has {health} health.")\n'
                        '\n'
                        'player_status("Arion", 100)',
      'quiz': [('What is a parameter?',
                ['Information a function receives', 'A loop', 'A list method', 'A file extension'],
                'Information a function receives'),
               ('What is an argument?',
                ['A value passed to a parameter', 'The colon', 'The function name', 'The return keyword'],
                'A value passed to a parameter'),
               ('Can a function have two parameters?', ['Yes', 'No', 'Only strings', 'Only lists'], 'Yes')],
      'next': 30,
      'next_title': 'What Is a Dictionary?',
      'next_desc': 'Next you will learn dictionaries and key-value pairs.'},
 30: {'title': 'What Is a Dictionary?',
      'intro': 'A dictionary stores information as key-value pairs.',
      'sections': [('Creating a dictionary',
                    'Dictionaries use curly braces with keys and values.',
                    'player = {"name": "Arion", "health": 100}',
                    None),
                   ('Key and value',
                    'The key is the label and the value is the information stored under it.',
                    'player = {"name": "Arion", "health": 100}',
                    None),
                   ('Accessing a value',
                    'Use the key in square brackets.',
                    'player = {"name": "Arion", "health": 100}\nprint(player["name"])',
                    None),
                   ('Adding a key',
                    'Assign a new value to a new key.',
                    'player = {"name": "Arion"}\nplayer["score"] = 500',
                    None),
                   ('Changing a value',
                    'Assign a new value to an existing key.',
                    'player = {"health": 100}\nplayer["health"] = 75',
                    None),
                   ('Removing a key',
                    '`pop()` can remove a key and return its value.',
                    'player = {"name": "Arion", "health": 100}\nplayer.pop("health")',
                    None),
                   ('keys, values, items',
                    'These methods help inspect dictionary contents.',
                    'player = {"name": "Arion", "score": 500}\nprint(player.keys())',
                    None),
                   ('Dictionary vs list',
                    'Lists are useful for ordered collections; dictionaries are useful when labels matter.',
                    None,
                    None)],
      'practice': ['Create a player dictionary.',
                   'Add a score key.',
                   'Change health.',
                   'Access a value by key.'],
      'challenge': 'Create a dictionary containing name, health, level, and score, then print two values.',
      'challenge_code': 'player = {\n'
                        '\t"name": "Arion",\n'
                        '\t"health": 100,\n'
                        '\t"level": 3,\n'
                        '\t"score": 500\n'
                        '}\n'
                        '\n'
                        'print(player["name"])\n'
                        'print(player["health"])',
      'quiz': [('What does a dictionary store?',
                ['Key-value pairs', 'Only numbers', 'Only loops', 'Only functions'],
                'Key-value pairs'),
               ('How do you access a value?',
                ['Using its key', 'Using range()', 'Using break', 'Using a colon only'],
                'Using its key'),
               ('Which brackets create a dictionary?', ['{}', '[]', '()', '<>'], '{}'),
               ('Can dictionary values change?', ['Yes', 'No', 'Only strings', 'Only numbers'], 'Yes')],
      'next': 31,
      'next_title': 'Understanding Errors',
      'next_desc': 'Next you will learn how to read common Python errors.'},
 31: {'title': 'Understanding Errors',
      'intro': "Errors are Python's way of telling you that something went wrong or that your code does not "
               'follow the rules.',
      'sections': [('Errors are normal',
                    'Every programmer encounters errors. They are part of learning and debugging.',
                    None,
                    None),
                   ('SyntaxError',
                    "Usually means the code does not follow Python's syntax rules.",
                    'print("Hello"',
                    None),
                   ('NameError',
                    'Can happen when Python cannot find the name you used.',
                    'print(score)',
                    'If `score` was never created, Python cannot find it.'),
                   ('TypeError',
                    'Can happen when an operation is used with incompatible types.',
                    '"Age: " + 15',
                    None),
                   ('IndexError',
                    'Can happen when a list index does not exist.',
                    'items = ["Key", "Potion"]\nprint(items[5])',
                    None),
                   ('KeyError',
                    'Can happen when a dictionary key is missing.',
                    'player = {"name": "Arion"}\nprint(player["health"])',
                    None),
                   ('Read the message',
                    'Look at the error type and the line Python points to. Start there.',
                    None,
                    None),
                   ('Fix one thing at a time',
                    'Make a small change, run again, and check the new result.',
                    None,
                    None)],
      'practice': ['Identify the error type in a few short examples.',
                   'Find a missing parenthesis.',
                   'Find a wrong list index.',
                   'Find a missing dictionary key.'],
      'challenge': 'Look at a broken list-access example and explain why it can produce an IndexError.',
      'challenge_code': 'items = ["Key"]\nprint(items[3])\n\n# Index 3 does not exist.',
      'quiz': [('What is a SyntaxError?',
                ['A syntax problem', 'A loop result', 'A list method', 'Successful output'],
                'A syntax problem'),
               ('Which can happen with an unknown variable name?',
                ['NameError', 'IndexError', 'KeyError', 'TypeError'],
                'NameError'),
               ('Which can happen with a missing list index?',
                ['IndexError', 'NameError', 'SyntaxError', 'KeyError'],
                'IndexError')],
      'next': 32,
      'next_title': 'try / except',
      'next_desc': 'Next you will learn how to handle certain runtime errors with try and except.'},
 32: {'title': 'try / except',
      'intro': '`try` and `except` let your program respond to certain runtime errors instead of failing at '
               'that point.',
      'sections': [('The basic structure',
                    'Put code that may fail inside `try`, followed by an `except` block.',
                    'try:\n\t# code that might fail\nexcept:\n\t# response',
                    None),
                   ('A simple example',
                    'If an error happens inside try, Python moves to except.',
                    'try:\n\tprint(10 / 0)\nexcept:\n\tprint("Something went wrong")',
                    None),
                   ('Specific exceptions',
                    'Catching a specific error is usually clearer.',
                    'try:\n\tprint(10 / 0)\nexcept ZeroDivisionError:\n\tprint("Cannot divide by zero")',
                    None),
                   ('ValueError',
                    'This can happen when converting unsuitable text to a number.',
                    'try:\n\tnumber = int("hello")\nexcept ValueError:\n\tprint("Please enter a number")',
                    None),
                   ('Keeping try blocks focused',
                    'Wrap the small operation you actually expect may fail.',
                    None,
                    None),
                   ('Common mistakes',
                    'Remember the colon, indentation, and the exception type.',
                    None,
                    None)],
      'practice': ['Handle division by zero.',
                   'Handle invalid number conversion.',
                   'Handle a missing dictionary key.'],
      'challenge': 'Safely handle division by zero and print a friendly message.',
      'challenge_code': 'try:\n'
                        '\tanswer = 100 / 0\n'
                        'except ZeroDivisionError:\n'
                        '\tprint("Cannot divide by zero.")',
      'quiz': [('What belongs inside try?',
                ['Code that might fail', 'Only comments', 'Only output', 'Only loops'],
                'Code that might fail'),
               ('What does except do?',
                ['Handles a matching error', 'Starts a loop', 'Creates a list', 'Defines a function'],
                'Handles a matching error'),
               ('Which error comes from division by zero?',
                ['ZeroDivisionError', 'ValueError', 'NameError', 'IndexError'],
                'ZeroDivisionError')],
      'next': 33,
      'next_title': 'Exception Patterns',
      'next_desc': 'The final lesson expands error handling with else, finally, and practical patterns.'},
 33: {'title': 'Exception Patterns',
      'intro': 'Build on try/except by learning useful patterns for successful and cleanup cases.',
      'sections': [('Specific except blocks',
                    'Catch the exception you actually expect when possible.',
                    'try:\n\tresult = 10 / 0\nexcept ZeroDivisionError:\n\tprint("No division by zero")',
                    None),
                   ('try and else',
                    'An `else` block can run when the try block succeeds without raising the caught '
                    'exception.',
                    'try:\n'
                    '\tresult = 10 / 2\n'
                    'except ZeroDivisionError:\n'
                    '\tprint("Cannot divide")\n'
                    'else:\n'
                    '\tprint(result)',
                    None),
                   ('finally',
                    'A `finally` block runs whether an exception happened or not and is useful for cleanup.',
                    'try:\n'
                    '\tprint("Work")\n'
                    'except Exception:\n'
                    '\tprint("Error")\n'
                    'finally:\n'
                    '\tprint("Finished")',
                    None),
                   ('Do not hide everything',
                    'A huge bare except can make debugging harder. Catch expected errors carefully.',
                    None,
                    None),
                   ('Real-world example',
                    'Input validation, file handling, network work, and many other tasks can benefit from '
                    'targeted exception handling.',
                    None,
                    None),
                   ('Debugging mindset',
                    'Try to understand why the error happened rather than simply hiding it.',
                    None,
                    None)],
      'practice': ['Use a specific ZeroDivisionError handler.',
                   'Add an else block to a successful try.',
                   'Add a finally block to a small example.',
                   'Explain why targeted exceptions are easier to debug.'],
      'challenge': 'Write a small program that uses try, except, and finally to show a clean success/failure '
                   'flow.',
      'challenge_code': 'try:\n'
                        '\tanswer = 20 / 5\n'
                        'except ZeroDivisionError:\n'
                        '\tprint("Cannot divide by zero")\n'
                        'else:\n'
                        '\tprint(answer)\n'
                        'finally:\n'
                        '\tprint("Finished")',
      'quiz': [("When can try's else run?",
                ['When try succeeds', 'Only on an error', 'Before try', 'Never'],
                'When try succeeds'),
               ('When does finally run?',
                ['Whether or not an exception occurred',
                 'Only on errors',
                 'Only on success',
                 'Only in loops'],
                'Whether or not an exception occurred'),
               ('Why prefer specific exceptions?',
                ['They make handling clearer',
                 'They make code longer for no reason',
                 'They stop all errors',
                 'They remove loops'],
                'They make handling clearer')],
      'next': None,
      'next_title': 'Projects',
      'next_desc': 'You have completed the core course. Now build projects to put the skills together.'}}
PROJECTS = {'🟢 Project 1 — Calculator': {'title': 'Calculator',
                              'goal': 'Build a calculator that asks for two numbers and an operation.',
                              'concepts': 'input(), variables, float(), arithmetic operators, if/elif/else',
                              'code': 'print("=== Calculator ===")\n'
                                      '\n'
                                      'number1 = float(input("Enter first number: "))\n'
                                      'number2 = float(input("Enter second number: "))\n'
                                      'operation = input("Choose +, -, *, or /: ")\n'
                                      '\n'
                                      'if operation == "+":\n'
                                      '\tprint(number1 + number2)\n'
                                      'elif operation == "-":\n'
                                      '\tprint(number1 - number2)\n'
                                      'elif operation == "*":\n'
                                      '\tprint(number1 * number2)\n'
                                      'elif operation == "/":\n'
                                      '\tif number2 == 0:\n'
                                      '\t\tprint("Cannot divide by zero.")\n'
                                      '\telse:\n'
                                      '\t\tprint(number1 / number2)\n'
                                      'else:\n'
                                      '\tprint("Unknown operation")',
                              'extensions': ['Add %, //, and **.',
                                             'Add a repeat option with a loop.',
                                             'Improve the result messages.']},
 '🟢 Project 2 — Number Guessing Game': {'title': 'Number Guessing Game',
                                        'goal': 'Build a game where a player guesses a secret number.',
                                        'concepts': 'input(), int(), comparisons, if/elif/else, while loop',
                                        'code': 'secret = 7\n'
                                                '\n'
                                                'while True:\n'
                                                '\tguess = int(input("Guess the number: "))\n'
                                                '\n'
                                                '\tif guess == secret:\n'
                                                '\t\tprint("Correct!")\n'
                                                '\t\tbreak\n'
                                                '\telif guess < secret:\n'
                                                '\t\tprint("Too low!")\n'
                                                '\telse:\n'
                                                '\t\tprint("Too high!")',
                                        'extensions': ['Count attempts.',
                                                       'Set a maximum number of guesses.',
                                                       'Choose the secret number randomly later.']},
 '🟢 Project 3 — Rock Paper Scissors': {'title': 'Rock Paper Scissors',
                                       'goal': 'Let the player choose rock, paper, or scissors and determine '
                                               'the result.',
                                       'concepts': 'input(), comparisons, if/elif/else, and/or',
                                       'code': 'player = input("Choose rock, paper, or scissors: ")\n'
                                               'computer = "rock"\n'
                                               '\n'
                                               'if player == computer:\n'
                                               '\tprint("Draw")\n'
                                               'elif player == "paper" and computer == "rock":\n'
                                               '\tprint("You win")\n'
                                               'elif player == "scissors" and computer == "paper":\n'
                                               '\tprint("You win")\n'
                                               'elif player == "rock" and computer == "scissors":\n'
                                               '\tprint("You win")\n'
                                               'else:\n'
                                               '\tprint("Computer wins")',
                                       'extensions': ['Use `random` later for the computer choice.',
                                                      'Keep score across multiple rounds.',
                                                      'Add input cleanup with string methods.']},
 '🟢 Project 4 — Quiz Game': {'title': 'Quiz Game',
                             'goal': 'Build a quiz that asks questions and keeps a score.',
                             'concepts': 'input(), variables, comparisons, if/else, f-strings',
                             'code': 'score = 0\n'
                                     '\n'
                                     'answer = input("What language are we learning? ")\n'
                                     '\n'
                                     'if answer.lower() == "python":\n'
                                     '\tprint("Correct!")\n'
                                     '\tscore = score + 1\n'
                                     'else:\n'
                                     '\tprint("Wrong!")\n'
                                     '\n'
                                     'answer = input("What symbol starts a comment? ")\n'
                                     '\n'
                                     'if answer == "#":\n'
                                     '\tprint("Correct!")\n'
                                     '\tscore = score + 1\n'
                                     'else:\n'
                                     '\tprint("Wrong!")\n'
                                     '\n'
                                     'print(f"Your score is {score}/2")',
                             'extensions': ['Add five questions.',
                                            'Show a final score message.',
                                            'Store questions in a list later.']},
 '🟢 Project 5 — To-Do List': {'title': 'To-Do List',
                              'goal': 'Build a small command-line task list.',
                              'concepts': 'lists, append(), remove(), input(), for/while loops',
                              'code': 'tasks = []\n'
                                      '\n'
                                      'task = input("Enter a task: ")\n'
                                      'tasks.append(task)\n'
                                      '\n'
                                      'task = input("Enter another task: ")\n'
                                      'tasks.append(task)\n'
                                      '\n'
                                      'print("Your tasks:")\n'
                                      'for task in tasks:\n'
                                      '\tprint("-", task)',
                              'extensions': ['Add a remove option.',
                                             'Add a show-all option.',
                                             'Create a full menu with while.']}}


def render_course_lesson(number, data):
    st.title(f"🐍 Lesson {number} — {data['title']}")
    st.write(data["intro"])
    st.divider()

    # Lesson overview
    st.subheader("🧭 Lesson Overview")
    cols = st.columns(3)
    with cols[0]:
        st.metric("Lesson", str(number))
    with cols[1]:
        st.metric("Teaching sections", str(len(data["sections"])))
    with cols[2]:
        st.metric("Quiz questions", str(len(data["quiz"])))

    st.info(
        "💡 Learn the idea first. Then type the examples yourself in your Python file. "
        "Do not worry about memorizing everything at once."
    )

    st.header("🎯 Learning Goals")
    for heading, _, _, _ in data["sections"][:5]:
        st.markdown(f"- Understand **{heading}**")

    st.divider()

    # Main lesson sections
    for index, section in enumerate(data["sections"], start=1):
        heading, explanation, code, note = section
        st.header(f"{index}. {heading}")
        st.write(explanation)
        if code:
            st.code(code, language="python")
        if note:
            st.info(note)

    # Beginner warning / debugging guidance
    st.header("⚠️ Common Beginner Mistakes")
    st.markdown(
        """
        At this level, most mistakes come from small details: a missing colon,
        the wrong indentation, a misspelled name, quotation marks in the wrong place,
        or accidentally mixing a later concept into the current lesson.
        """
    )
    st.warning(
        "When something does not work, read the error message first and check the line it mentions."
    )

    # Think-before-run section
    first_code = next((section[2] for section in data["sections"] if section[2]), None)
    if first_code:
        st.header("🧠 Think Before You Run")
        st.write("Predict what this example will do before running it.")
        st.code(first_code, language="python")

    # Practice
    st.header("🧩 Practice")
    st.write("Open your Python file and complete these exercises:")
    for item in data["practice"]:
        st.markdown(f"- {item}")

    # Mini challenge
    st.header("🔥 Mini Challenge")
    st.write(data["challenge"])
    if st.button("Show Challenge Solution", key=f"master_l{number}_challenge"):
        st.code(data["challenge_code"], language="python")
        st.success("Now change the example and build your own version.")

    # Reflection
    st.header("🛠️ Explain It in Your Own Words")
    student_note = st.text_area(
        "Write one or two sentences explaining today's concept:",
        height=110,
        key=f"master_l{number}_reflection",
    )
    if st.button("Check My Explanation", key=f"master_l{number}_reflection_btn"):
        if student_note.strip():
            st.success(
                "Nice! Explaining a programming idea in your own words is excellent practice."
            )
        else:
            st.warning("Write your explanation first.")

    # Quiz
    st.header("🧠 Quick Quiz")
    answers = []
    for q_index, (question, options, correct) in enumerate(data["quiz"], start=1):
        answers.append(
            st.radio(
                question,
                options,
                key=f"master_l{number}_quiz_{q_index}",
            )
        )

    if st.button("✅ Submit Quiz", key=f"master_l{number}_quiz_submit"):
        score = sum(
            answer == correct
            for answer, (_, _, correct) in zip(answers, data["quiz"])
        )
        total = len(data["quiz"])
        st.write(f"### Your Score: {score}/{total}")
        if score == total:
            st.balloons()
            st.success("🎉 Perfect! You understood this lesson.")
        elif score >= max(1, total - 1):
            st.info("👍 Very good! Review the one idea you missed.")
        else:
            st.warning(
                "Keep practicing. Read the lesson again and try the quiz once more."
            )

    st.divider()
    st.header("📚 What You Learned")
    st.markdown(
        """
        - The main idea of today's lesson
        - The important syntax and examples
        - How to use the concept in a small program
        - Common beginner mistakes
        - How the concept connects to the next part of Python
        """
    )
    st.success(f"🎯 Lesson {number} complete!")

    if data.get("next"):
        st.header("➡️ Next Lesson")
        st.write(f"**Lesson {data['next']} — {data['next_title']}**")
        st.write(data["next_desc"])


def render_project(project_name, project):
    st.title(f"🟢 {project_name}")
    st.write(project["goal"])
    st.divider()

    cols = st.columns(3)
    with cols[0]:
        st.subheader("🎯 Goal")
        st.write(project["goal"])
    with cols[1]:
        st.subheader("🧠 Concepts")
        st.write(project["concepts"])
    with cols[2]:
        st.subheader("🚀 Workflow")
        st.write("Run → Understand → Change → Extend")

    st.header("💻 Starter Code")
    st.code(project["code"], language="python")
    st.warning(
        "Run the project in VS Code or the terminal. Projects using input() are shown as code here."
    )

    st.header("🔍 Understand the Code First")
    st.markdown(
        """
        1. Read the code from top to bottom.
        2. Identify variables and inputs.
        3. Find the conditions and loops.
        4. Predict the output.
        5. Run the program.
        6. Only then start adding features.
        """
    )

    st.header("🚀 Extension Challenges")
    for index, item in enumerate(project["extensions"], start=1):
        st.markdown(f"**Challenge {index}:** {item}")

    st.header("🧩 Project Checklist")
    check1 = st.checkbox("I can run the starter project.", key=f"{project_name}_check1")
    check2 = st.checkbox("I understand the main parts of the code.", key=f"{project_name}_check2")
    check3 = st.checkbox("I changed something myself.", key=f"{project_name}_check3")
    if check1 and check2 and check3:
        st.success("🎉 Project checklist complete!")


# ============================================================
# MASTER LESSONS / PROJECTS — CONNECTED BELOW THE ORIGINAL LESSONS
# ============================================================

# --- DYNAMIC LESSON AREA WITH AUTO-SCROLL ---
st.divider()

# Anchor target for JavaScript smooth scrolling
st.markdown("<div id='lesson-target'></div>", unsafe_allow_html=True)

if st.session_state.current_topic:
    # Trigger smooth scroll if a lesson button was just clicked
    if st.session_state.get("should_scroll", False):
        st.components.v1.html(
            """
            <script>
                window.parent.document.getElementById('lesson-target').scrollIntoView({
                    behavior: 'smooth'
                });
            </script>
            """,
            height=0
        )
        st.session_state.should_scroll = False  # Reset flag

    # Lesson Header wrapped in Entrance Animation
    st.markdown(f"<div class='fade-in-up'><h2 class='sub-glow'>📖 Lesson: {st.session_state.current_topic}</h2></div>", unsafe_allow_html=True)
    
    # Close lesson button
    if st.button("❌ Close Lesson"):
        st.session_state.current_topic = None
        st.rerun()

    st.markdown("---")

    # --- LESSON TUTORIAL CONTENT ---
    if st.session_state.current_topic == "1. What Is Programming?":
        st.markdown("Before we write any Python code, let's understand the most basic question:")
        st.header(":red[What is programming?]")
        st.divider()
        st.header("1. What is a program?")
        st.info("A program is a set of instructions that tells a computer what to do.")
        st.image("images/Writing code is time-consuming, and even experienced developers spend significant time on repetitive tasks_ AI coding assistants have changed this. These tools suggest code completions as you type, generate entire functions from plain English de.jpeg")
        st.subheader("Think about giving instructions to a person.")
        st.markdown("""
            1. Take a cup.  
            2. Boil water.  
            3. Put tea in the cup. 
            4. Add hot water.
            5. Add sugar.
            6. Mix it.
            """)
        st.markdown("These are **instructions**.")
        st.subheader("A computer also needs instructions.")
        st.code("""
                1. Ask the user for their name.
                2. Store their name.
                3. Display "Hello" followed by their name. 
                """)
        st.markdown("Those instructions together form a **program**.")
        st.divider()
        st.header(":red[2. What is programming?]")
        st.info("Programming is the process of creating instructions for a computer to follow.")
        st.write("In simple words:")
        st.subheader("    🧠 Programming = Giving instructions to a computer.")
        st.image("images/Download Young smiling man cartoon character holding or showing the blank screen of a laptop computer and pointing hand finger_ .jpeg")
        st.write("For example:")
        st.code("You → Give instructions → Computer → Performs the task")
        st.markdown("The instructions are written using a **programming language**.")
        st.divider()
        st.header(":red[3. Why can't we just talk to a computer normally?]")
        st.info("Computers fundamentally work with very low-level machine instructions, represented in binary:")
        st.code("01001000 01101001 ...")
        st.markdown("Humans don't want to write programs like that.")
        st.markdown("So programming languages were created.")
        st.markdown("""
        Examples include:
            Python
            C
            C++
            C#
            Java
            JavaScript
            Rust
            """)

        st.image("images/anmol.jpeg")
        st.markdown("These languages allow humans to write instructions in a much more understandable form.")
        st.divider()
        st.header(":red[4. What is a programming language?]")
        st.info("A **programming language** is a language used to communicate instructions to a computer.")
        st.write("For example, in Python:")
        st.image("images/hellow.jpeg")
        st.write("This tells Python:")
        st.subheader("  **Display Hello** on the screen.")
        st.write("Python then takes care of translating your instructions into things the computer can execute.")
        st.divider()
        st.header(":red[5. The three important words]")
        st.subheader("Program")
        st.info("A collection of instructions that performs a task.")
        st.subheader("Programming")
        st.info("The process of creating those instructions.")
        st.subheader("Programming language")
        st.info("The language used to write those instructions.")
        st.markdown("**So**")
        st.markdown("""
        1. Python is a programming language.
        2. A Python program is a set of instructions written using Python.
        3. Programming is the process of creating those instructions.
        """)
        st.divider()
        st.subheader("Go ahead for next topic")

    elif st.session_state.current_topic == "2. Setting Up Python":
        st.header(":red[1. What is Python?]")
        st.markdown("**Python is a programming language.**")
        st.write("It allows us to write instructions that a computer can execute.")
        st.image("images/PY.jpeg", width=650)
        st.write("For example:")
        st.code("""print("Hello World")""")
        st.write("This is Python code.")
        st.write("The instruction means:")
        st.markdown("""**Display "Hello World" on the screen.**""")
        st.divider()

        st.header(":red[2. Why was Python created?]")
        st.write("Computers understand instructions, but humans need a convenient way to write those instructions.")
        st.markdown("Python was designed to have **simple and readable syntax.**")
        st.write("For example, Python:")
        st.code("""print("Hello")""")
        st.write("is much easier for a beginner to understand than low-level machine instructions.")
        st.markdown("That's one reason Python became widely used.")
        st.divider()

        st.header(":red[3. What can Python do?]")
        st.write("Python is not only for one type of program. You can use it for:")
        st.subheader("🌐 Web development")
        st.subheader("🤖 Artificial intelligence")
        st.subheader("📊 Data science")
        st.subheader("🎮 Games")
        st.subheader("⚙️ Automation")
        st.subheader("🖥️ Desktop applications")
        st.subheader("🔐 Cybersecurity")
        st.divider()

        st.header("5. What is the Python interpreter?")
        st.write("The **Python interpreter** is software that reads Python code and helps execute it.")
        st.write("For example, when you run:")
        st.code('print("Hello")', language="python")
        st.write("Python processes that instruction and causes `Hello` to appear on the screen.")
        st.write("You don't need to understand the internal details yet.")
        st.write("For now, remember:")
        st.info("💡 **The Python interpreter is the program that runs Python code.**")

        st.header("6. Your `.py` file")
        st.write("When you write Python code, you normally save it in a file ending with:")
        st.code(".py", language="text")
        st.write("For example:")
        st.code("hello.py", language="text")
        st.write("Inside it:")
        st.code('print("Hello World")', language="python")
        st.write("Then you run the file using Python.")
        st.write("So:")
        st.code(
            """hello.py
      │
      ▼
    Python runs it
      │
      ▼
    Hello World""",
            language="text",
        )
        st.divider()

        # ==========================================
        # SECTION 7: PYTHON IS CASE-SENSITIVE
        # ==========================================
        st.header("7. Python is case-sensitive")
        st.write("This is something you should know from the beginning.")
        st.write("These are different:")
        st.code(
            """name
Name
NAME""",
            language="python",
        )
        st.image("images/case.jpeg", width=600)
        st.write("Python treats them as three different names.")
        st.write("Similarly:")
        st.code("print()", language="python")
        st.write("is correct, while:")
        st.code("Print()", language="python")
        st.write("is not the same thing.")
        st.markdown("So **capital letters matter in Python.**")
        st.divider()

        # ==========================================
        # SECTION 8: PYTHON FOLLOWS RULES
        # ==========================================
        st.header("8. Python follows rules")
        st.write("Every programming language has rules.")
        st.write("These rules are called **syntax**.")
        st.image("images/rules.jpeg")
        st.write("For example:")
        st.code('print("Hello")', language="python")
        st.write("follows Python's syntax.")

        st.write("If you write something incorrectly, Python can give you an error.")
        st.write("For example:")
        st.code('print("Hello"', language="python")
        st.error("THIS IS AN ERROR")

        st.write("The closing `)` is missing.")
        st.write("Python will complain because the instruction isn't written correctly.")
        st.write("Don't worry about errors. **Errors are a normal part of programming.**")
        st.divider()

        # ==========================================
        # SECTION 9: PYTHON IS NOT MAGIC
        # ==========================================
        st.header("9. Python is not magic")
        st.write("Suppose you write:")
        st.code("print(10 + 20)", language="python")
        st.write("Python doesn't magically know the answer.")
        st.write("It follows the instructions:")

        st.code(
            """10 + 20
        │
        ▼
        Calculate
        │
        ▼
        30
        │
        ▼
        Display 30""",
            language="text",
        )
        st.write("This idea becomes extremely important later.")
        st.divider()

        # --- LESSON 2 HEADER ---
        st.title("🐍 Lesson 2 — Setting Up Python in VS Code")
        st.write("First, understand that there are **three separate things**:")
        st.code("""VS Code
        +
        Python Extension
        +
        Python Interpreter""", language="text")
        st.write("They each have a different job. VS Code is where you write your code, the Python extension adds Python-specific features, and the Python interpreter actually runs your Python code.")
        st.image("images/vs.jpeg")
        st.divider()

        # ==========================================
        # SECTION 1: CHECK PYTHON INSTALLATION
        # ==========================================
        st.header("1. Check whether Python is already installed")
        st.write("Open your terminal or command prompt.")

        tab_win, tab_lin = st.tabs(["🪟 Windows", "🐧 Linux / Ubuntu"])

        with tab_win:
            st.write("Open **Command Prompt** (cmd) or **PowerShell**, and run:")
            st.code("python --version", language="cmd")
            
            st.write("You should get something similar to:")
            st.code("Python 3.12.3", language="text")
            
            st.write("If you get an error like `'python' is not recognized...`, download and install it from [python.org](https://www.python.org/downloads/).")
            st.warning("⚠️ **Important during installation on Windows:** Make sure to check the box that says **'Add Python.exe to PATH'** before clicking Install!")

        with tab_lin:
            st.write("Open your **Terminal** and run:")
            st.code("python3 --version", language="bash")
            
            st.write("You should get something similar to:")
            st.code("Python 3.12.3", language="text")
            
            st.write("If you see `python3: command not found`, install it using:")
            st.code("""sudo apt update
sudo apt install python3""", language="bash")

        st.divider()

        # ==========================================
        # SECTION 2: CHECK VS CODE
        # ==========================================
        st.header("2. Check VS Code")
        st.write("Open VS Code on your system.")
        st.write("If you don't have it installed, download it from [code.visualstudio.com](https://code.visualstudio.com/):")
        st.markdown("""
        * **Windows:** Download and run the `.exe` installer.
        * **Linux:** Download the `.deb` package (for Debian/Ubuntu) or install via your package manager.
        """)
        st.divider()

        # ==========================================
        # SECTION 3: INSTALL PYTHON EXTENSION
        # ==========================================
        st.header("3. Install the Python Extension")
        st.write("Now we need to tell VS Code: *'I want to work with Python.'*")
        st.markdown("""
        **Step 1:** Click the **Extensions** icon on the left sidebar (or press `Ctrl + Shift + X`).

        **Step 2:** Search for:
        """)
        st.code("Python", language="text")
        st.write("**Step 3:** Click **Install** on the official Python extension by **Microsoft**.")
        st.info("The official extension provides Python features such as IntelliSense, code completion, debugging, and interpreter selection.")
        st.divider()

        # ==========================================
        # SECTION 4: SELECT PYTHON INTERPRETER
        # ==========================================
        st.header("4. Select the Python Interpreter")
        st.write("This is an important concept. VS Code needs to know: *'Which Python installation should I use to run this program?'*")
        st.write("Press `Ctrl + Shift + P` to open the **Command Palette**, then search for:")
        st.code("Python: Select Interpreter", language="text")
        st.write("Click it and select your installed Python version. You will see something like:")

        tab_int_win, tab_int_lin = st.tabs(["🪟 Windows Path Example", "🐧 Linux Path Example"])

        with tab_int_win:
            st.code(r"Python 3.12.x C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe", language="text")

        with tab_int_lin:
            st.code("Python 3.12.x /usr/bin/python3", language="text")

        st.divider()

        # ==========================================
        # SECTION 5 & 6: FOLDER & FILE SETUP
        # ==========================================
        st.header("5. Create Your First Python Folder")
        st.write("Create a convenient folder (e.g., `Python-Learning`) and open it in VS Code via **File → Open Folder**.")

        st.header("6. Create Your First Python File")
        st.write("Inside VS Code Explorer, create a new file named:")
        st.code("hello.py", language="text")
        st.write("The `.py` extension tells VS Code that this is a Python source file.")
        st.divider()

        # ==========================================
        # SECTION 7 & 8: WRITE & RUN CODE
        # ==========================================
        st.header("7. Write Your First Python Code")
        st.write("Inside `hello.py`, write:")
        st.code('print("Hello World")', language="python")

        st.header("8. Run Your Program ▶️")
        st.write("Click the **▶️ Run Python File** button in the top-right corner of the editor. You will see the output in the bottom terminal panel:")
        st.code("Hello World", language="text")
        st.divider()

        # ==========================================
        # SECTION 9: RUNNING FROM TERMINAL
        # ==========================================
        st.header("9. You Can Also Run It From the Terminal")
        st.write("Inside the built-in terminal at the bottom of VS Code, run:")

        tab_term_win, tab_term_lin = st.tabs(["🪟 Windows Terminal", "🐧 Linux Terminal"])

        with tab_term_win:
            st.code("python hello.py", language="cmd")

        with tab_term_lin:
            st.code("python3 hello.py", language="bash")

        st.write("Output:")
        st.code("Hello World", language="text")
        st.divider()

        # ==========================================
        # SECTION 10 & TEST: ARCHITECTURE & TEST
        # ==========================================
        st.header("10. What You Have Set Up")
        st.code("""                 VS CODE
                            │
                ┌─────────┴─────────┐
                ↓                   ↓
            Python Extension     Your Python File
                                    │
                                    ↓
                            Python Interpreter
                                    │
                                    ↓
                                Computer
                                    │
                                    ↓
                                Output""", language="text")

        st.subheader("🧪 Your First Setup Test")
        st.write("Put this inside `hello.py` and run it:")
        st.code("""print("Hello World")
print("I am learning Python!")
print(2 + 3)""", language="python")

        st.write("Expected Output:")
        st.code("""Hello World
I am learning Python!
5""", language="text")

        st.success("🎉 If you get exactly that, your Python setup is working correctly!")
        st.divider()
        st.subheader("Head up with next")
    
    elif st.session_state.current_topic == "3. Your First Python Code":





        st.title("🐍 Lesson 3 — Your First Python Code")

        st.write(
            "In this lesson, you will write, save, and run your first Python code."
        )

        st.divider()

        # --------------------------------------------------
        # 1. WRITING YOUR FIRST LINE
        # --------------------------------------------------

        st.header("1. Writing Your First Line of Python Code")

        st.write(
            "Open the Python file you created in VS Code."
        )

        st.write(
            "Now write your first line of Python code:"
        )

        st.code(
            'print("Hello World")',
            language="python"
        )

        st.write(
            "Don't worry about understanding `print()` yet. "
            "We will learn exactly what `print()` means in the next lesson."
        )

        st.info(
            "For now, your goal is simply to write the code and make the program run."
        )

        # --------------------------------------------------
        # 2. SAVING THE FILE
        # --------------------------------------------------

        st.header("2. Save Your Python File")

        st.write(
            "After writing your code, save the file."
        )

        st.markdown(
            """
            ### In VS Code:

            - Press **Ctrl + S**
            - Or go to **File → Save**
            """
        )

        st.write(
            "Make sure your file has the `.py` extension."
        )

        st.code(
            "hello.py",
            language="text"
        )

        st.success(
            "Your Python program is now saved."
        )

        # --------------------------------------------------
        # 3. RUNNING THE PROGRAM
        # --------------------------------------------------

        st.header("3. Running Your Program")

        st.write(
            "Now we need to tell Python to run our code."
        )

        st.write(
            "In VS Code, you can usually see a ▶ button in the top-right corner."
        )

        st.markdown(
            """
            ### Click:

            **▶ Run Python File**
            """
        )

        st.write(
            "Python will execute the code inside your `.py` file."
        )

        st.code(
            'print("Hello World")',
            language="python"
        )

        st.write(
            "You should see the result in the terminal."
        )

        # --------------------------------------------------
        # 4. UNDERSTANDING THE OUTPUT
        # --------------------------------------------------

        st.header("4. Understanding the Output")

        st.write(
            "After running the program, you should see:"
        )

        st.code(
            "Hello World",
            language="text"
        )

        st.write(
            "This is called the **output** of your program."
        )

        st.markdown(
            """
            ### Think of it like this:

            **Your Code → Python Runs It → Output**
            """
        )

        st.info(
            "The computer follows the instructions you wrote and produces a result."
        )

        # --------------------------------------------------
        # 5. RUNNING FROM TERMINAL
        # --------------------------------------------------

        st.header("5. Running Python from the Terminal")

        st.write(
            "You can also run your Python program directly from the terminal."
        )

        st.write(
            "First, open the terminal in VS Code."
        )

        st.code(
            "Ctrl + `",
            language="text"
        )

        st.write(
            "Then use the `python3` command followed by your file name."
        )

        st.code(
            "python3 hello.py",
            language="bash"
        )

        st.write(
            "Press **Enter**."
        )

        st.write(
            "You should see:"
        )

        st.code(
            "Hello World",
            language="text"
        )

        st.success(
            "You have now run a Python program from the terminal!"
        )

        # --------------------------------------------------
        # 6. COMMON BEGINNER MISTAKES
        # --------------------------------------------------

        st.header("6. Common Beginner Mistakes")

        # Mistake 1
        st.subheader("❌ Mistake 1 — Wrong file name")

        st.code(
            "python3 hello",
            language="bash"
        )

        st.write(
            "If your file is actually called `hello.py`, include `.py`."
        )

        st.code(
            "python3 hello.py",
            language="bash"
        )

        # Mistake 2
        st.subheader("❌ Mistake 2 — Terminal is in the wrong folder")

        st.write(
            "If Python says it cannot find your file, your terminal may be "
            "in a different folder."
        )

        st.write(
            "Make sure the terminal is opened in the folder containing your Python file."
        )

        # Mistake 3
        st.subheader("❌ Mistake 3 — Forgetting quotation marks")

        st.code(
            'print(Hello World)',
            language="python"
        )

        st.write(
            "For now, remember that text inside `print()` needs quotation marks."
        )

        st.code(
            'print("Hello World")',
            language="python"
        )

        # Mistake 4
        st.subheader("❌ Mistake 4 — Using capital P")

        st.code(
            'Print("Hello World")',
            language="python"
        )

        st.write(
            "Python is case-sensitive. `print` and `Print` are not the same."
        )

        # Mistake 5
        st.subheader("❌ Mistake 5 — Not saving the file")

        st.write(
            "If you changed your code but didn't save it, Python may run the older version."
        )

        st.markdown(
            "**Remember:** Press **Ctrl + S** before running your program."
        )

        # --------------------------------------------------
        # 7. PRACTICE
        # --------------------------------------------------

        st.divider()

        st.header("📝 7. Small Practice")

        st.write(
            "Create a new Python file called:"
        )

        st.code(
            "my_first_program.py",
            language="text"
        )

        st.write(
            "Write these lines:"
        )

        st.code(
            '''print("My First Python Program")
        print("I am learning Python")
        print("This is my first program")''',
            language="python"
        )

        st.write(
            "Save the file and run it."
        )

        st.write(
            "Your output should look like:"
        )

        st.code(
            """My First Python Program
        I am learning Python
        This is my first program""",
            language="text"
        )

        st.success(
            "🎯 If you can do this without help, you have successfully written and run your first Python program!"
        )

        # --------------------------------------------------
        # 8. MINI CHALLENGE
        # --------------------------------------------------

        st.header("🔥 8. Mini Challenge")

        st.write(
            "Create a Python file called:"
        )

        st.code(
            "about_me.py",
            language="text"
        )

        st.write(
            "Make the program display three lines about yourself."
        )

        st.write(
            "For example:"
        )

        st.code(
            '''print("My name is Anmol")
        print("I am learning Python")
        print("I want to make apps")''',
            language="python"
        )

        st.write(
            "Now change the information to your own."
        )

        # --------------------------------------------------
        # 9. QUICK CHECK
        # --------------------------------------------------

        st.divider()

        st.header("🧠 9. Quick Check")

        q1 = st.radio(
            "1. What should you do after changing your Python code?",
            [
                "Close VS Code",
                "Save the file",
                "Delete the file",
                "Restart the computer"
            ]
        )

        q2 = st.radio(
            "2. Which command can run a Python file on Linux?",
            [
                "run hello.py",
                "start hello.py",
                "python3 hello.py",
                "open hello.py"
            ]
        )

        q3 = st.radio(
            "3. What do we call the result produced by a program?",
            [
                "Input",
                "Variable",
                "Output",
                "Folder"
            ]
        )

        q4 = st.radio(
            "4. What should the Python file normally end with?",
            [
                ".txt",
                ".jpg",
                ".py",
                ".html"
            ]
        )

        if st.button("✅ Check Answers"):

            score = 0

            if q1 == "Save the file":
                score += 1

            if q2 == "python3 hello.py":
                score += 1

            if q3 == "Output":
                score += 1

            if q4 == ".py":
                score += 1

            st.write(f"### Your Score: {score}/4")

            if score == 4:
                st.success("🎉 Perfect! You understand the basics of running Python code.")

            elif score == 3:
                st.success("👍 Very good! Review the one question you missed.")

            elif score == 2:
                st.info("Keep practicing. Go through the lesson once more.")

            else:
                st.warning("Don't worry! Read the lesson again and try the quiz again.")

        # --------------------------------------------------
        # 10. LESSON COMPLETE
        # --------------------------------------------------

        st.divider()

        st.header("🎯 Lesson 3 Complete!")

        st.write(
            "In this lesson, you learned how to:"
        )

        st.markdown(
            """
            - Write your first Python code
            - Save a Python file
            - Run a Python program from VS Code
            - Run a Python program from the terminal
            - Understand what output means
            - Recognize common beginner mistakes
            """
        )

        st.success(
            "🚀 Next lesson: `print()` — Now we will learn exactly how print() works."
        )
    elif st.session_state.current_topic == "4. print()":
        

        # --------------------------------------------------
        # TITLE
        # --------------------------------------------------

        st.title("🐍 Lesson 4 — print()")

        st.write(
            "In this lesson, you will learn how Python's `print()` function works "
            "and how to use it to display information on the screen."
        )

        st.divider()

        # --------------------------------------------------
        # 1. WHAT IS print()?
        # --------------------------------------------------

        st.header("1. What is print()?")

        st.write(
            "`print()` is a Python function used to display information on the screen."
        )

        st.code(
            'print("Hello World")',
            language="python"
        )
        st.image("images/print2.jpeg")

        st.write("Output:")

        st.code(
            "Hello World",
            language="text"
        )

        st.info(
            "Think of `print()` as telling Python: "
            "“Show this on the screen.”"
        )

        # --------------------------------------------------
        # 2. UNDERSTANDING THE CODE
        # --------------------------------------------------

        st.header("2. Understanding print()")

        st.code(
            'print("Hello World")',
            language="python"
        )

        st.write("Let's break it into parts:")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("print")
            st.write(
                "`print` is the name of the Python function."
            )

        with col2:
            st.subheader("()")
            st.write(
                "The parentheses contain the information we want to print."
            )

        with col3:
            st.subheader('"Hello World"')
            st.write(
                "This is the text that Python will display."
            )

        st.divider()

        # --------------------------------------------------
        # 3. PRINTING TEXT
        # --------------------------------------------------

        st.header("3. Printing Text")

        st.write(
            "Text is called a **string** in Python."
        )

        st.write(
            "Strings are written inside quotation marks."
        )

        st.code(
            '''print("Hello")
        print("My name is Anmol")
        print("I am learning Python")''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """Hello
        My name is Anmol
        I am learning Python""",
            language="text"
        )
        st.image("images/print.jpeg")

        st.info(
            "You can use either double quotes or single quotes for strings."
        )

        st.code(
            '''print("Hello")
        print('Hello')''',
            language="python"
        )

        # --------------------------------------------------
        # 4. PRINTING NUMBERS
        # --------------------------------------------------

        st.header("4. Printing Numbers")

        st.write(
            "You can also print numbers without quotation marks."
        )

        st.code(
            '''print(10)
        print(100)
        print(3.14)''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """10
        100
        3.14""",
            language="text"
        )

        st.warning(
            "Remember: `10` is a number, while `\"10\"` is text."
        )

        # --------------------------------------------------
        # 5. TEXT VS NUMBER
        # --------------------------------------------------

        st.header("5. Text vs Number")

        st.code(
            '''print("10")
        print(10)''',
            language="python"
        )

        st.write("Both look like this when displayed:")

        st.code(
            """10
        10""",
            language="text"
        )

        st.write(
            "But internally, Python treats them differently:"
        )

        comparison = {
            "Code": ['print("10")', "print(10)"],
            "What it contains": ["Text (string)", "Number (integer)"]
        }

        st.table(comparison)

        st.info(
            "This difference becomes very important when we start doing calculations."
        )

        # --------------------------------------------------
        # 6. PRINTING CALCULATIONS
        # --------------------------------------------------

        st.header("6. Printing Calculations")

        st.write(
            "`print()` can display the result of a mathematical calculation."
        )

        st.code(
            '''print(10 + 5)
        print(10 - 5)
        print(10 * 5)
        print(10 / 5)''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """15
        5
        50
        2.0""",
            language="text"
        )

        st.markdown(
            """
            ### Basic operators

            - `+` → Addition
            - `-` → Subtraction
            - `*` → Multiplication
            - `/` → Division
            """
        )

        # --------------------------------------------------
        # 7. MULTIPLE VALUES
        # --------------------------------------------------

        st.header("7. Printing Multiple Values")

        st.write(
            "You can print multiple values using commas."
        )

        st.code(
            'print("My age is", 15)',
            language="python"
        )

        st.write("Output:")

        st.code(
            "My age is 15",
            language="text"
        )

        st.write(
            "Python automatically places a space between the values."
        )

        st.code(
            'print("Health:", 100, "Score:", 500)',
            language="python"
        )

        st.write("Output:")

        st.code(
            "Health: 100 Score: 500",
            language="text"
        )

        # --------------------------------------------------
        # 8. MULTIPLE print() STATEMENTS
        # --------------------------------------------------

        st.header("8. Using Multiple print() Statements")

        st.write(
            "Every time you use `print()`, Python normally moves to a new line."
        )

        st.code(
            '''print("Line 1")
        print("Line 2")
        print("Line 3")''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """Line 1
        Line 2
        Line 3""",
            language="text"
        )

        st.success(
            "Python executes the statements from top to bottom."
        )

        # --------------------------------------------------
        # 9. PRINTING BOOLEANS
        # --------------------------------------------------

        st.header("9. Printing True and False")

        st.write(
            "Python also has boolean values: `True` and `False`."
        )

        st.code(
            '''print(True)
        print(False)''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """True
        False""",
            language="text"
        )

        st.info(
            "Notice that `True` and `False` start with capital letters."
        )

        # --------------------------------------------------
        # 10. COMMENTS
        # --------------------------------------------------

        st.header("10. Comments")

        st.write(
            "You can add notes to your Python code using `#`."
        )

        st.code(
            '''# This is a comment
        print("Hello World")''',
            language="python"
        )

        st.write(
            "Python ignores the comment when running the program."
        )

        st.info(
            "Comments are useful for explaining your code."
        )

        # --------------------------------------------------
        # 11. COMMON MISTAKES
        # --------------------------------------------------

        st.header("11. Common Beginner Mistakes")

        st.subheader("❌ Mistake 1 — Forgetting quotation marks")

        st.code(
            'print(Hello World)',
            language="python"
        )

        st.write(
            "If you want to print text, put it inside quotation marks."
        )

        st.code(
            'print("Hello World")',
            language="python"
        )

        st.subheader("❌ Mistake 2 — Writing Print instead of print")

        st.code(
            'Print("Hello")',
            language="python"
        )

        st.write(
            "Python is case-sensitive. `print()` must be written with a lowercase `p`."
        )

        st.subheader("❌ Mistake 3 — Missing a parenthesis")

        st.code(
            'print("Hello"',
            language="python"
        )

        st.write(
            "The opening `(` needs a matching closing `)`."
        )

        st.code(
            'print("Hello")',
            language="python"
        )

        st.subheader("❌ Mistake 4 — Mixing quotation marks")

        st.code(
            'print("Hello\')',
            language="python"
        )

        st.write(
            "Use matching quotation marks."
        )

        st.code(
            'print("Hello")',
            language="python"
        )

        # --------------------------------------------------
        # 12. INTERACTIVE PRINT PRACTICE
        # --------------------------------------------------

        st.divider()

        st.header("💻 12. Try print() Yourself")

        st.write(
            "Write a simple `print()` statement below."
        )

        user_text = st.text_input(
            "What do you want to print?",
            "Hello Python!"
        )

        if st.button("▶ Show Output"):

            st.write("Your code:")

            st.code(
                f'print("{user_text}")',
                language="python"
            )

            st.write("Output:")

            st.code(
                user_text,
                language="text"
            )

            st.success("You just used the idea behind print()!")

        # --------------------------------------------------
        # 13. PRACTICE
        # --------------------------------------------------

        st.header("📝 13. Practice")

        st.write(
            "Create a Python file and use `print()` to display the following:"
        )

        st.code(
            '''print("My Game")
        print("Player: Anmol")
        print("Health:", 100)
        print("Score:", 500)
        print(2 + 3)''',
            language="python"
        )

        st.write("Try to predict the output before running it.")

        if st.checkbox("Show Answer"):

            st.code(
                """My Game
        Player: Anmol
        Health: 100
        Score: 500
        5""",
                language="text"
            )

        # --------------------------------------------------
        # 14. MINI CHALLENGE
        # --------------------------------------------------

        st.header("🔥 14. Mini Challenge")

        st.write(
            "Using only `print()`, create a program that displays:"
        )

        st.code(
            """====================
            MY GAME
        ====================
        Player: Anmol
        Health: 100
        Score: 500
        Level: 1
        ====================""",
            language="text"
        )

        st.markdown(
            """
            ### Rules

            - Use only `print()`.
            - Don't use variables yet.
            - Don't use `input()` yet.
            - Try to make the output look exactly like the example.
            """
        )

        challenge = st.text_area(
            "Write your solution here:",
            height=220,
            placeholder='print("====================")\n...'
        )

        if st.button("🔍 Check My Code"):

            if challenge.strip() == "":
                st.warning("Write your code first!")

            else:
                st.code(
                    challenge,
                    language="python"
                )

                st.info(
                    "Run your code in VS Code and compare its output with the target."
                )

        # --------------------------------------------------
        # 15. QUICK QUIZ
        # --------------------------------------------------

        st.divider()

        st.header("🧠 15. Quick Quiz")

        q1 = st.radio(
            "What is the main purpose of print()?",
            [
                "To store information",
                "To display information",
                "To create a loop",
                "To create a variable"
            ]
        )

        q2 = st.radio(
            "Which code correctly prints Hello?",
            [
                'Print("Hello")',
                'print(Hello)',
                'print("Hello")',
                'PRINT("Hello")'
            ]
        )

        q3 = st.radio(
            "Which one is a number?",
            [
                '"10"',
                '"100"',
                "10",
                '"5"'
            ]
        )

        q4 = st.radio(
            "What will this code print?\n\nprint(5 + 5)",
            [
                "55",
                "10",
                '"10"',
                "5 + 5"
            ]
        )

        q5 = st.radio(
            "What does a # at the beginning of a line create?",
            [
                "A variable",
                "A number",
                "A comment",
                "A loop"
            ]
        )

        if st.button("✅ Check Quiz"):

            score = 0

            if q1 == "To display information":
                score += 1

            if q2 == 'print("Hello")':
                score += 1

            if q3 == "10":
                score += 1

            if q4 == "10":
                score += 1

            if q5 == "A comment":
                score += 1

            st.write(f"### Your Score: {score}/5")

            if score == 5:
                st.success("🎉 Perfect! You understand print() very well!")

            elif score >= 3:
                st.info("👍 Good job! Review the sections you found difficult.")

            else:
                st.warning(
                    "Keep practicing! Read the lesson again and try the quiz."
                )

        # --------------------------------------------------
        # LESSON SUMMARY
        # --------------------------------------------------

        st.divider()

        st.header("📚 What You Learned")

        st.markdown(
            """
            By the end of this lesson, you should understand:

            - What `print()` does
            - How to print text
            - How to print numbers
            - The difference between text and numbers
            - How to print calculations
            - How to print multiple values
            - How multiple `print()` statements work
            - How to print `True` and `False`
            - What comments are
            - Common `print()` mistakes
            """
        )

        # --------------------------------------------------
        # NEXT LESSON
        # --------------------------------------------------

        st.divider()

        st.header("🚀 Next Lesson")

        st.write(
            "Next, we will start understanding how Python code is organized "
            "and how to read code more easily."
        )

        st.success("🎯 Lesson 4 Complete!")
    elif st.session_state.current_topic == "5. Understanding Code":


        st.title("🐍 Lesson 5 — Understanding Code")

        st.write(
            "In this lesson, you will learn how to read Python code, "
            "understand what each part means, and follow what the computer does."
        )

        st.divider()

        # --------------------------------------------------
        # 1. WHAT DOES IT MEAN TO UNDERSTAND CODE?
        # --------------------------------------------------

        st.header("1. What Does It Mean to Understand Code?")

        st.write(
            "Understanding code means being able to look at a program and explain "
            "what each line does."
        )

        st.write("For example:")

        st.code(
            '''print("Hello")
        print("Welcome to Python")''',
            language="python"
        )

        st.write(
            "You should be able to look at this and understand that Python will "
            "execute the first line and then the second line."
        )

        st.info(
            "Don't try to memorize code. Try to understand what each part is doing."
        )

        # --------------------------------------------------
        # 2. PYTHON READS CODE FROM TOP TO BOTTOM
        # --------------------------------------------------

        st.header("2. Python Usually Runs Code from Top to Bottom")

        st.write(
            "Python normally starts at the first line and moves downward."
        )

        st.code(
            '''print("First")
        print("Second")
        print("Third")''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """First
        Second
        Third""",
            language="text"
        )

        st.success(
            "Python runs the first statement, then the second, then the third."
        )

        # --------------------------------------------------
        # 3. WHAT IS A LINE OF CODE?
        # --------------------------------------------------

        st.header("3. What Is a Line of Code?")

        st.write(
            "A line of code is one instruction written in your program."
        )

        st.code(
            '''print("Hello")
        print("Python")
        print("Game")''',
            language="python"
        )

        st.write(
            "Here we have three lines, and each line gives Python an instruction."
        )

        # --------------------------------------------------
        # 4. UNDERSTANDING A SIMPLE LINE
        # --------------------------------------------------

        st.header("4. Understanding a Line of Code")

        st.code(
            'print("Hello World")',
            language="python"
        )

        st.write("Let's look at each part:")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("print")
            st.write(
                "The function Python uses to display something."
            )

        with col2:
            st.subheader("( )")
            st.write(
                "The parentheses contain the information given to the function."
            )

        with col3:
            st.subheader('"Hello World"')
            st.write(
                "The text that we want Python to display."
            )

        st.info(
            "Learning to break code into smaller parts makes code much easier to understand."
        )

        # --------------------------------------------------
        # 5. STRINGS
        # --------------------------------------------------

        st.header("5. Understanding Text in Code")

        st.write(
            "Text written inside quotation marks is called a **string**."
        )

        st.code(
            '''print("Hello")
        print("Python is fun")
        print("I am learning")''',
            language="python"
        )

        st.write(
            "The quotation marks tell Python that the content is text."
        )

        st.warning(
            "Without quotation marks, Python may interpret the words differently."
        )

        # --------------------------------------------------
        # 6. NUMBERS IN CODE
        # --------------------------------------------------

        st.header("6. Understanding Numbers")

        st.write(
            "Numbers can be written directly in Python without quotation marks."
        )

        st.code(
            '''print(10)
        print(25)
        print(100)''',
            language="python"
        )

        st.write("Python treats these as numbers.")

        st.write("Compare this:")

        st.code(
            '''print(10)
        print("10")''',
            language="python"
        )

        st.write(
            "Both may look similar when displayed, but Python understands them differently."
        )

        comparison = {
            "Code": ["10", '"10"'],
            "Meaning": ["Number", "Text"]
        }

        st.table(comparison)

        # --------------------------------------------------
        # 7. SYMBOLS IN CODE
        # --------------------------------------------------

        st.header("7. Understanding Symbols")

        st.write(
            "Python uses different symbols to tell the computer what to do."
        )

        symbols = {
            "Symbol": ["+", "-", "*", "/"],
            "Meaning": [
                "Addition",
                "Subtraction",
                "Multiplication",
                "Division"
            ]
        }

        st.table(symbols)

        st.code(
            '''print(5 + 3)
        print(10 - 4)
        print(6 * 2)
        print(20 / 5)''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """8
        6
        12
        4.0""",
            language="text"
        )

        # --------------------------------------------------
        # 8. READING CODE LIKE A STORY
        # --------------------------------------------------

        st.header("8. Read Code Like a Story")

        st.write(
            "When you see code, don't look at the whole program at once."
        )

        st.write(
            "Read it one line at a time."
        )

        st.code(
            '''print("Game Started")
        print("Player entered the forest")
        print("A monster appeared")''',
            language="python"
        )

        st.markdown(
            """
            ### Read it like this:

            **Line 1:** The game starts.

            **Line 2:** The player enters the forest.

            **Line 3:** A monster appears.
            """
        )

        st.success(
            "This way of thinking will become very useful when programs become bigger."
        )

        # --------------------------------------------------
        # 9. PREDICTING OUTPUT
        # --------------------------------------------------

        st.header("9. Predict the Output")

        st.write(
            "One of the best ways to understand code is to predict what it will do "
            "before running it."
        )

        st.code(
            '''print("Hello")
        print(5 + 5)
        print("Game Over")''',
            language="python"
        )

        st.write("What will the output be?")

        answer = st.radio(
            "Choose the correct output:",
            [
                """Hello
        5
        Game Over""",

                """Hello
        10
        Game Over""",

                """10
        Hello
        Game Over""",

                """Hello
        Game Over
        10"""
            ]
        )

        if st.button("🔍 Check Output"):

            correct_answer = """Hello
        10
        Game Over"""

            if answer == correct_answer:
                st.success("🎉 Correct! You correctly followed the code.")
            else:
                st.error("Not quite. Look at the second line: 5 + 5 is calculated before it is displayed.")

        # --------------------------------------------------
        # 10. COMMENTS
        # --------------------------------------------------

        st.header("10. Understanding Comments")

        st.write(
            "Comments are notes written inside your code for humans to read."
        )

        st.code(
            '''# Start the game
        print("Game Started")

        # Show the player
        print("Welcome Player")''',
            language="python"
        )

        st.write(
            "Python ignores everything after `#` on a comment line."
        )

        st.info(
            "Comments help programmers understand their own code later."
        )

        # --------------------------------------------------
        # 11. CODE AND COMMENTS TOGETHER
        # --------------------------------------------------

        st.header("11. Code vs Comments")

        st.code(
            '''# This is a comment
        print("Hello")

        # This is another comment
        print("Python")''',
            language="python"
        )

        st.markdown(
            """
            ### Remember:

            📝 **Comment** → written for humans

            💻 **Code** → instructions Python executes
            """
        )

        # --------------------------------------------------
        # 12. SPACES AND INDENTATION
        # --------------------------------------------------

        st.header("12. Why Spaces Matter")

        st.write(
            "Python uses indentation (spaces or tabs at the beginning of a line) "
            "to organize certain parts of code."
        )

        st.write(
            "You will learn indentation more deeply when we start using `if` "
            "statements and loops."
        )

        st.code(
            '''if True:
            print("Hello")''',
            language="python"
        )

        st.info(
            "For now, just remember: Python cares about the structure of your code."
        )

        # --------------------------------------------------
        # 13. COMMON BEGINNER MISTAKES
        # --------------------------------------------------

        st.header("13. Common Beginner Mistakes")

        st.subheader("❌ Mistake 1 — Forgetting quotation marks")

        st.code(
            'print(Hello)',
            language="python"
        )

        st.write(
            "If Hello is supposed to be text, quotation marks are needed."
        )

        st.code(
            'print("Hello")',
            language="python"
        )

        st.subheader("❌ Mistake 2 — Using the wrong capitalization")

        st.code(
            'Print("Hello")',
            language="python"
        )

        st.write(
            "Python is case-sensitive. `print` and `Print` are different."
        )

        st.subheader("❌ Mistake 3 — Missing parentheses")

        st.code(
            'print("Hello"',
            language="python"
        )

        st.write(
            "The parentheses must be properly opened and closed."
        )

        st.subheader("❌ Mistake 4 — Not reading the code carefully")

        st.code(
            '''print("Start")
        print(10 + 5)
        print("End")''',
            language="python"
        )

        st.write(
            "Before running the program, try to predict its output."
        )

        # --------------------------------------------------
        # 14. PRACTICE
        # --------------------------------------------------

        st.divider()

        st.header("📝 14. Practice")

        st.write(
            "Look at this program and try to understand it without running it."
        )

        st.code(
            '''print("Welcome")
        print(10 + 20)
        print("Python")
        print(50 - 10)''',
            language="python"
        )

        st.write("Try to predict the output:")

        practice_answer = st.text_area(
            "Write what you think the output will be:",
            height=150,
            placeholder="Write the output here..."
        )

        if st.button("👀 Show Practice Answer"):

            st.write("Correct output:")

            st.code(
                """Welcome
        30
        Python
        40""",
                language="text"
            )

        # --------------------------------------------------
        # 15. MINI CHALLENGE
        # --------------------------------------------------

        st.header("🔥 15. Mini Challenge")

        st.write(
            "Look at the following code and answer the questions before running it."
        )

        st.code(
            '''print("My Game")
        print(100 + 50)
        print("Level 1")
        print(20 * 2)
        print("Game Started")''',
            language="python"
        )

        st.markdown(
            """
            ### Challenge

            1. What will the **first line** display?
            2. What will the **second line** display?
            3. What will the **fourth line** display?
            4. What will the **last line** display?
            """
        )

        challenge_answer = st.text_area(
            "Write your answers:",
            height=180,
            placeholder="1. ...\n2. ...\n3. ...\n4. ..."
        )

        if st.button("🔓 Show Challenge Answer"):

            st.write("Answers:")

            st.code(
                """1. My Game
        2. 150
        3. 40
        4. Game Started""",
                language="text"
            )

        # --------------------------------------------------
        # 16. QUICK QUIZ
        # --------------------------------------------------

        st.divider()

        st.header("🧠 16. Quick Quiz")

        q1 = st.radio(
            "1. How does Python normally execute a simple program?",
            [
                "From bottom to top",
                "From top to bottom",
                "Randomly",
                "Only the last line"
            ]
        )

        q2 = st.radio(
            "2. What is a line of code?",
            [
                "A folder",
                "An instruction in a program",
                "A computer screen",
                "A Python file"
            ]
        )

        q3 = st.radio(
            '3. In print("Hello"), what is "Hello"?',
            [
                "A number",
                "A comment",
                "A string",
                "An operator"
            ]
        )

        q4 = st.radio(
            "4. What does # normally indicate in Python?",
            [
                "A comment",
                "A number",
                "A function",
                "A string"
            ]
        )

        q5 = st.radio(
            "What will this code display?\n\nprint(10 + 5)",
            [
                "105",
                "15",
                '"15"',
                "10 + 5"
            ]
        )

        if st.button("✅ Check Quiz"):

            score = 0

            if q1 == "From top to bottom":
                score += 1

            if q2 == "An instruction in a program":
                score += 1

            if q3 == "A string":
                score += 1

            if q4 == "A comment":
                score += 1

            if q5 == "15":
                score += 1

            st.write(f"### Your Score: {score}/5")

            if score == 5:
                st.success("🎉 Perfect! You understand how to read basic Python code.")

            elif score >= 3:
                st.info(
                    "👍 Good job! Review the sections you found difficult."
                )

            else:
                st.warning(
                    "Keep practicing. Read the lesson again and try the quiz once more."
                )

        # --------------------------------------------------
        # LESSON SUMMARY
        # --------------------------------------------------

        st.divider()

        st.header("📚 What You Learned")

        st.markdown(
            """
            By the end of this lesson, you should understand:

            - What a line of code is
            - How Python normally executes code
            - How to read code one line at a time
            - How to understand strings and numbers
            - What common Python symbols mean
            - How to predict the output of simple code
            - The difference between code and comments
            - Why Python cares about code structure
            - How to find common beginner mistakes
            """
        )

        # --------------------------------------------------
        # NEXT LESSON
        # --------------------------------------------------

        st.divider()

        st.header("🚀 Next Lesson")

        st.write(
            "Next, we will learn one of the most important concepts in Python:"
        )

        st.subheader("📦 What Is a Variable?")

        st.write(
            "You will learn how to store information in your program "
            "and use that information later."
        )

        st.success("🎯 Lesson 5 Complete!")
    elif st.session_state.current_topic == "6. What Is a Variable?":
        
        # --------------------------------------------------
        # TITLE
        # --------------------------------------------------

        st.title("🐍 Lesson 6 — What Is a Variable?")

        st.write(
            "In this lesson, you will learn what a variable is, "
            "how to create one, how to use it, and how to change its value."
        )

        st.divider()

        # --------------------------------------------------
        # 1. WHAT IS A VARIABLE?
        # --------------------------------------------------

        st.header("1. What Is a Variable?")

        st.write(
            "A variable is a name that we use to store a value in a program."
        )

        st.write(
            "For example:"
        )

        st.code(
            'name = "Anmol"',
            language="python"
        )

        st.write(
            "Here, we created a variable called `name` and stored the value "
            "`\"Anmol\"` in it."
        )

        st.info(
            "Think of a variable like a labeled box that holds some information."
        )

        # --------------------------------------------------
        # 2. THE BOX EXAMPLE
        # --------------------------------------------------

        st.header("2. Think of a Variable as a Box")

        st.write(
            "Imagine you have a box with a label on it:"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📦 Label")

            st.code(
                "name",
                language="text"
            )

        with col2:
            st.subheader("📦 Value")

            st.code(
                "Anmol",
                language="text"
            )

        st.write(
            "The label is the variable name, and the value is the information "
            "stored in that variable."
        )

        st.code(
            'name = "Anmol"',
            language="python"
        )

        st.warning(
            "This box is just a simple way to understand the idea. "
            "A Python variable is not literally a physical box."
        )

        # --------------------------------------------------
        # 3. CREATING A VARIABLE
        # --------------------------------------------------

        st.header("3. Creating a Variable")

        st.write(
            "To create a variable, give it a name and assign a value to it."
        )

        st.code(
            'name = "Anmol"',
            language="python"
        )

        st.markdown(
            """
            ### The `=` symbol

            The `=` symbol is used to assign a value to a variable.

            **Variable name = Value**
            """
        )

        st.code(
            'age = 15',
            language="python"
        )

        st.write(
            "Now the variable `age` has the value `15`."
        )

        # --------------------------------------------------
        # 4. USING A VARIABLE
        # --------------------------------------------------

        st.header("4. Using a Variable")

        st.write(
            "After creating a variable, you can use its name later in your program."
        )

        st.code(
            '''name = "Anmol"
        print(name)''',
            language="python"
        )

        st.write("Output:")

        st.code(
            "Anmol",
            language="text"
        )

        st.write(
            "Python looks at `name`, finds the value stored there, "
            "and uses that value."
        )

        # --------------------------------------------------
        # 5. VARIABLES WITH print()
        # --------------------------------------------------

        st.header("5. Variables and print()")

        st.write(
            "You can use a variable inside `print()`."
        )

        st.code(
            '''name = "Anmol"
        age = 15

        print(name)
        print(age)''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """Anmol
        15""",
            language="text"
        )

        st.info(
            "The variable stores the information. `print()` displays it."
        )

        # --------------------------------------------------
        # 6. CHANGING A VARIABLE
        # --------------------------------------------------

        st.header("6. Changing the Value of a Variable")

        st.write(
            "A variable's value can be changed."
        )

        st.code(
            '''age = 15
        print(age)

        age = 16
        print(age)''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """15
        16""",
            language="text"
        )

        st.write(
            "First, `age` contains `15`."
        )

        st.write(
            "Then we assign `16` to `age`, so its value becomes `16`."
        )

        st.success(
            "A variable can hold a new value when you assign a new value to it."
        )

        # --------------------------------------------------
        # 7. MULTIPLE VARIABLES
        # --------------------------------------------------

        st.header("7. Creating Multiple Variables")

        st.write(
            "You can create many variables in the same program."
        )

        st.code(
            '''name = "Anmol"
        age = 15
        score = 500
        health = 100''',
            language="python"
        )

        st.write(
            "Each variable has its own name and value."
        )

        st.code(
            '''print(name)
        print(age)
        print(score)
        print(health)''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """Anmol
        15
        500
        100""",
            language="text"
        )

        # --------------------------------------------------
        # 8. VARIABLE NAMES
        # --------------------------------------------------

        st.header("8. Naming Variables")

        st.write(
            "When creating a variable, you need to give it a valid name."
        )

        st.write("Good variable names:")

        st.code(
            '''name = "Anmol"
        age = 15
        player_name = "Arion"
        player_score = 500''',
            language="python"
        )

        st.write(
            "Good names make your code easier to understand."
        )

        # --------------------------------------------------
        # 9. BASIC NAMING RULES
        # --------------------------------------------------

        st.header("9. Basic Variable Naming Rules")

        st.markdown(
            """
            ### Rule 1 — Use letters

            ```text
            name
            player
            score
            ```

            ### Rule 2 — Numbers can be used, but not at the beginning

            ```text
            player1
            score2
            ```

            But this is invalid:

            ```text
            1player
            ```

            ### Rule 3 — Don't use spaces

            Instead of:

            ```text
            player name
            ```

            Use an underscore:

            ```text
            player_name
            ```

            ### Rule 4 — Python is case-sensitive

            These are different variable names:

            ```text
            name
            Name
            NAME
            ```

            ### Rule 5 — Don't use Python's reserved words as variable names

            We will learn about these words later.
            """
        )

        # --------------------------------------------------
        # 10. CASE SENSITIVITY
        # --------------------------------------------------

        st.header("10. Variable Names Are Case-Sensitive")

        st.write(
            "Python treats uppercase and lowercase letters as different."
        )

        st.code(
            '''name = "Anmol"
        Name = "Rahul"

        print(name)
        print(Name)''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """Anmol
        Rahul""",
            language="text"
        )

        st.warning(
            "`name` and `Name` are two different variables."
        )

        # --------------------------------------------------
        # 11. CHANGING INFORMATION
        # --------------------------------------------------

        st.header("11. Variables Are Useful Because Information Can Change")

        st.write(
            "Imagine a game where the player's health changes."
        )

        st.code(
            '''health = 100

        health = 80

        health = 50

        health = 20''',
            language="python"
        )

        st.write(
            "The same variable can represent the player's current health "
            "as the value changes."
        )

        st.info(
            "This is one reason variables are extremely important in programming."
        )

        # --------------------------------------------------
        # 12. VARIABLES IN A SMALL PROGRAM
        # --------------------------------------------------

        st.header("12. Using Variables in a Small Program")

        st.write(
            "Let's combine what we have learned."
        )

        st.code(
            '''player_name = "Anmol"
        player_health = 100
        player_score = 500

        print(player_name)
        print(player_health)
        print(player_score)''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """Anmol
        100
        500""",
            language="text"
        )

        st.write(
            "Here we created three variables and then used them."
        )

        # --------------------------------------------------
        # 13. WHAT DOES = MEAN?
        # --------------------------------------------------

        st.header("13. What Does `=` Mean?")

        st.write(
            "In Python, `=` means assignment."
        )

        st.code(
            'age = 15',
            language="python"
        )

        st.write(
            "This means:"
        )

        st.markdown(
            """
            **Store the value `15` in the variable called `age`.**
            """
        )

        st.write(
            "It does not mean that `age` and `15` are mathematically equal."
        )

        st.info(
            "We will learn more about operators and comparisons in separate lessons."
        )

        # --------------------------------------------------
        # 14. COMMON BEGINNER MISTAKES
        # --------------------------------------------------

        st.header("14. Common Beginner Mistakes")

        st.subheader("❌ Mistake 1 — Using spaces in a variable name")

        st.code(
            'player name = "Anmol"',
            language="python"
        )

        st.write("Use an underscore instead:")

        st.code(
            'player_name = "Anmol"',
            language="python"
        )

        # --------------------------------------------------

        st.subheader("❌ Mistake 2 — Starting with a number")

        st.code(
            '1player = "Anmol"',
            language="python"
        )

        st.write("A variable name cannot start with a number.")

        st.code(
            'player1 = "Anmol"',
            language="python"
        )

        # --------------------------------------------------

        st.subheader("❌ Mistake 3 — Wrong capitalization")

        st.code(
            '''name = "Anmol"

        print(Name)''',
            language="python"
        )

        st.write(
            "`name` and `Name` are different variables."
        )

        # --------------------------------------------------

        st.subheader("❌ Mistake 4 — Forgetting to assign a value")

        st.code(
            '''name
        print(name)''',
            language="python"
        )

        st.write(
            "Before using a variable, make sure you have created and assigned it."
        )

        # --------------------------------------------------
        # 15. PREDICT THE OUTPUT
        # --------------------------------------------------

        st.divider()

        st.header("🧠 15. Predict the Output")

        st.write(
            "Try to predict what this program will display before running it."
        )

        st.code(
            '''name = "Anmol"
        age = 15

        print(name)
        print(age)''',
            language="python"
        )

        prediction = st.radio(
            "What will the program display?",
            [
                """name
        age""",

                """Anmol
        15""",

                """15
        Anmol""",

                """name
        15"""
            ]
        )

        if st.button("🔍 Check Answer"):

            if prediction == """Anmol
        15""":
                st.success("🎉 Correct! Python uses the values stored in the variables.")
            else:
                st.error(
                    "Not quite. Look at the values assigned to `name` and `age`."
            )

        # --------------------------------------------------
        # 16. PRACTICE
        # --------------------------------------------------

        st.header("📝 16. Practice")

        st.write(
            "Create three variables:"
        )

        st.code(
            '''name = "Your Name"
        age = 15
        game = "Your Game"''',
            language="python"
        )

        st.write(
            "Then use `print()` to display each variable."
        )

        st.code(
            '''print(name)
        print(age)
        print(game)''',
            language="python"
        )

        st.write(
            "Try changing the values to your own information."
        )

        # --------------------------------------------------
        # 17. MINI CHALLENGE
        # --------------------------------------------------

        st.header("🔥 17. Mini Challenge")

        st.write(
            "Create a small game player profile using variables."
        )

        st.write(
            "Your program should have variables for:"
        )

        st.markdown(
            """
            - Player name
            - Player health
            - Player score
            - Player level
            """

        )

        st.write(
            "For example:"
        )

        st.code(
            '''player_name = "Anmol"
        health = 100
        score = 500
        level = 1

        print(player_name)
        print(health)
        print(score)
        print(level)''',
            language="python"
        )

        st.write(
            "Now change the values and make your own player."
        )

        # --------------------------------------------------
        # 18. INTERACTIVE VARIABLE PRACTICE
        # --------------------------------------------------

        st.header("💻 18. Build Your Own Variables")

        name_input = st.text_input(
            "Player Name",
            "Anmol"
        )

        health_input = st.number_input(
            "Health",
            min_value=0,
            value=100
        )

        score_input = st.number_input(
            "Score",
            min_value=0,
            value=500
        )

        if st.button("▶ Create Player"):

            st.write("Your Python variables would look like:")

            st.code(
                f'''player_name = "{name_input}"
        health = {health_input}
        score = {score_input}''',
                language="python"
            )

            st.write("Values stored:")

            st.write(f"Player Name: **{name_input}**")
            st.write(f"Health: **{health_input}**")
            st.write(f"Score: **{score_input}**")

        # --------------------------------------------------
        # 19. QUICK QUIZ
        # --------------------------------------------------

        st.divider()

        st.header("📚 19. Quick Quiz")

        q1 = st.radio(
            "1. What is a variable?",
            [
                "A Python error",
                "A name used to store a value",
                "A type of loop",
                "A Python file"
            ]
        )

        q2 = st.radio(
            "2. What does the `=` symbol do when creating a variable?",
            [
                "Assigns a value",
                "Prints a value",
                "Deletes a value",
                "Starts a loop"
            ]
        )

        q3 = st.radio(
            "3. Which is a valid variable name?",
            [
                "player name",
                "1player",
                "player_name",
                "player-name"
            ]
        )

        q4 = st.radio(
            "4. What happens here?\n\nage = 15\nage = 16",
            [
                "age remains 15",
                "age becomes 16",
                "Python creates two ages",
                "Python deletes age"
            ]
        )

        q5 = st.radio(
            "5. Are `name` and `Name` the same variable in Python?",
            [
                "Yes",
                "No",
                "Only sometimes",
                "Only on Linux"
            ]
        )

        if st.button("✅ Check Quiz"):

            score = 0

            if q1 == "A name used to store a value":
                score += 1

            if q2 == "Assigns a value":
                score += 1

            if q3 == "player_name":
                score += 1

            if q4 == "age becomes 16":
                score += 1

            if q5 == "No":
                score += 1

            st.write(f"### Your Score: {score}/5")

            if score == 5:
                st.success("🎉 Perfect! You understand variables!")

            elif score >= 3:
                st.info(
                    "👍 Good job! Review the sections you found difficult."
                )

            else:
                st.warning(
                    "Keep practicing. Read the lesson again and try the quiz once more."
                )

        # --------------------------------------------------
        # SUMMARY
        # --------------------------------------------------

        st.divider()

        st.header("📚 What You Learned")

        st.markdown(
            """
            By the end of this lesson, you should understand:

            - What a variable is
            - Why variables are useful
            - How to create a variable
            - How to assign a value
            - How to use a variable
            - How to use variables with `print()`
            - How to change a variable's value
            - How to create multiple variables
            - Basic variable naming rules
            - That Python is case-sensitive
            - What the `=` assignment symbol means
            """
        )

        # --------------------------------------------------
        # NEXT LESSON
        # --------------------------------------------------

        st.divider()

        st.header("🚀 Next Lesson")

        st.write(
            "Next, we will learn about **Basic Data Types**."
        )

        st.write(
            "We will learn what kinds of values Python can work with "
            "and how Python treats different kinds of information."
        )

        st.success("🎯 Lesson 6 Complete!")
    elif st.session_state.current_topic == "7. Basic Data Types":


        # --------------------------------------------------
        # TITLE
        # --------------------------------------------------

        st.title("🐍 Lesson 7 — Basic Data Types")

        st.write(
            "In this lesson, you will learn about the different types of "
            "values Python can store and work with."
        )

        st.info(
            "A data type tells Python what kind of value something is."
        )

        st.divider()

        # --------------------------------------------------
        # 1. WHAT IS A DATA TYPE?
        # --------------------------------------------------

        st.header("1. What Is a Data Type?")

        st.write(
            "Just like we have different kinds of information in real life, "
            "Python also works with different kinds of values."
        )

        st.write("For example:")

        st.code(
            '''name = "Anmol"
        age = 15
        height = 5.8
        is_playing = True''',
            language="python"
        )

        st.write(
            "These values are different kinds of data."
        )

        st.markdown(
            """
            - `"Anmol"` → text
            - `15` → whole number
            - `5.8` → decimal number
            - `True` → true/false value
            """
        )

        st.success(
            "These different kinds of values are called data types."
        )

        # --------------------------------------------------
        # 2. THE 7 BASIC DATA TYPES
        # --------------------------------------------------

        st.header("2. The 7 Basic Data Types")

        st.write(
            "In this course, we will start with these seven important Python data types:"
        )

        data = {
            "Data Type": [
                "str",
                "int",
                "float",
                "bool",
                "list",
                "tuple",
                "dict"
            ],
            "Meaning": [
                "String",
                "Integer",
                "Floating-point number",
                "Boolean",
                "List",
                "Tuple",
                "Dictionary"
            ],
            "Example": [
                '"Hello"',
                "25",
                "3.14",
                "True",
                '[1, 2, 3]',
                '(1, 2, 3)',
                '{"name": "Anmol"}'
            ]
        }

        st.table(data)

        # --------------------------------------------------
        # 3. STRING
        # --------------------------------------------------

        st.header("3. String — `str`")

        st.write(
            "A string is text."
        )

        st.write(
            "Strings are written inside quotation marks."
        )

        st.code(
            '''name = "Anmol"
        game = "My Adventure"
        message = "Hello World"''',
            language="python"
        )

        st.write("Examples of strings:")

        st.code(
            '''print("Hello")
        print("Python")
        print("123")
        print("This is text")''',
            language="python"
        )

        st.warning(
            "Even though `\"123\"` contains digits, it is a string because it is inside quotation marks."
        )

        st.info(
            "String type name: `str`"
        )

        # --------------------------------------------------
        # 4. INTEGER
        # --------------------------------------------------

        st.header("4. Integer — `int`")

        st.write(
            "An integer is a whole number without a decimal part."
        )

        st.code(
            '''age = 15
        score = 500
        health = 100
        lives = 3''',
            language="python"
        )

        st.write("Examples:")

        st.code(
            '''10
        25
        100
        -5
        0''',
            language="python"
        )

        st.info(
            "Integer type name: `int`"
        )

        st.warning(
            "Numbers such as `10.5` are not integers because they contain a decimal part."
        )

        # --------------------------------------------------
        # 5. FLOAT
        # --------------------------------------------------

        st.header("5. Float — `float`")

        st.write(
            "A float is a number that contains a decimal point."
        )

        st.code(
            '''height = 5.8
        price = 99.99
        temperature = 36.5''',
            language="python"
        )

        st.write("Examples:")

        st.code(
            '''3.14
        10.5
        0.5
        99.99''',
            language="python"
        )

        st.info(
            "Float type name: `float`"
        )

        # --------------------------------------------------
        # 6. BOOLEAN
        # --------------------------------------------------

        st.header("6. Boolean — `bool`")

        st.write(
            "A boolean represents one of two values:"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("True")
            st.write("Something is true.")

            st.code(
                "True",
                language="python"
            )

        with col2:
            st.subheader("False")
            st.write("Something is false.")

            st.code(
                "False",
                language="python"
            )

        st.code(
            '''is_playing = True
        has_key = False''',
            language="python"
        )

        st.info(
            "Boolean type name: `bool`"
        )

        st.warning(
            "`True` and `False` must start with a capital letter."
        )

        # --------------------------------------------------
        # 7. LIST
        # --------------------------------------------------

        st.header("7. List — `list`")

        st.write(
            "A list allows you to store multiple values together."
        )

        st.code(
            '''fruits = ["apple", "banana", "mango"]''',
            language="python"
        )

        st.write(
            "Here, one variable contains three values."
        )

        st.code(
            '''numbers = [10, 20, 30, 40]
        names = ["Anmol", "Rahul", "Aman"]''',
            language="python"
        )

        st.write(
            "A list is written using square brackets: `[ ]`"
        )

        st.info(
            "List type name: `list`"
        )

        # --------------------------------------------------
        # 8. LIST CAN CONTAIN DIFFERENT VALUES
        # --------------------------------------------------

        st.header("8. Lists Can Store Different Values")

        st.write(
            "A list can contain different kinds of values."
        )

        st.code(
            '''player = ["Anmol", 100, 500, True]''',
            language="python"
        )

        st.write(
            "This list contains:"
        )

        st.markdown(
            """
            - Text → `"Anmol"`
            - Integer → `100`
            - Integer → `500`
            - Boolean → `True`
            """
        )

        # --------------------------------------------------
        # 9. TUPLE
        # --------------------------------------------------

        st.header("9. Tuple — `tuple`")

        st.write(
            "A tuple is another way to store multiple values together."
        )

        st.code(
            '''coordinates = (10, 20)
        colors = ("red", "green", "blue")''',
            language="python"
        )

        st.write(
            "A tuple is written using parentheses: `( )`"
        )

        st.info(
            "Tuple type name: `tuple`"
        )

        st.write(
            "For now, remember the basic difference:"
        )

        comparison = {
            "Type": ["List", "Tuple"],
            "Written using": ["[ ]", "( )"],
            "Example": ["[10, 20, 30]", "(10, 20, 30)"]
        }

        st.table(comparison)

        st.write(
            "We will learn the important differences between lists and tuples "
            "in a later lesson."
        )

        # --------------------------------------------------
        # 10. DICTIONARY
        # --------------------------------------------------

        st.header("10. Dictionary — `dict`")

        st.write(
            "A dictionary stores information using **keys and values**."
        )

        st.code(
            '''player = {
            "name": "Anmol",
            "health": 100,
            "score": 500
        }''',
            language="python"
        )

        st.write(
            "Here:"
        )

        st.markdown(
            """
            - `"name"` is a key
            - `"Anmol"` is its value
            - `"health"` is a key
            - `100` is its value
            - `"score"` is a key
            - `500` is its value
            """
        )

        st.info(
            "Dictionary type name: `dict`"
        )

        # --------------------------------------------------
        # 11. DICTIONARY REAL-LIFE EXAMPLE
        # --------------------------------------------------

        st.header("11. Think of a Dictionary Like a Record")

        st.write(
            "Imagine you have a player information card:"
        )

        st.code(
            '''Name: Anmol
        Health: 100
        Score: 500''',
            language="text"
        )

        st.write(
            "A Python dictionary can represent this kind of information:"
        )

        st.code(
            '''player = {
            "name": "Anmol",
            "health": 100,
            "score": 500
        }''',
            language="python"
        )

        st.success(
            "Keys help identify what each value represents."
        )

        # --------------------------------------------------
        # 12. CHECKING THE DATA TYPE
        # --------------------------------------------------

        st.header("12. Checking a Data Type")

        st.write(
            "Python provides a function called `type()` that can tell us "
            "what type of value something is."
        )

        st.code(
            '''print(type("Hello"))
        print(type(10))
        print(type(3.14))
        print(type(True))''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """<class 'str'>
        <class 'int'>
        <class 'float'>
        <class 'bool'>""",
            language="text"
        )

        st.info(
            "`type()` tells Python to show us what kind of value something is."
        )

        # --------------------------------------------------
        # 13. CHECKING VARIABLES
        # --------------------------------------------------

        st.header("13. Checking the Type of a Variable")

        st.write(
            "You can also use `type()` with variables."
        )

        st.code(
            '''name = "Anmol"
        age = 15
        height = 5.8

        print(type(name))
        print(type(age))
        print(type(height))''',
            language="python"
        )

        st.write("Output:")

        st.code(
            """<class 'str'>
        <class 'int'>
        <class 'float'>""",
            language="text"
        )

        # --------------------------------------------------
        # 14. ONE VARIABLE, ONE VALUE TYPE
        # --------------------------------------------------

        st.header("14. Understanding the Value Stored in a Variable")

        st.code(
            '''age = 15''',
            language="python"
        )

        st.write(
            "The value stored in `age` is `15`, which is an integer."
        )

        st.code(
            "print(type(age))",
            language="python"
        )

        st.code(
            "<class 'int'>",
            language="text"
        )

        st.write(
            "The type belongs to the value stored in the variable."
        )

        # --------------------------------------------------
        # 15. COMPARING THE BASIC TYPES
        # --------------------------------------------------

        st.header("15. Quick Comparison")

        comparison_data = {
            "Type": [
                "str",
                "int",
                "float",
                "bool",
                "list",
                "tuple",
                "dict"
            ],
            "Example": [
                '"Hello"',
                "10",
                "3.14",
                "True",
                "[1, 2, 3]",
                "(1, 2, 3)",
                '{"name": "Anmol"}'
            ],
            "Used For": [
                "Text",
                "Whole numbers",
                "Decimal numbers",
                "True/False values",
                "Multiple values",
                "Multiple values",
                "Key-value information"
            ]
        }

        st.table(comparison_data)

        # --------------------------------------------------
        # 16. COMMON BEGINNER MISTAKES
        # --------------------------------------------------

        st.header("16. Common Beginner Mistakes")

        st.subheader("❌ Mistake 1 — Thinking \"10\" and 10 are the same type")

        st.code(
            '''print(type("10"))
        print(type(10))''',
            language="python"
        )

        st.write(
            "`\"10\"` is a string, while `10` is an integer."
        )

        # --------------------------------------------------

        st.subheader("❌ Mistake 2 — Forgetting the capital letters in Boolean values")

        st.code(
            '''is_alive = true
        is_game_over = false''',
            language="python"
        )

        st.write(
            "Python uses `True` and `False` with capital T and F."
        )

        st.code(
            '''is_alive = True
        is_game_over = False''',
            language="python"
        )

        # --------------------------------------------------

        st.subheader("❌ Mistake 3 — Confusing a list and a tuple")

        st.code(
            '''my_list = [1, 2, 3]
        my_tuple = (1, 2, 3)''',
            language="python"
        )

        st.write(
            "The brackets tell you which one is a list and which one is a tuple."
        )

        # --------------------------------------------------

        st.subheader("❌ Mistake 4 — Forgetting dictionary keys")

        st.code(
            '''player = {
            "name": "Anmol",
            "health": 100
        }''',
            language="python"
        )

        st.write(
            "A dictionary stores information as key-value pairs."
        )

        # --------------------------------------------------
        # 17. PREDICT THE TYPES
        # --------------------------------------------------

        st.divider()

        st.header("🧠 17. Predict the Data Types")

        st.write(
            "Try to identify the data type of each value before checking the answer."
        )

        st.code(
            '''a = "Python"
        b = 25
        c = 3.14
        d = True
        e = [1, 2, 3]
        f = (1, 2, 3)
        g = {"name": "Anmol"}''',
            language="python"
        )

        prediction = st.selectbox(
            "What is the data type of `c`?",
            [
                "str",
                "int",
                "float",
                "bool"
            ]
        )

        if st.button("🔍 Check Answer"):

            if prediction == "float":
                st.success("🎉 Correct! `3.14` is a decimal number, so it is a float.")
            else:
                st.error("Not quite. `3.14` contains a decimal point.")

        # --------------------------------------------------
        # 18. PRACTICE
        # --------------------------------------------------

        st.header("📝 18. Practice")

        st.write(
            "Create the following variables:"
        )

        st.code(
            '''name = "Your Name"
        age = 15
        height = 5.8
        is_student = True
        fruits = ["apple", "banana"]
        coordinates = (10, 20)
        player = {"name": "Your Name", "score": 100}''',
            language="python"
        )

        st.write(
            "Then use `type()` to check the type of every variable."
        )

        st.code(
            '''print(type(name))
        print(type(age))
        print(type(height))
        print(type(is_student))
        print(type(fruits))
        print(type(coordinates))
        print(type(player))''',
            language="python"
        )

        # --------------------------------------------------
        # 19. MINI CHALLENGE
        # --------------------------------------------------

        st.header("🔥 19. Mini Challenge")

        st.write(
            "Create a character using all seven data types."
        )

        st.write(
            "Try to include:"
        )

        st.markdown(
            """
            - A string for the character's name
            - An integer for health
            - A float for speed
            - A boolean for whether the character is alive
            - A list for items
            - A tuple for position
            - A dictionary for character information
            """
        )

        st.write("Example:")

        st.code(
            '''name = "Arion"
        health = 100
        speed = 5.5
        is_alive = True

        items = ["Sword", "Key", "Potion"]

        position = (100, 200)

        character = {
            "name": "Arion",
            "health": 100
        }''',
            language="python"
        )

        st.write(
            "Now create your own character by changing the values."
        )

        # --------------------------------------------------
        # 20. QUICK QUIZ
        # --------------------------------------------------

        st.divider()

        st.header("📚 20. Quick Quiz")

        q1 = st.radio(
            "1. Which data type is used for text?",
            [
                "int",
                "str",
                "float",
                "bool"
            ]
        )

        q2 = st.radio(
            "2. Which data type is 25?",
            [
                "str",
                "float",
                "int",
                "bool"
            ]
        )

        q3 = st.radio(
            "3. Which data type is 3.14?",
            [
                "int",
                "str",
                "float",
                "bool"
            ]
        )

        q4 = st.radio(
            "4. Which data type has True and False?",
            [
                "list",
                "tuple",
                "dict",
                "bool"
            ]
        )

        q5 = st.radio(
            "5. Which one is a list?",
            [
                "(1, 2, 3)",
                "{1, 2, 3}",
                "[1, 2, 3]",
                '"1, 2, 3"'
            ]
        )

        q6 = st.radio(
            "6. Which one is a tuple?",
            [
                "[1, 2, 3]",
                "(1, 2, 3)",
                '{"a": 1}',
                '"1, 2, 3"'
            ]
        )

        q7 = st.radio(
            "7. Which data type uses key-value pairs?",
            [
                "str",
                "int",
                "list",
                "dict"
            ]
        )

        if st.button("✅ Check Quiz"):

            score = 0

            if q1 == "str":
                score += 1

            if q2 == "int":
                score += 1

            if q3 == "float":
                score += 1

            if q4 == "bool":
                score += 1

            if q5 == "[1, 2, 3]":
                score += 1

            if q6 == "(1, 2, 3)":
                score += 1

            if q7 == "dict":
                score += 1

            st.write(f"### Your Score: {score}/7")

            if score == 7:
                st.success("🎉 Perfect! You understand the seven basic data types!")

            elif score >= 5:
                st.info(
                    "👍 Very good! Review the types you got wrong."
                )

            elif score >= 3:
                st.warning(
                    "Keep practicing. Go through the lesson again."
                )

            else:
                st.error(
                    "Don't worry! Review the lesson and try the quiz again."
                )

        # --------------------------------------------------
        # SUMMARY
        # --------------------------------------------------

        st.divider()

        st.header("📚 What You Learned")

        st.markdown(
            """
            You learned the seven basic Python data types:

            - `str` → String → Text
            - `int` → Integer → Whole numbers
            - `float` → Float → Decimal numbers
            - `bool` → Boolean → True or False
            - `list` → List → Collection of values
            - `tuple` → Tuple → Collection of values
            - `dict` → Dictionary → Key-value information

            You also learned:

            - What a data type is
            - How to use `type()`
            - How to recognize different types of values
            - The basic difference between lists and tuples
            - How dictionaries use keys and values
            """
        )

        # --------------------------------------------------
        # NEXT LESSON
        # --------------------------------------------------

        st.divider()

        st.header("🚀 Next Lesson")

        st.write(
            "Next, we will learn **Basic Math in Python**."
        )

        st.write(
            "You will learn how Python performs calculations using numbers "
            "and mathematical operators."
        )

        st.success("🎯 Lesson 7 Complete!")
        st.divider()
    elif st.session_state.current_topic == "8. Basic Math":


        st.title("🐍 Lesson 8 — Basic Math")

        st.write(
            "Python can be used as a calculator. "
            "In this lesson, you will learn how to perform mathematical calculations using Python."
        )

        st.divider()


        # ============================================================
        # 1. PYTHON AS A CALCULATOR
        # ============================================================

        st.header("1. Python Can Do Math")

        st.write(
            "Just like a calculator, Python can perform mathematical calculations."
        )

        st.code(
            """5 + 3
        10 - 4
        6 * 2
        20 / 5""",
            language="python"
        )

        st.write("Python calculates these expressions and produces results.")

        st.info(
            "An expression is a piece of code that Python can calculate."
        )


        # ============================================================
        # 2. ADDITION
        # ============================================================

        st.header("2. Addition — +")

        st.write(
            "Use the `+` symbol to add numbers."
        )

        st.code(
            """5 + 3

        10 + 20
        100 + 50""",
            language="python"
        )

        st.write("Examples:")

        st.code(
            """5 + 3
        # 8

        10 + 20
        # 30""",
            language="python"
        )

        st.success("The `+` symbol means addition.")


        # ============================================================
        # 3. SUBTRACTION
        # ============================================================

        st.header("3. Subtraction — -")

        st.write(
            "Use the `-` symbol to subtract numbers."
        )

        st.code(
            """10 - 4

        20 - 7
        50 - 25""",
            language="python"
        )

        st.write("Examples:")

        st.code(
            """10 - 4
        # 6

        20 - 7
        # 13""",
            language="python"
        )

        st.success("The `-` symbol means subtraction.")


        # ============================================================
        # 4. MULTIPLICATION
        # ============================================================

        st.header("4. Multiplication — *")

        st.write(
            "In Python, multiplication uses the `*` symbol."
        )

        st.write(
            "Python does NOT use `×` for multiplication."
        )

        st.code(
            """5 * 3

        10 * 2
        20 * 5""",
            language="python"
        )

        st.write("Examples:")

        st.code(
            """5 * 3
        # 15

        10 * 2
        # 20""",
            language="python"
        )

        st.success("The `*` symbol means multiplication.")


        # ============================================================
        # 5. DIVISION
        # ============================================================

        st.header("5. Division — /")

        st.write(
            "Use the `/` symbol to divide numbers."
        )

        st.code(
            """10 / 2

        20 / 5
        15 / 3""",
            language="python"
        )

        st.write("Examples:")

        st.code(
            """10 / 2
        # 5.0

        20 / 5
        # 4.0""",
            language="python"
        )

        st.info(
            "Notice that `/` normally produces a decimal number in Python, "
            "even when the answer is a whole number."
        )


        # ============================================================
        # 6. FOUR BASIC OPERATIONS
        # ============================================================

        st.header("6. The Four Basic Operations")

        st.write("Here are the four main mathematical operators:")

        st.table({
            "Operation": ["Addition", "Subtraction", "Multiplication", "Division"],
            "Symbol": ["+", "-", "*", "/"],
            "Example": ["5 + 2", "5 - 2", "5 * 2", "5 / 2"],
            "Result": ["7", "3", "10", "2.5"]
        })


        # ============================================================
        # 7. MODULO
        # ============================================================

        st.header("7. Remainder — %")

        st.write(
            "The `%` operator gives us the remainder after division."
        )

        st.code(
            """10 % 3

        7 % 2

        20 % 5""",
            language="python"
        )

        st.write("Examples:")

        st.code(
            """10 % 3
        # 1

        7 % 2
        # 1

        20 % 5
        # 0""",
            language="python"
        )

        st.write(
            "Why is `10 % 3` equal to `1`?"
        )

        st.code(
            """10 ÷ 3

        3 goes into 10 three times.

        3 × 3 = 9

        10 - 9 = 1

        Therefore:

        10 % 3
        # 1""",
            language="text"
        )

        st.info(
            "The `%` operator is called the modulo operator. "
            "It gives the remainder."
        )


        # ============================================================
        # 8. FLOOR DIVISION
        # ============================================================

        st.header("8. Floor Division — //")

        st.write(
            "`//` performs division and removes the decimal part "
            "by taking the floor of the result."
        )

        st.code(
            """10 // 3

        20 // 6

        15 // 5""",
            language="python"
        )

        st.write("Examples:")

        st.code(
            """10 // 3
        # 3

        20 // 6
        # 3

        15 // 5
        # 3""",
            language="python"
        )

        st.info(
            "Compare `/` and `//`:"
        )

        st.code(
            """10 / 3
        # 3.3333333333333335

        10 // 3
        # 3""",
            language="python"
        )


        # ============================================================
        # 9. POWER
        # ============================================================

        st.header("9. Power — **")

        st.write(
            "Python uses `**` to calculate powers."
        )

        st.code(
            """2 ** 3

        5 ** 2

        10 ** 2""",
            language="python"
        )

        st.write("Examples:")

        st.code(
            """2 ** 3
        # 8

        5 ** 2
        # 25

        10 ** 2
        # 100""",
            language="python"
        )

        st.write(
            "`2 ** 3` means 2 raised to the power of 3."
        )

        st.code(
            """2 × 2 × 2 = 8""",
            language="text"
        )

        st.success("The `**` symbol means power/exponentiation.")


        # ============================================================
        # 10. PARENTHESES
        # ============================================================

        st.header("10. Using Parentheses")

        st.write(
            "Parentheses `()` can be used to control which calculation "
            "Python performs first."
        )

        st.code(
            """2 + 3 * 4

        (2 + 3) * 4""",
            language="python"
        )

        st.write("These give different results:")

        st.code(
            """2 + 3 * 4
        # 14

        (2 + 3) * 4
        # 20""",
            language="python"
        )

        st.info(
            "Python follows mathematical order of operations. "
            "Parentheses can be used when you want a specific part "
            "of the calculation to happen first."
        )


        # ============================================================
        # 11. ORDER OF OPERATIONS
        # ============================================================

        st.header("11. Order of Operations")

        st.write(
            "When an expression contains multiple operators, "
            "Python follows an order."
        )

        st.write("A simplified beginner-friendly order is:")

        st.markdown(
            """
            1. **Parentheses** `()`
            2. **Power** `**`
            3. **Multiplication, Division, Floor Division, Modulo** `* / // %`
            4. **Addition and Subtraction** `+ -`
            """
        )

        st.code(
            """2 + 3 * 4
        # 14""",
            language="python"
        )

        st.write(
            "Python performs `3 * 4` first, then adds `2`."
        )

        st.code(
            """2 + (3 * 4)
        # 14""",
            language="python"
        )


        # ============================================================
        # 12. NUMBERS AND DECIMALS
        # ============================================================

        st.header("12. Math With Decimal Numbers")

        st.write(
            "Python can also perform calculations using decimal numbers."
        )

        st.code(
            """5.5 + 2.5

        10.5 - 3.2

        2.5 * 4

        10.0 / 2""",
            language="python"
        )

        st.write("Example:")

        st.code(
            """5.5 + 2.5
        # 8.0""",
            language="python"
        )

        st.info(
            "Decimal numbers are called `float` values. "
            "You learned about floats in the previous lesson."
        )


        # ============================================================
        # 13. MATH WITH VARIABLES
        # ============================================================

        st.header("13. Using Math With Variables")

        st.write(
            "You can also perform calculations using values stored in variables."
        )

        st.code(
            """a = 10
        b = 5

        a + b
        a - b
        a * b
        a / b""",
            language="python"
        )

        st.write(
            "Here, Python uses the values stored in `a` and `b` "
            "to perform the calculations."
        )

        st.code(
            """a = 10
        b = 5

        print(a + b)

        # 15""",
            language="python"
        )

        st.info(
            "Variables were taught in Lesson 6. "
            "We are only using them here to perform math."
        )


        # ============================================================
        # 14. PRACTICAL EXAMPLE
        # ============================================================

        st.header("14. Practical Example")

        st.write(
            "Imagine you have 5 apples and buy 3 more."
        )

        st.code(
            """apples = 5
        more_apples = 3

        print(apples + more_apples)

        # 8""",
            language="python"
        )

        st.write(
            "Python adds the two numbers and gives us `8`."
        )


        # ============================================================
        # 15. COMMON MISTAKES
        # ============================================================

        st.header("15. Common Beginner Mistakes")

        st.subheader("Mistake 1 — Using ×")

        st.code(
            """5 × 3""",
            language="text"
        )

        st.error(
            "Python does not use `×` for multiplication."
        )

        st.write("Correct:")

        st.code(
            """5 * 3""",
            language="python"
        )


        st.subheader("Mistake 2 — Using ÷")

        st.code(
            """10 ÷ 2""",
            language="text"
        )

        st.error(
            "Python uses `/` for division."
        )

        st.write("Correct:")

        st.code(
            """10 / 2""",
            language="python"
        )


        st.subheader("Mistake 3 — Forgetting the second * for power")

        st.write("Power uses two stars:")

        st.code(
            """2 ** 3""",
            language="python"
        )


        st.subheader("Mistake 4 — Confusing / and //")

        st.code(
            """10 / 3
        # 3.3333333333333335

        10 // 3
        # 3""",
            language="python"
        )


        # ============================================================
        # 16. PREDICT THE ANSWER
        # ============================================================

        st.header("16. Predict the Answer")

        st.write(
            "Before looking at the answer, try to calculate these yourself."
        )

        st.code(
            """1. 10 + 5
        2. 20 - 8
        3. 6 * 4
        4. 20 / 5
        5. 10 % 3
        6. 2 ** 4""",
            language="text"
        )

        show_answers = st.button("Show Answers")

        if show_answers:
            st.success(
                """
                1. 15

                2. 12

                3. 24

                4. 4.0

                5. 1

                6. 16
                """
            )


        # ============================================================
        # 17. INTERACTIVE CALCULATOR
        # ============================================================

        st.header("17. Interactive Math Practice")

        st.write(
            "Choose two numbers and an operation."
        )

        col1, col2 = st.columns(2)

        with col1:
            number1 = st.number_input(
                "First number",
                value=10.0
            )

        with col2:
            number2 = st.number_input(
                "Second number",
                value=5.0
            )

        operation = st.selectbox(
                "Choose an operation",
                [
                    "Addition (+)",
                    "Subtraction (-)",
                    "Multiplication (*)",
                    "Division (/)",
                    "Remainder (%)",
                    "Floor Division (//)",
                    "Power (**)"
                ]
        )

        calculate = st.button("Calculate")

        if calculate:

            if operation == "Addition (+)":
                result = number1 + number2
                st.success(f"Result: {result}")

            elif operation == "Subtraction (-)":
                result = number1 - number2
                st.success(f"Result: {result}")

            elif operation == "Multiplication (*)":
                result = number1 * number2
                st.success(f"Result: {result}")

            elif operation == "Division (/)" :

                if number2 == 0:
                    st.error("You cannot divide by zero.")
                else:
                    result = number1 / number2
                    st.success(f"Result: {result}")

            elif operation == "Remainder (%)":

                if number2 == 0:
                    st.error("You cannot divide by zero.")
                else:
                    result = number1 % number2
                    st.success(f"Result: {result}")

            elif operation == "Floor Division (//)":

                if number2 == 0:
                    st.error("You cannot divide by zero.")
                else:
                    result = number1 // number2
                    st.success(f"Result: {result}")

            elif operation == "Power (**)":
                result = number1 ** number2
                st.success(f"Result: {result}")


        # ============================================================
        # 18. PRACTICE
        # ============================================================

        st.header("18. Practice")

        st.write("Try writing these calculations in Python:")

        st.markdown(
            """
            ### Practice 1
            Add `25` and `15`.

            ### Practice 2
            Subtract `30` from `100`.

            ### Practice 3
            Multiply `12` by `5`.

            ### Practice 4
            Divide `50` by `10`.

            ### Practice 5
            Find the remainder when `17` is divided by `5`.

            ### Practice 6
            Calculate `3` raised to the power of `4`.

            ### Practice 7
            Calculate:

            `(10 + 5) * 2`
            """
        )

        practice_answer = st.text_area(
            "Write your answers here:",
            height=180
        )

        if st.button("Check Practice"):
            st.info(
                "Try calculating each answer yourself first. "
                "Then compare your answers with Python by running the code."
            )


        # ============================================================
        # 19. MINI CHALLENGE
        # ============================================================

        st.header("19. Mini Challenge 🧠")

        st.write(
            "Create a small Python program that calculates the total "
            "price of three items."
        )

        st.write("Use these prices:")

        st.code(
            """item1 = 50
        item2 = 30
        item3 = 20""",
            language="python"
        )

        st.write(
            "Your program should calculate:"
        )

        st.code(
            """50 + 30 + 20""",
            language="python"
        )

        st.write(
            "Try writing the complete code yourself."
        )

        challenge = st.text_area(
            "Write your solution:",
            height=150
        )

        if st.button("Show Challenge Solution"):
            st.code(
                """item1 = 50
        item2 = 30
        item3 = 20

        total = item1 + item2 + item3

        print(total)""",
                language="python"
            )

            st.success("The answer should be 100.")


        # ============================================================
        # 20. QUICK QUIZ
        # ============================================================

        st.header("20. Quick Quiz 🎯")

        q1 = st.radio(
            "1. Which symbol is used for multiplication?",
            [
                "+",
                "*",
                "x",
                "%"
            ],
            key="q1"
        )

        q2 = st.radio(
            "2. What does `/` do?",
            [
                "Addition",
                "Subtraction",
                "Division",
                "Power"
            ],
            key="q2"
        )

        q3 = st.radio(
            "3. What does `%` give?",
            [
                "The remainder",
                "The power",
                "The average",
                "The decimal"
            ],
            key="q3"
        )

        q4 = st.radio(
            "4. What is `2 ** 3`?",
            [
                "5",
                "6",
                "8",
                "9"
            ],
            key="q4"
        )

        q5 = st.radio(
            "5. What is `10 // 3`?",
            [
                "3",
                "3.33",
                "1",
                "10"
            ],
            key="q5"
        )

        q6 = st.radio(
            "6. What is `2 + 3 * 4`?",
            [
                "20",
                "14",
                "24",
                "9"
            ],
            key="q6"
        )

        if st.button("Submit Quiz"):

            score = 0

            if q1 == "*":
                score += 1

            if q2 == "Division":
                score += 1

            if q3 == "The remainder":
                score += 1

            if q4 == "8":
                score += 1

            if q5 == "3":
                score += 1

            if q6 == "14":
                score += 1

            st.success(f"You scored {score}/6!")

            if score == 6:
                st.balloons()
                st.success("Excellent! 🎉 You understand the basics of Python math.")

            elif score >= 4:
                st.info("Good job! Review the questions you missed.")

            else:
                st.warning("Review the lesson and try the quiz again.")


        # ============================================================
        # 21. WHAT YOU LEARNED
        # ============================================================

        st.header("📚 What You Learned")

        st.markdown(
            """
            By completing this lesson, you learned:

            - How Python performs mathematical calculations
            - Addition `+`
            - Subtraction `-`
            - Multiplication `*`
            - Division `/`
            - Remainder `%`
            - Floor division `//`
            - Power `**`
            - Using parentheses `()`
            - Basic order of operations
            - Math with decimal numbers
            - Using variables in calculations
            """
        )

        st.success(
            "You can now use Python as a basic calculator!"
        )


        # ============================================================
        # 22. NEXT LESSON
        # ============================================================

        st.header("➡️ Next Lesson")

        st.write(
            "**Lesson 9 — Assignment**"
        )

        st.write(
            "In the next lesson, we will learn more deeply about "
            "how Python assigns and changes values using `=`."
        )
    elif st.session_state.current_topic == "9. Assignment":

        st.title("🐍 Lesson 9 — Assignment")

        st.write(
            "In this lesson, you will learn how Python gives values to variables "
            "and how you can change those values."
        )

        st.divider()


        # ============================================================
        # 1. WHAT IS ASSIGNMENT?
        # ============================================================

        st.header("1. What Is Assignment?")

        st.write(
            "Assignment means giving a value to a variable."
        )

        st.write(
            "In Python, we use the `=` symbol for assignment."
        )

        st.code(
            """age = 15""",
            language="python"
        )

        st.write(
            "Here, Python takes the value `15` and assigns it to the variable `age`."
        )

        st.info(
            "Assignment is about giving a value to a variable."
        )


        # ============================================================
        # 2. UNDERSTANDING =
        # ============================================================

        st.header("2. What Does `=` Mean?")

        st.write(
            "The `=` symbol in Python means:"
        )

        st.markdown(
            """
            **"Assign the value on the right to the variable on the left."**
            """
        )

        st.code(
            """age = 15""",
            language="python"
        )

        st.write("Think about it like this:")

        st.code(
            """age  ←  15""",
            language="text"
        )

        st.write(
            "The variable `age` now contains the value `15`."
        )


        # ============================================================
        # 3. ASSIGNING DIFFERENT TYPES OF VALUES
        # ============================================================

        st.header("3. Assigning Different Values")

        st.write(
            "You can assign different kinds of values to variables."
        )

        st.code(
            """name = "Anmol"

        age = 15

        height = 5.8

        is_student = True""",
            language="python"
        )

        st.write(
            "Each variable receives a value."
        )

        st.table({
            "Variable": ["name", "age", "height", "is_student"],
            "Assigned Value": ['"Anmol"', "15", "5.8", "True"]
        })


        # ============================================================
        # 4. ASSIGNMENT WITH STRINGS
        # ============================================================

        st.header("4. Assigning a String")

        st.code(
            """name = "Anmol"

        print(name)""",
            language="python"
        )

        st.write("Output:")

        st.code(
            """Anmol""",
            language="text"
        )

        st.write(
            'The string `"Anmol"` was assigned to the variable `name`.'
        )


        # ============================================================
        # 5. ASSIGNMENT WITH NUMBERS
        # ============================================================

        st.header("5. Assigning Numbers")

        st.code(
            """age = 15

        score = 95

        print(age)
        print(score)""",
            language="python"
        )

        st.write("Output:")

        st.code(
            """15
        95""",
            language="text"
        )

        st.write(
            "Numbers can also be assigned to variables."
        )


        # ============================================================
        # 6. CHANGING A VALUE
        # ============================================================

        st.header("6. Changing a Variable's Value")

        st.write(
            "One of the most important things about assignment is that "
            "you can give a variable a new value."
        )

        st.code(
            """age = 15

        age = 16

        print(age)""",
            language="python"
        )

        st.write("Output:")

        st.code(
            """16""",
            language="text"
        )

        st.write(
            "First, `age` was assigned `15`."
        )

        st.write(
            "Then, `age` was assigned a new value: `16`."
        )

        st.info(
            "When a new value is assigned to the same variable, "
            "the variable now refers to the new value."
        )


        # ============================================================
        # 7. ASSIGNMENT HAPPENS FROM RIGHT TO LEFT
        # ============================================================

        st.header("7. Right Side → Left Side")

        st.write(
            "Python evaluates the value on the right side and assigns it "
            "to the variable on the left."
        )

        st.code(
            """score = 100""",
            language="python"
        )

        st.markdown(
            """
            - **Left side:** `score` → the variable
            - **Right side:** `100` → the value
            - **`=`:** assigns the value
            """
        )

        st.code(
            """score = 100""",
            language="python"
        )

        st.write(
            "Think of it as:"
        )

        st.code(
            """score  ←  100""",
            language="text"
        )


        # ============================================================
        # 8. ASSIGNMENT USING ANOTHER VARIABLE
        # ============================================================

        st.header("8. Assigning One Variable to Another")

        st.write(
            "You can assign the value of one variable to another variable."
        )

        st.code(
            """age = 15

        my_age = age

        print(my_age)""",
            language="python"
        )

        st.write("Output:")

        st.code(
            """15""",
            language="text"
        )

        st.write(
            "Here, Python takes the value currently stored in `age` "
            "and assigns it to `my_age`."
        )


        # ============================================================
        # 9. VARIABLES CAN HAVE NEW VALUES
        # ============================================================

        st.header("9. Reassigning Values")

        st.write(
            "Reassignment means assigning a new value to a variable "
            "that already has a value."
        )

        st.code(
            """name = "Alex"

        name = "John"

        name = "Sam"

        print(name)""",
            language="python"
        )

        st.write("Output:")

        st.code(
            """Sam""",
            language="text"
        )

        st.write(
            "The final assignment determines the value currently stored "
            "in `name`."
        )


        # ============================================================
        # 10. ASSIGNMENT AND CALCULATIONS
        # ============================================================

        st.header("10. Assigning a Calculation")

        st.write(
            "You can assign the result of a calculation to a variable."
        )

        st.code(
            """total = 10 + 5

        print(total)""",
            language="python"
        )

        st.write("Output:")

        st.code(
            """15""",
            language="text"
        )

        st.write(
            "Python first calculates `10 + 5` and then assigns the result "
            "`15` to `total`."
        )

        st.info(
            "You learned mathematical operators in Lesson 8. "
            "Here we are using them with assignment."
        )


        # ============================================================
        # 11. ANOTHER CALCULATION EXAMPLE
        # ============================================================

        st.header("11. More Assignment Examples")

        st.code(
            """total = 20 * 5

        difference = 100 - 30

        average = 20 / 4""",
            language="python"
        )

        st.write(
            "Each calculation produces a value, and that value is assigned "
            "to the variable."
        )


        # ============================================================
        # 12. MULTIPLE VARIABLES
        # ============================================================

        st.header("12. Assigning Values to Multiple Variables")

        st.write(
            "You can create multiple variables by using separate assignment statements."
        )

        st.code(
            """name = "Anmol"
        age = 15
        score = 90""",
            language="python"
        )

        st.write(
            "Now there are three variables:"
        )

        st.table({
            "Variable": ["name", "age", "score"],
            "Value": ['"Anmol"', "15", "90"]
        })


        # ============================================================
        # 13. ASSIGNMENT IS NOT EQUALITY
        # ============================================================

        st.header("13. Assignment Is Not the Same as Equality")

        st.write(
            "This is very important for beginners."
        )

        st.code(
            """age = 15""",
            language="python"
        )

        st.write(
            "Here, `=` means assignment."
        )

        st.markdown(
            """
            **It means:**

            > Give the value `15` to the variable `age`.
            """
        )

        st.info(
            "The `==` operator is used for comparison and will be taught "
            "in a later lesson. For now, focus on `=` as assignment."
        )


        # ============================================================
        # 14. COMMON MISTAKES
        # ============================================================

        st.header("14. Common Beginner Mistakes")

        st.subheader("Mistake 1 — Forgetting the `=`")

        st.code(
            """age 15""",
            language="python"
        )

        st.error(
            "This is not a correct assignment statement."
        )

        st.write("Correct:")

        st.code(
            """age = 15""",
            language="python"
        )


        st.subheader("Mistake 2 — Putting the variable on the wrong side")

        st.code(
            """15 = age""",
            language="python"
        )

        st.error(
            "This is not how normal assignment works in Python."
        )

        st.write("Correct:")

        st.code(
            """age = 15""",
            language="python"
        )


        st.subheader("Mistake 3 — Accidentally using text as a variable")

        st.code(
            """ "age" = 15 """,
            language="python"
        )

        st.error(
            "Strings cannot be used as normal variable names for assignment."
        )

        st.write("Correct:")

        st.code(
            """age = 15""",
            language="python"
        )


        # ============================================================
        # 15. PREDICT THE OUTPUT
        # ============================================================

        st.header("15. Predict the Output 🧠")

        st.write(
            "Try to predict what Python will print before looking at the answer."
        )

        st.code(
            """score = 50
        score = 80

        print(score)""",
            language="python"
        )

        show_answer_1 = st.button("Show Answer", key="answer1")

        if show_answer_1:
            st.success("Answer: 80")


        st.divider()

        st.code(
            """name = "Alex"
        name = "Sam"

        print(name)""",
            language="python"
        )

        show_answer_2 = st.button("Show Answer", key="answer2")

        if show_answer_2:
            st.success("Answer: Sam")


        # ============================================================
        # 16. PRACTICE
        # ============================================================

        st.header("16. Practice")

        st.write(
            "Try these exercises in your own Python file."
        )

        st.markdown(
            """
            ### Practice 1
            Create a variable called `name` and assign your name to it.

            ### Practice 2
            Create a variable called `age` and assign your age to it.

            ### Practice 3
            Create a variable called `score` and assign `100` to it.

            ### Practice 4
            Create a variable called `city` and assign a city to it.

            ### Practice 5
            Create a variable called `number`, give it the value `10`,
            then change it to `20`.

            ### Practice 6
            Create a variable called `total` and assign the result of:

            `50 + 25`
            """
        )


        # ============================================================
        # 17. MINI CHALLENGE
        # ============================================================

        st.header("17. Mini Challenge 🏆")

        st.write(
            "Create a small Python program that stores information about a player."
        )

        st.write(
            "Your program should have these variables:"
        )

        st.code(
            """player_name
        player_age
        player_score""",
            language="python"
        )

        st.write(
            "Give each variable a suitable value and then print all three."
        )

        challenge = st.text_area(
            "Write your solution here:",
            height=180
        )

        if st.button("Show Challenge Solution"):
            st.code(
                """player_name = "Alex"
        player_age = 15
        player_score = 100

        print(player_name)
        print(player_age)
        print(player_score)""",
                language="python"
            )

            st.success("Try changing the values and running the program yourself!")


        # ============================================================
        # 18. INTERACTIVE ASSIGNMENT PRACTICE
        # ============================================================

        st.header("18. Interactive Assignment Practice")

        st.write(
            "Choose a variable name and give it a value."
        )

        variable_name = st.text_input(
            "Variable name",
            value="score"
        )

        variable_value = st.text_input(
            "Value",
            value="100"
        )

        if st.button("Create Assignment"):
            st.code(
                f'{variable_name} = "{variable_value}"',
                language="python"
            )

            st.success(
                f"The assignment statement gives the value to `{variable_name}`."
            )


        # ============================================================
        # 19. QUICK QUIZ
        # ============================================================

        st.header("19. Quick Quiz 🎯")

        q1 = st.radio(
            "1. Which symbol is used for assignment?",
            [
                "+",
                "=",
                "*",
                "/"
            ],
            key="q1"
        )

        q2 = st.radio(
            "2. What does this do? `age = 15`",
            [
                "It assigns 15 to age",
                "It compares age and 15",
                "It adds age and 15",
                "It multiplies age by 15"
            ],
            key="q2"
        )

        q3 = st.radio(
            "3. What is the final value of x?",
            [
                "5",
                "10",
                "20",
                "30"
            ],
            key="q3"
        )

        st.code(
            """x = 5
        x = 10
        x = 20""",
            language="python"
        )

        q4 = st.radio(
            "4. Which one is a correct assignment?",
            [
                "20 = score",
                "score 20",
                "score = 20",
                "score == 20"
            ],
            key="q4"
        )

        q5 = st.radio(
            "5. What is reassignment?",
            [
                "Creating a Python file",
                "Giving a variable a new value",
                "Deleting Python",
                "Printing a variable"
            ],
            key="q5"
        )

        q6 = st.radio(
            "6. What is the value of total?",
            [
                "10",
                "15",
                "20",
                "25"
            ],
            key="q6"
        )

        st.code(
            """total = 10 + 5""",
            language="python"
        )

        if st.button("Submit Quiz"):

            score = 0

            if q1 == "=":
                score += 1

            if q2 == "It assigns 15 to age":
                score += 1

            if q3 == "20":
                score += 1

            if q4 == "score = 20":
                score += 1

            if q5 == "Giving a variable a new value":
                score += 1

            if q6 == "15":
                score += 1

            st.success(f"You scored {score}/6!")

            if score == 6:
                st.balloons()
                st.success("Excellent! 🎉 You understand assignment!")

            elif score >= 4:
                st.info("Good job! Review the questions you missed.")

            else:
                st.warning(
                    "Review the lesson and try the quiz again."
                )


        # ============================================================
        # 20. WHAT YOU LEARNED
        # ============================================================

        st.header("📚 What You Learned")

        st.markdown(
            """
            By completing this lesson, you learned:

            - What assignment means in Python
            - How the `=` symbol works
            - How to assign values to variables
            - How to assign strings and numbers
            - How to change a variable's value
            - What reassignment means
            - How to assign one variable to another
            - How to assign the result of a calculation
            - How to use multiple variables
            - The difference between assignment and equality
            """
        )

        st.success(
            "You now understand how Python gives values to variables!"
        )


        # ============================================================
        # 21. NEXT LESSON
        # ============================================================

        st.header("➡️ Next Lesson")

        st.write("**Lesson 10 — input()**")

        st.write(
            "In the next lesson, you will learn how to make your Python "
            "program receive information from the person using it."
        )
    elif st.session_state.current_topic == "10. input()":


        st.title("🐍 Lesson 10 — input()")

        st.write(
            "Until now, our Python programs have used values that we wrote "
            "inside the code. In this lesson, you will learn how to make "
            "your program ask the user for information."
        )

        st.divider()


        # ============================================================
        # 1. WHAT IS input()?
        # ============================================================

        st.header("1. What Is input()?")

        st.write(
            "`input()` is a Python function that allows a program to "
            "receive information from the user."
        )

        st.code(
            """input()""",
            language="python"
        )

        st.write(
            "When Python reaches `input()`, it waits for the user to "
            "type something."
        )

        st.info(
            "Think of `input()` as Python saying: "
            "\"Tell me something.\""
        )


        # ============================================================
        # 2. A SIMPLE input()
        # ============================================================

        st.header("2. Your First input()")

        st.code(
            """input()""",
            language="python"
        )

        st.write(
            "When you run this program, Python waits for you to type "
            "something and press Enter."
        )

        st.code(
            """Hello""",
            language="text"
        )

        st.write(
            "Python receives the text that you entered."
        )


        # ============================================================
        # 3. input() WITH A MESSAGE
        # ============================================================

        st.header("3. Giving the User a Message")

        st.write(
            "You can put a message inside the parentheses of `input()`."
        )

        st.code(
            """input("What is your name? ")""",
            language="python"
        )

        st.write(
            "The message tells the user what information they should enter."
        )

        st.code(
            """What is your name?""",
            language="text"
        )

        st.info(
            "The text inside `input()` is called the prompt. "
            "It tells the user what to type."
        )


        # ============================================================
        # 4. UNDERSTANDING THE SYNTAX
        # ============================================================

        st.header("4. Understanding the Syntax")

        st.code(
            """input("What is your name? ")""",
            language="python"
        )

        st.markdown(
            """
            Let's break it down:

            - `input` → the name of the Python function
            - `()` → tells Python to run the function
            - `"What is your name? "` → the message shown to the user
            """
        )


        # ============================================================
        # 5. STORING INPUT IN A VARIABLE
        # ============================================================

        st.header("5. Storing User Input")

        st.write(
            "Usually, we want to keep the information that the user enters."
        )

        st.code(
            """name = input("What is your name? ")""",
            language="python"
        )

        st.write(
            "Here, the information entered by the user is assigned to "
            "the variable `name`."
        )

        st.markdown(
            """
            Think about what happens:

            **Step 1:** Python asks a question.

            **Step 2:** The user types an answer.

            **Step 3:** Python receives the answer.

            **Step 4:** The answer is assigned to `name`.
            """
        )


        # ============================================================
        # 6. USING THE INPUT
        # ============================================================

        st.header("6. Using the Information")

        st.write(
            "After storing the input in a variable, you can use that "
            "variable later in your program."
        )

        st.code(
            """name = input("What is your name? ")

        print(name)""",
            language="python"
        )

        st.write("For example, if the user types:")

        st.code(
            """Alex""",
            language="text"
        )

        st.write("The program prints:")

        st.code(
            """Alex""",
            language="text"
        )


        # ============================================================
        # 7. input() AND print()
        # ============================================================

        st.header("7. input() and print() Together")

        st.write(
            "`input()` and `print()` can work together."
        )

        st.code(
            """name = input("Enter your name: ")

        print(name)""",
            language="python"
        )

        st.write(
            "`input()` gets the information."
        )

        st.write(
            "`print()` displays information."
        )

        st.table({
            "Function": ["input()", "print()"],
            "Purpose": [
                "Gets information from the user",
                "Displays information"
            ]
        })


        # ============================================================
        # 8. ASKING DIFFERENT QUESTIONS
        # ============================================================

        st.header("8. Asking Different Questions")

        st.write(
            "You can use `input()` to ask the user many different things."
        )

        st.code(
            """name = input("Enter your name: ")

        city = input("Enter your city: ")

        game = input("What is your favorite game? ")""",
            language="python"
        )

        st.write(
            "Each answer can be stored in a different variable."
        )

        st.table({
            "Question": [
                "Enter your name",
                "Enter your city",
                "Favorite game"
            ],
            "Variable": [
                "name",
                "city",
                "game"
            ]
        })


        # ============================================================
        # 9. MULTIPLE INPUTS
        # ============================================================

        st.header("9. Using input() More Than Once")

        st.code(
            """name = input("Enter your name: ")
        city = input("Enter your city: ")

        print(name)
        print(city)""",
            language="python"
        )

        st.write(
            "Python asks the first question, waits for the answer, "
            "then asks the second question."
        )

        st.info(
            "Python normally runs these statements from top to bottom, "
            "so the questions appear one after another."
        )


        # ============================================================
        # 10. INPUT IS TEXT
        # ============================================================

        st.header("10. Important: input() Gives You Text")

        st.write(
            "This is one of the most important things to understand about `input()`."
        )

        st.code(
            """age = input("Enter your age: ")""",
            language="python"
        )

        st.write(
            "Even if the user types:"
        )

        st.code(
            """15""",
            language="text"
        )

        st.write(
            "`input()` receives it as text."
        )

        st.info(
            "For now, remember: `input()` gives you a string (text)."
        )

        st.write(
            "Converting input into numbers will be taught separately later. "
            "We will not use type conversion in this lesson."
        )


        # ============================================================
        # 11. TEXT INPUT
        # ============================================================

        st.header("11. Getting Text From the User")

        st.code(
            """name = input("Enter your name: ")

        print(name)""",
            language="python"
        )

        st.write(
            "This is perfect for information such as:"
        )

        st.markdown(
            """
            - Names
            - Cities
            - Favorite games
            - Favorite foods
            - Countries
            - Hobbies
            """
        )


        # ============================================================
        # 12. INPUT WITH VARIABLES
        # ============================================================

        st.header("12. input() and Variables")

        st.write(
            "You already learned variables in Lesson 6."
        )

        st.code(
            """name = input("Enter your name: ")""",
            language="python"
        )

        st.write(
            "The variable `name` gets its value from the user instead "
            "of getting a value directly from the code."
        )

    elif st.session_state.current_topic == "11. if statement":
        render_course_lesson(11, LESSONS_11_TO_33[11])
    elif st.session_state.current_topic == "12. Comparison Operators":
        render_course_lesson(12, LESSONS_11_TO_33[12])
    elif st.session_state.current_topic == "13. else":
        render_course_lesson(13, LESSONS_11_TO_33[13])
    elif st.session_state.current_topic == "14. elif":
        render_course_lesson(14, LESSONS_11_TO_33[14])
    elif st.session_state.current_topic == "15. Combining Conditions":
        render_course_lesson(15, LESSONS_11_TO_33[15])
    elif st.session_state.current_topic == "16. while Loop":
        render_course_lesson(16, LESSONS_11_TO_33[16])
    elif st.session_state.current_topic == "17. for Loop":
        render_course_lesson(17, LESSONS_11_TO_33[17])
    elif st.session_state.current_topic == "18. break":
        render_course_lesson(18, LESSONS_11_TO_33[18])
    elif st.session_state.current_topic == "19. continue":
        render_course_lesson(19, LESSONS_11_TO_33[19])
    elif st.session_state.current_topic == "20. Understanding Strings":
        render_course_lesson(20, LESSONS_11_TO_33[20])
    elif st.session_state.current_topic == "21. String Slicing":
        render_course_lesson(21, LESSONS_11_TO_33[21])
    elif st.session_state.current_topic == "22. Basic String Methods":
        render_course_lesson(22, LESSONS_11_TO_33[22])
    elif st.session_state.current_topic == "23. f-Strings":
        render_course_lesson(23, LESSONS_11_TO_33[23])
    elif st.session_state.current_topic == "24. What Is a List?":
        render_course_lesson(24, LESSONS_11_TO_33[24])
    elif st.session_state.current_topic == "25. Basic List Methods":
        render_course_lesson(25, LESSONS_11_TO_33[25])
    elif st.session_state.current_topic == "26. Looping Through Lists":
        render_course_lesson(26, LESSONS_11_TO_33[26])
    elif st.session_state.current_topic == "27. Why Functions?":
        render_course_lesson(27, LESSONS_11_TO_33[27])
    elif st.session_state.current_topic == "28. Creating and Calling Functions":
        render_course_lesson(28, LESSONS_11_TO_33[28])
    elif st.session_state.current_topic == "29. Parameters":
        render_course_lesson(29, LESSONS_11_TO_33[29])
    elif st.session_state.current_topic == "30. What Is a Dictionary?":
        render_course_lesson(30, LESSONS_11_TO_33[30])
    elif st.session_state.current_topic == "31. Understanding Errors":
        render_course_lesson(31, LESSONS_11_TO_33[31])
    elif st.session_state.current_topic == "32. try / except":
        render_course_lesson(32, LESSONS_11_TO_33[32])
    elif st.session_state.current_topic == "33. Exception Patterns":
        render_course_lesson(33, LESSONS_11_TO_33[33])
    elif st.session_state.current_topic == '🟢 Project 1 — Calculator':
        render_project('🟢 Project 1 — Calculator', PROJECTS['🟢 Project 1 — Calculator'])
    elif st.session_state.current_topic == '🟢 Project 2 — Number Guessing Game':
        render_project('🟢 Project 2 — Number Guessing Game', PROJECTS['🟢 Project 2 — Number Guessing Game'])
    elif st.session_state.current_topic == '🟢 Project 3 — Rock Paper Scissors':
        render_project('🟢 Project 3 — Rock Paper Scissors', PROJECTS['🟢 Project 3 — Rock Paper Scissors'])
    elif st.session_state.current_topic == '🟢 Project 4 — Quiz Game':
        render_project('🟢 Project 4 — Quiz Game', PROJECTS['🟢 Project 4 — Quiz Game'])
    elif st.session_state.current_topic == '🟢 Project 5 — To-Do List':
        render_project('🟢 Project 5 — To-Do List', PROJECTS['🟢 Project 5 — To-Do List'])
