import os

ENTRY = "One star: the locals stare at glowing rectangles all day and call it 'connection' — but the noodles alone are worth the 40-light-year trip."


ENTRY_FILENAME = "entry.txt"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
