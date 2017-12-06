import argparse
import os
import logging

def ParseCommandLine():
	parser = argparse.ArgumentParser('Python Word Search')

	parser.add_argument('-v','--verbose',help="Enabled printing of program messages",action='store_true')
