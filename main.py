"""Entry for make.fun bounty "Funniest Cat Voicemail Greeting".
Entry text (revised v2): Hi, it's the cat. I'm busy knocking your glass off the table, so leave a message I'll pretend to listen to later.
Limit: 120 characters. No trailing newline is written.
"""
import os
ENTRY = "Hi, it's the cat. I'm busy knocking your glass off the table, so leave a message I'll pretend to listen to later."
def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
if __name__ == "__main__":
    main()
