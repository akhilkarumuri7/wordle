# Wordle (Python + Tkinter)

A desktop **Wordle** clone built in Python with a simple Tkinter UI.

## Features
- 5-letter Wordle gameplay with up to 6 attempts
- Letter feedback (correct letter / correct position)
- Random daily-style selection from a curated list (~1,300 words)

## Run Locally (Python 3.10+)
> Tkinter usually ships with Python on macOS. On Linux, install `python3-tk`.

```bash
# (optional) create a venv
python3 -m venv .venv && source .venv/bin/activate

# run
python wordle/main.py
