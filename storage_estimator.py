# storage_estimator.py
# Estimates total storage needed for a number of files.

def main():
    print("Storage Estimator")

    num_files = int(input("How many files? "))
    avg_size_kb = float(input("Average file size in KB? "))

    total_kb = num_files * avg_size_kb
    total_mb = total_kb / 1024

    print("Total KB:", total_kb)
    print("Total MB:", total_mb)


main()
