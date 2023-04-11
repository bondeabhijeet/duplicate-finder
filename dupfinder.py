import hashlib
import os

def get_hash(filename):                             # Define a function to compute the hash of a file
  hash = hashlib.md5()                              # Create a hash object
  
  with open(filename, "rb") as f:                   # Open the file in binary mode
    
    for chunk in iter(lambda: f.read(4096), b""):   # Read and update hash in chunks of 4KB
      hash.update(chunk)
  
  return hash.hexdigest()                           # Return the hex digest of the hash


def ScanAll(path):                            # Define a function to find duplicate files in a given path
  file_list = {}                                     # Create an empty dictionary
  
  for dirpath, dirnames, filenames in os.walk(path):  # Walk through all files in the path

    for filename in filenames:  
      full_path = os.path.join(dirpath, filename)     # Get the full path of the file
      file_hash = get_hash(full_path)                 # Get the file hash

      if file_hash not in file_list:                 # Add or append the file path to the dictionary
        file_list[file_hash] = [full_path]
      else:
        file_list[file_hash].append(full_path)

  return file_list 