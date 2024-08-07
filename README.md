[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7gMNT4kz)
# Programming Assignment: Exam Grader

## Objective

This assignment will test your ability to use loops, conditionals, and basic string operations to implement a simple exam grading system.

## Problem Statement

You are tasked with writing a program that grades a multiple-choice exam. Each question has four possible choices: a, b, c, or d. The program will compare the user's answers to a set of correct answers and calculate the user's score. The possible correct answers are given on the `assignment.py` file

### Tasks

1. **Input Validation**:

   - Prompt the user to enter their exam answers. Ensure that the number of answers matches the number of questions. If not, display an error message and prompt again.

2. **Check Exam**:

   - Compare each answer from the user to the corresponding correct answer. Keep track of the number of correct answers and build a string showing correct answers and 'X' for incorrect ones.

3. **Grade Exam**:
   - Calculate the user's score as a percentage and display it. Provide feedback if the user scores 100%.

## Instructions

1. Update the `assignment.py` file and place intro comments using the template below.
2. Use comments to write the code your program will follow.
3. Test your completed code using your test cases.

## Intro Comments Template

```python
# Programmer: [your name]
# Course: CS701/GB-731, Dr. Yalew
# Date: [Submission date]
# Programming Assignment: 3
# Program Inputs: A string containing answer
# Program Outputs: Very good(If 100% correct) or Missed number and Score Presentage
```

## Submission

- Clone the project
- Follow the instructions on the README.md file and the comment on code
  - Complete the code
  - You can look into the `test_assignment.py` for inspiratin too
- **Test the program**: by running `pytest`
  - If the test passes
    - Push the project to the repository
      - If this is hard
      - Submit the assignment.py on moodle
