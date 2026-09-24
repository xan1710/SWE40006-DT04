import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/output"

def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"[{ts}] {msg}", flush=True)

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.lower().split()
    word_count = len(words)
    line_count = text.count("\n") + 1
    top_words = Counter(words).most_common(5)
    return word_count, line_count, top_words

def main():
    log("Container started. Beginning data processing job.")

    if not os.path.isdir(INPUT_DIR):
        log(f"ERROR: input directory {INPUT_DIR} not found.")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".txt")]
    if not files:
        log(f"ERROR: no .txt files found in {INPUT_DIR}.")
        sys.exit(1)

    log(f"Found {len(files)} file(s) to process: {files}")

    report_lines = [f"Data Processing Report — {datetime.now(timezone.utc).isoformat()}", "=" * 50]

    for filename in files:
        filepath = os.path.join(INPUT_DIR, filename)
        log(f"Processing {filename}...")
        time.sleep(1)  # simulate work, makes lifecycle visible in logs
        word_count, line_count, top_words = process_file(filepath)

        report_lines.append(f"\nFile: {filename}")
        report_lines.append(f"  Lines: {line_count}")
        report_lines.append(f"  Words: {word_count}")
        report_lines.append(f"  Top 5 words: {top_words}")

        log(f"Finished {filename} — {line_count} lines, {word_count} words.")

    output_path = os.path.join(OUTPUT_DIR, "report.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    log(f"Report written to {output_path}.")
    log("Job complete. Container exiting with status 0.")
    sys.exit(0)

if __name__ == "__main__":
    main()