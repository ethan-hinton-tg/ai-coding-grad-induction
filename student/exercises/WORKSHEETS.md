# Workshop Worksheets

These prompts are suggestions, not guaranteed instructions. Ask the AI tool to explain or propose before it edits. Keep your own reasoning in charge, inspect every diff, and run tests after changes.

## Exercise 1: Get familiar with the project and make a small change

**Purpose:** Learn your way around the repository, then implement the `missing_required_fields` function.

**Steps**

1. Ask Copilot to explain the repository and trace one example record through the existing functions. Ask it not to edit any files yet.
2. Read the source code and the baseline tests yourself. Find the `missing_required_fields` function and read its docstring.
3. Implement the `missing_required_fields` function. It should tell you which required keys are not present in a record.
4. Ask Copilot to suggest some tests. Choose the tests that make sense, inspect your changes, and run `python -m pytest`.

**Suggested prompts**

- “Please explain the repository structure and trace this example through the code. Do not edit any files yet.”
- “Please suggest how I could implement the `missing_required_fields` function from its docstring and the requirements. Do not edit any files yet.”
- “Review my diff and identify missing cases without changing files.”

**Deliverables:** A working implementation and tests showing that missing names are returned in the required order, a non-dictionary returns all required names, and a present key counts as present even when its value is invalid.

**Debrief:** What evidence did you use to decide whether the AI’s suggestion matched the requirement?

## Exercise 2: Investigate and fix a bug

**Purpose:** Learn how to compare what the code does with what the requirements say it should do.

**Where to work:** Add your experiment and permanent regression test to `student/tests/test_data_quality.py`. Make the implementation fix in `student/src/data_quality.py`. Use the terminal only to run `python -m pytest` from the repository root.

**Steps**

1. Read the `is_valid_amount` rules in the **Requirements** section of `student/README.md` and look at how the function currently works.
2. In `student/tests/test_data_quality.py`, add a focused test for an example that might show a difference between the requirements and the code.
3. In the terminal, run `python -m pytest` from the repository root and confirm that your new test fails.
4. Ask Copilot for possible explanations of the failure. Ask it not to edit any files.
5. In `student/src/data_quality.py`, make the smallest code change you can to fix the behavior. Then run `python -m pytest` again.
6. Review your diff and explain why your change fixes the problem without changing unrelated behavior.

**Suggested prompts**

- “Please compare the amount requirements with the current implementation. What should I investigate? Do not edit any files yet.”
- “Please give me two possible explanations for this failing test and explain how I could check each one. Do not edit any files.”
- “I have added a failing test in `student/tests/test_data_quality.py`. Please suggest the smallest fix for `student/src/data_quality.py`, but do not apply it yet.”

**Deliverables:** A test that shows the problem, a small implementation change that fixes it, and a passing test suite.

**Debrief:** How did your test show what the function should do, rather than just checking how it happened to be written?

## Exercise 3: Ask AI for test ideas

**Purpose:** Use AI to think of more test cases, then decide for yourself which tests are useful and supported by the requirements.

**Steps**

1. Ask Copilot to suggest tests for `is_valid_amount` and `is_valid_record`. Ask it to include values at the boundaries and unusual inputs.
2. Look at cases such as zero, booleans, NaN (not-a-number), infinity, empty strings, whitespace, and unexpected input types.
3. Read each suggested test and decide whether it follows from the written requirements. Add the tests you choose and run them.
4. For each test you add, write down what behavior it checks and what possible mistake it could catch.

**Suggested prompts**

- “Please suggest a list of tests for these functions, including boundary and unusual inputs. Explain which requirement each test checks. Do not edit any files.”
- “Please review these tests for missing cases and for tests that check implementation details instead of behavior. Do not edit.”

**Deliverables:** Useful edge-case tests, plus a short explanation of which suggestions you used, which you did not use, and why.

**Debrief:** Which suggested test was hardest to justify, and what did you use to decide whether to include it?

## Exercise 4: Build a summary by region

**Purpose:** Bring together the skills from the earlier exercises to add a complete feature and test it carefully.

**Steps**

1. Before editing, create a folder outside the workshop project called `exercise-4-backup`. Copy `student/src/data_quality.py` and `student/tests/test_data_quality.py` into it. This gives you a safe copy of your work from the start of the exercise.
2. Read the requirements for `summarize_by_region` and ask Copilot to suggest an approach before editing any files.
3. Implement the function and add tests. Your function should count only valid records, ignore invalid records, remove extra whitespace around region names, add the amounts, and keep regions in the order they first appear.
4. Review your diff, run the full test suite, and explain one suggestion from Copilot that you changed or decided not to use.

**Suggested prompts**

- “Please turn these requirements into a simple implementation plan and test plan. Do not edit any files yet.”
- “Please review my implementation against each requirement and point out a missing test. Do not edit.”

**Deliverables:** A working implementation, tests for each requirement, a reviewed diff, and a passing full test suite.

**Debrief:** Which requirement was easiest to miss, and how did your tests help you notice it?

## Exercise 4b: Try the task with Agent mode

**Purpose:** Compare different prompts and practise reviewing code written by an AI coding agent.

Use the `exercise-4-backup` folder you created at the start of Exercise 4. It contains your earlier source and test files, so you can restore the starting state without losing your own solution.

**Steps**

1. Copy the two files from `exercise-4-backup` back to their original locations under `student/`. This restores the Exercise 4 starting state: `summarize_by_region` should raise `NotImplementedError`, and your Exercise 4 tests will no longer be present.
2. Try asking Copilot to complete the task with each of these prompts:

	- “Implement `summarize_by_region`.”
	- “Implement `summarize_by_region` and add tests.”
	- “Before editing, explain your approach. Then implement `summarize_by_region` in `student/src/data_quality.py` and add tests in `student/tests/test_data_quality.py`. Use only the existing Python standard library. Handle invalid records, whitespace around region names, summed amounts, and first-seen key order.”

3. Compare the responses and choose the prompt that gives the clearest instructions.
4. Use that prompt in Agent mode and allow it to edit the source and test files.
5. Inspect every changed file and review the diff. Check that the changes match the requirements and do not alter unrelated exercises.
6. Run `python -m pytest` from the repository root.
7. Compare the Agent-mode solution with your original solution. Note one change you accepted, modified, or rejected and explain why.

**Deliverables:** A prompt comparison, an Agent-mode implementation, a reviewed diff, a passing test suite, and a short comparison with your original solution.

**Debrief:** What did you need to tell the AI tool explicitly, and what did you still need to check yourself?

## Responsible-use scenario activity

Discuss each item using your organization’s policy. Stop and ask the facilitator when approval is unclear.

- A public Python error message.
- A client dataset containing personal information.
- An API key in a configuration file.
- A code snippet from a public tutorial.
- Proprietary code where the approved-tool policy is unclear.

For each, decide what could be shared, what must be removed or anonymized, and what approved alternative you would use. Never assume that “public” or “small” automatically means permitted.