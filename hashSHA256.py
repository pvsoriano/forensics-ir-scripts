#
# Simple program to generate the SHA-256
# crypto hash of a given file
#

import sys
import hashlib

print
print ("Simple program that generate the SHA-256 hash of any file")
print

# Main sha256 hash function 
def sha256(file_name):
	hash_sha256 = hashlib.sha256()
	
# Iterate a file larger than 4096 bytes 
	with open(file_name, "rb") as open_file:
		for chunk in iter(lambda: open_file.read(4096), b""):
			hash_sha256.update(chunk)
	print "The SHA256 hash for this file is: " 
	print hash_sha256.hexdigest()

# Check to see if the file is passed as an argument
if len(sys.argv) < 2:
    print "You must provide the file to hash."

if len(sys.argv) == 2:
	sha256(sys.argv[1])
