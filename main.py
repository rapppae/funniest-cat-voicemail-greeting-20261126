"""Entry for make.fun bounty "Funniest Cat Voicemail Greeting".
Entry text (v1): Meow. You've reached the cat. I'm busy knocking things off tables. Leave a message I'll ignore, human.
Limit: 120 characters. No trailing newline is written.
"""
import os
ENTRY = "Meow. You've reached the cat. I'm busy knocking things off tables. Leave a message I'll ignore, human."
def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
if __name__ == "__main__":
    main()
