# TDD - Creating a command line tool

For this assessment, We'll be using the concept of Test-Driven Development (TDD) to created a modified version of the `echo` command line tool:

![example output](screenshots/result.gif)

In doing so, you'll be demonstrating a basic understanding of the following:

- Converting acceptance criteria into unit tests using
  [unittest](https://docs.python.org/3/library/unittest.html)
- Employing [Test-Driven Development (TDD)](https://medium.freecodecamp.org/learning-to-test-with-python-997ace2d8abe) to write a program that conforms to those criteria
- Parsing command line arguments with [argparse](https://docs.python.org/3/howto/argparse.html)
- Commonly-used [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## Getting Started
TDD *starts* with setting up a test harness, and writing the tests **first**, before writing application code. Think of the test cases that you will need for the `echo` application that you will build. For a small project like this, it's sufficient to have a single test case named `test_echo.py`. In the beginning, all tests should fail (of course, because you haven't written anything!) However, you are proving out the basic execution paths and setup of your program.
Pay special attention to the name of the test module: `test_echo.py`. When writing test modules, start each module filename with the prefix `test*`. Many testing frameworks are set up to *auto discover* test modules that adhere to this naming convention. Auto discovery is important &mdash; in a continuous integration environment, your tests will be discovered and run when you attempt to push changes to the repo. Some CI/CD pipelines will not allow you to push changes to the repo if they cannot auto discover and run your tests.

The last step involves your application code, which will reside in the `echo.py` file. When done, you should have a project directory that looks something like this:

```
.
├── CODEOWNERS
├── README.md
├── USAGE
├── echo.py
├── screenshots
│   └── result.gif
└── tests
    ├── __init__.py
    └── test_echo.py
```

Even before you write a single test, you might find it useful to try out your test harness. Note the use of the `rerun` helper utility. You can `pip install` this useful tool that watches a directory for file changes, and re-runs the command each time it detects a newly-saved file. The VS Code IDE also has [built-in unit test discovery](https://code.visualstudio.com/docs/python/testing), but you must manually enable it.

```console
% pip install rerun
% rerun "python -m unittest discover"
```

## Acceptance Criteria

### Step 1: Display Help
When the user provides invalid options or supplies the `-h/--help` flag, the
program should print the following usage message:

    usage: echo.py [-h] [-u] [-l] [-t] text

    Perform transformation on input text.

    positional arguments:
        text         text to be manipulated

    optional arguments:
        -h, --help   show this help message and exit
        -u, --upper  convert text to uppercase
        -l, --lower  convert text to lowercase
        -t, --title  convert text to titlecase

The following unit test can be used to check that your program prints a properly formatted help message:

```python
def test_help(self):
    """Running the program without arguments should show usage."""

    # Run the command `python ./echo.py -h` in a separate process, then
    # collect its output.
    process = subprocess.Popen(
        ["python", "./echo.py", "-h"],
        stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    with open("USAGE") as f:
        usage = f.read()

    self.assertEquals(stdout, usage)
```

### Step 2: Test the `-u/--upper option`
Write a unit test that asserts that `upper` gets stored inside of the
namespace returned from `parser.parse_args()` when either `"-u"` or
`"--upper"` arguments are given on the command line.

It should also test that `"hello"` gets turned into `"HELLO"` when the
program is run.

### Step 3: Test the `-l/--lower option`
Write a unit test that asserts that `lower` gets stored inside of the
namespace returned from `parser.parse_args()` when either `"-l"` or
`"--lower"` arguments are given on the command line.

It should also test that `"Hello"` gets turned into `"hello"` when the
program is run.

### Step 4: Test the `-t/--title option`
Write a unit test that asserts that `title` gets stored inside of the
namespace returned from `parser.parse_args()` when either `"-t"` or
`"--title"` arguments are given on the command line.

It should also test that `"hello"` gets turned into `"Hello"` when the
program is run.

### Step 6: Test for when all options are provided
When a user provides all three options, they should be applied in the order
listed in the helpful usage message that argparse constructs from the
argument definitions. Here are a few examples:

```console
% python echo.py -tul "heLLo!"
Hello!
```

```console
% python echo.py -ul "heLLo!"
hello!
```

Note that the order the options are provided doesn't matter, e.g. '-tul' and '-utl' and '-lut' are all equivalent inputs to argparse. Only the final text transformation result should be printed.

### Step 7: Test for no arguments
Write a unit test that asserts that, when no arguments are given, the program
returns the unaltered input text.

### Step 8: Implement the program
Now that your tests are complete, implement the program so that the above
tests pass.

## Structuring your code
Remember to separate functionality in your `echo.py` application. Notice that many of the tests above are checking to see if the argument parser has done its job correctly by parsing out an option from the command line and making it available in the parser output (the Namespace, or parsed args dict).
Therefore, it makes sense to have a function in `echo.py` whose sole purpose is to deliver back a parser object that can be stored in your TestEcho class and invoked by calling its `parse_args()` method with various argument lists. Such a function might be named `create_parser()`.
You may also benefit from having a separate `main()` function in your echo.py application. A `main()` function can be invoked from the command line directly, as well as imported by your test program and tested independently.


## PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account.
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
5. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.
