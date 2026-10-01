FocusTimer: Build SpecProblem. Students lose track of how much focused time they actually put in. FocusTimer is a small terminal (command-line) program that times named focus sessions and shows a daily summary.
Users. One student, running it in a terminal on their own machine or Codespace. No accounts.
How it runs (the menu). When the program starts, it prints a numbered menu and waits for a choice:
1. Start a focus session
2. Show today's summary
3. Quit
After each action it shows the menu again, until the user chooses Quit.
Behavior: Start a focus session.
Ask the user for a session name (for example, "Math homework").
Begin timing. Tell the user to press Enter when they're done.
When they press Enter, stop timing.
Compute the length in minutes = elapsed seconds ÷ 60, rounded to 1 decimal place.
Save the session (see Data), then return to the menu.
Behavior: Show today's summary.
Look at every saved session whose date is today.
For each distinct session name, print one line: <name>: <total minutes> min (add up every session with that name today).
After the per-name lines, print one final line: Total: <grand total> min.
If there are no sessions today, print exactly: No focus sessions logged today.
Data / storage.
Sessions live in a JSON file named focus_log.json, in the same folder as the program.
The file holds a JSON list of session objects. Each object has exactly these fields:
{"name": "Math homework", "date": "2026-09-14", "minutes": 27.5}
date is the calendar date the session was recorded, formatted YYYY-MM-DD.
On start, load focus_log.json. If the file does not exist, start with an empty list and do not crash.
After each new session, save the updated list back to focus_log.json.
Out of scope (do NOT build).
No accounts, passwords, or multiple users.
No editing or deleting past sessions.
No graphs, colors, or web interface: plain terminal text only.
No database: the JSON file is the only storage.
Acceptance criteria. Your build is done when ALL of these are true:
Running the program shows the numbered menu (Start / Summary / Quit) and returns to it after each action until Quit.
Starting a session asks for a name, times it until the user presses Enter, and records name + today's date + minutes (rounded to 1 decimal).
Sessions are written to focus_log.json and are still there after you quit and restart.
"Show today's summary" prints one <name>: <minutes> min line per distinct name for today, then a Total: <minutes> min line.
With no sessions recorded today, the summary prints exactly: No focus sessions logged today.
If focus_log.json does not exist yet, the program starts with an empty log and does not crash.
