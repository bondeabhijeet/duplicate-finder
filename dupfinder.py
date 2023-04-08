import os         # Import the modules
import sys
import hashlib
import sqlite3
import sqbase as sqdatabase

DB_Name = "dupfiles.db"               # Database name
Table_Name = "duplicate_files"        # Table name


def get_hash(filename):                             # Define a function to compute the hash of a file
  hash = hashlib.md5()                              # Create a hash object
  
  with open(filename, "rb") as f:                   # Open the file in binary mode
    
    for chunk in iter(lambda: f.read(4096), b""):   # Read and update hash in chunks of 4KB
      hash.update(chunk)
  
  return hash.hexdigest()                           # Return the hex digest of the hash


def find_duplicates(path):                            # Define a function to find duplicate files in a given path
  duplicates = {}                                     # Create an empty dictionary
  
  for dirpath, dirnames, filenames in os.walk(path):  # Walk through all files in the path

    for filename in filenames:  
      full_path = os.path.join(dirpath, filename)     # Get the full path of the file
      file_hash = get_hash(full_path)                 # Get the file hash

      if file_hash not in duplicates:                 # Add or append the file path to the dictionary
        duplicates[file_hash] = [full_path]
      else:
        duplicates[file_hash].append(full_path)

  return duplicates                                   # Return the dictionary of duplicates


conn = sqlite3.connect(DB_Name)
cur = conn.cursor()
sqdatabase.DropTable(cur, Table_Name)
sqdatabase.CreateTable(cur, Table_Name)

path = sys.argv[1]                      # Get the path from the command line argument

duplicates = find_duplicates(path)      # Find and print the duplicates
print(duplicates)
sqdatabase.FillDatabase(duplicates, cur, Table_Name)
# for key, value in duplicates.items():
#   if len(value) > 1:
#     print(f"Duplicate files: {', '.join(value)}")

conn.commit()
conn.close()