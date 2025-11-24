import os
import glob

OUTPUT_PATHS = [
    "../outputs/raw_json/*.json",
    "../outputs/csv/*.csv",
    "../outputs/analytics/charts/*.png",
    "../outputs/validation_report.json"
]

def cleanup():
    print("\n===============================")
    print("   Cleaning Output Folders")
    print("===============================\n")

    total_deleted = 0

    for path in OUTPUT_PATHS:
        files = glob.glob(path)
        for file in files:
            try:
                os.remove(file)
                total_deleted += 1
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Could not delete {file}: {e}")

    print("\n===============================")
    print(f" Cleanup complete. {total_deleted} files removed.")
    print("===============================\n")


if __name__ == "__main__":
    cleanup()
