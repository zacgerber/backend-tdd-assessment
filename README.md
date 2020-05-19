# TDD - Test Driven Development

For this assessment, We'll be using the concept of Test Driven Development (TDD) to created a modified version of the `echo` command line tool.  This tool is built into every shell, and functions very much like `print()` does in Python.  For this assessment we'll be creating our own version of `echo` which accepts a few additional parameters on the command line.

![example output](screenshots/result.gif)

In doing so, you'll be demonstrating a basic understanding of the following:

- Converting acceptance criteria into unit tests using
  [unittest](https://docs.python.org/3/library/unittest.html)
- Employing [Test Driven Development (TDD)](https://medium.freecodecamp.org/learning-to-test-with-python-997ace2d8abe) to write a program that conforms to those criteria
- Parsing command line argumens with [argparse](https://docs.python.org/3/howto/argparse.html#id1)
- Commonly used [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## Getting Started
TDD *starts* with setting up a test harness, and writing the tests FIRST, before writing application code.  A test harness (or fixture) is a completely separate module designed to test your application code.  One analogy to think of is how rocket or jet engines are tested: A new engine is mounted into a _test fixture_, which supplies inputs like fuel and control signals.  It measures the performance of the engine in a safe environment, before the engine gets deployed into the real world.

<img height="120px" src="https://www.nasa.gov/sites/default/files/thumbnails/image/0302460.jpg" />

Think of the test cases that you will need for the `echo` application that you will build. You will need to check each command line option, in various forms, to make sure they are working.  You'll also need to test them together, to make sure order of precedence is kept (e.g. should TitleCase be applied before or after Lowercase if they are both present?) 

For a small project like this, it's sufficient to have a single test module named `test_echo.py`.  In the beginning, all tests should fail (of course, because you haven't written anything!)  However, you are proving out the basic execution paths and setup of your program.

**Keep in Mind:**
 - When writing a test, write the _assertion_ statement first, and work backwards.
 - Before writing the application code, run the test to make sure it fails in the way you think it should.
 - Write meaningful, short tests that are self-explanatory.  Keep the "Reader" of your code in mind.  It may not be you.  Is your intention clear?
 - Always keep test code separate from application code.
 - Each test should run indepedently.  No cross-dependencies between tests.
 - Make frequent, small commits after each test is passing.


Pay special attention to the name of the test module: `test_echo.py`.  When writing test modules, start each module filename with the prefix `test*`.  Many testing frameworks are set up to *auto-discover* test modules that adhere to this naming convention.  Auto-discovery is important-- in a Continuous Integration (CI) environment, your tests will be discovered and run when you attempt to push changes to the repository.

The two files you will be editing are `test_echo.py` and `echo.py`. Don't worry about the files inside the soln directory, those are encrypted and used only by your instructor team. When done, you should have a project directory that looks something like this:

```
.
├── README.md
├── USAGE
├── echo.py
├── screenshots
│   └── result.gif
├── soln
│   ├── .gitattributes
│   ├── echo.py
│   └── test_echo.py
└── tests
    ├── __init__.py
    └── test_echo.py
```

## Running Tests from command line
Even before you write a single test, you might find it useful to try out your test harness.  Note the use of the `rerun` helper utility.  You can PIP-install this useful tool that watches directory for file changes, and re-runs the command each time it detects a saved edit.  

```bash
$ pip install rerun
$ rerun "python -m unittest discover"
```

## Running Tests from VSCode
If you don't want your tests manually from the command line, VSCode has a nifty plugin feature that runs your tests directly from your code window.  Access this feature through the Test Tube icon on the left ribbon bar.  This VSCode plugin also supports [built-in unit test discovery](https://code.visualstudio.com/docs/python/unit-testing), but you must manually enable it.

<img height="200px" src="screenshots/VSCodeTest.png" />

## Acceptance Criteria

### Step 1: Test the Help/Usage
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

The following unit test can be used to check that your program prints a properly formatted help message.  It does this by launching a completely separate python process, and running your echo.py in that process, and saving the output for comparison:

```python
def test_help(self):
    """ Running the program without arguments should show usage. """

    # Run the command `python ./echo.py -h` in a separate process, then
    # collect it's output.
    process = subprocess.Popen(
        ["python", "./echo.py", "-h"],
        stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    with open("USAGE") as f:
        usage = f.read()

    self.assertEqual(stdout, usage)
```

However, the `test_echo.py` file also contains a class helper that will allow you to capture the printed output of echo.py without needing to launch a new process.  So you could also try this test instead

```python
def test_help(self):
        """ Check that usage is printed when -h option is given"""
        args = ["-h"]
        with open("USAGE") as f:
            usage = f.read().splitlines()
        with Capturing() as output:
            self.module.main(args)
        self.assertEqual(output, usage)
```

### Step 2: Test the `-u/--upper option`
Write a unit test that asserts that `upper` get stored inside of the
namespace returned from `parser.parse_args` when either `"-u"` or `"--upper"`
arguments are passed.

It should also test that `"hello"` gets turned into `"HELLO"` when the
program is run.

### Step 3: Test the `-l/--lower option`
Write a unit test that asserts that `lower` get stored inside of the
namespace returned from `parser.parse_args` when either `"-l"` or `"--lower"`
arguments are passed.

It should also test that `"Hello"` gets turned into `"hello"` when the
program is run.

### Step 4: Test the `-t/--title option`
Write a unit test that asserts that `title` get stored inside of the
namespace returned from `parser.parse_args` when either `"-t"` or `"--title"`
arguments are passed.

It should also test that `"hello"` gets turned into `"Hello"` when the
program is run.

### Step 6: Test for when all option flags are provided
When a user provides all three option flags (-lut), they should be **applied in the order listed in the helpful usage message** that Argparse constructs from the argument definitions. Here are a few examples:

```console
$ python echo.py -tul "heLLo!"
Hello!
```

```console
$ python echo.py -ul "heLLo!"
hello!
```

Note that the order that the options are provided doesn't matter, e.g. '-tul' and '-utl' and '-lut' are **all equivalent inputs to Argparse**.  Only the final text transform result should be printed.

### Step 7: Test for no options flags
Write a unit test that asserts that when no options flags are given, the program
prints the unaltered input text.

### Step 8: Implement echo.py
This step can be done in several ways.  
- You can try to implement ALL the test cases in advance and then code the application to pass all the tests.  You'll probably forget some along the way and come back later to add them.
- A better approach might be to write a small failing test, then write some application code to make it pass.  Then write another failing test, and write more app code to make it pass.  You get the idea, to alternate between test dev and app dev as you code.

## Structuring your echo.py application
Remember to separate functionality in your echo.py application.  Notice that many of the tests above are checking to see if the argument parser has done its job correctly by parsing out an option from the command line, and making it available in parser output (the Namespace, or parsed args dict).  
Therefore, it makes sense to have a function in echo.py whose sole purpose is to deliver back a parser object, that can be stored in your TestEcho class and invoked by calling its parse_args() method with various argument lists.  Such a function might be named `create_parser()`.
You may also benefit from having a separate `main()` function in your echo.py appliction.  A main() function can be invoked from the command line directly as part of the application, but it can also be _directly imported_ by your test program so you can test it all different ways.  The starter code for these two functions is provided in echo.py.

## Submitting Your Work
Use the `PR Workflow` process to submit your work.  This process is detailed in your course materials.


## PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account.
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
5. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.

