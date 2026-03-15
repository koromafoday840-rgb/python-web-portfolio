# Phonebook Manager

This is a simple, menu-driven phonebook app I built to get more comfortable with Python. It’s designed to run directly in your terminal, keeping things clean and straightforward.

## How it works
At its heart, the program uses a Python dictionary to keep your contacts organized. When you run it, it drops you into a loop that stays open until you're ready to leave.

### What it can do:
* **Add or Update:** Toss a name and number in, and it'll store it. If the name exists, it just updates it.
* **Delete:** Remove anyone you don't need anymore.
* **Search:** Quickly find a number if you know the name.
* **View All:** See every contact you've saved so far.

## The Logic (How the code moves)
I built this with a `while True` loop so the menu keeps popping up after you finish a task. 

1. **Initialization:** It starts by setting up an empty dictionary.
2. **The Loop:** It waits for your input.
3. **The Decisions:** Using `if/elif/else` statements, it figures out if you want to add, remove, or view data.
4. **Shutdown:** When you hit '5', it kills the loop and exits.

## Getting started
Just open your terminal, navigate to the project folder, and run:

```bash
python3 manager.py