# NewWorld Automation Brief CLI

A simple command-line tool for NewWorld AI Solutions that turns a messy,
repetitive business process into a structured automation brief — no AI or
API involved, just plain Python practising CS50P fundamentals (functions,
variables, input/output).

## What it does

The program asks four questions about a repetitive workflow:

1. Business or client
2. Repetitive task
3. Workflow trigger
4. Desired outcome

It then prints a labelled brief with all four answers, plus a simple
automation hypothesis sentence describing when and how the task could be
automated.

## Automation potential rating

Each brief is automatically classified into one of three categories, based
on keywords found in the workflow trigger:

- **High automation potential** — the trigger involves a person manually
  initiating the task (e.g. contains words like "client", "someone",
  "request", "submit", "approval").
- **Medium automation potential** — the trigger is partially automated
  already, but still needs a person to act (e.g. contains words like
  "logged", "added", "notified").
- **Low automation potential** — the trigger is already automatic or
  scheduled, with none of the above keywords present.

This is a simple, rule-based keyword check — not AI-powered — so it won't
catch every possible phrasing, but it gives a quick first read on which
automation ideas are worth prioritizing.

## How to run it

From inside the newworld-cli folder:

python3 newworld_cli.py

You'll be prompted for each of the four inputs, and the finished brief will
print to the terminal.

## Files

- newworld_cli.py — the program itself
- README.md — this file
- sample-output.txt — a real run of the program