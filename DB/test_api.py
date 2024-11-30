"""
This script runs and prints the curl commands from "API_communication".txt to test basic API communication. 

Author: HereItIs Group
Date: 11-13-2024

"""
import os

def test_api():
    # Read commands from file
    with open('API communication.txt', 'r') as file:
        # Split the content into separate commands using double newlines
        commands = file.read().split('\n\n')
    
    # Execute each command
    test_num = 1
    for command in commands:
        print(f"\n=== Test {test_num} ===")
        print(f"Executing: {command}\n")
        os.system(command)
        print("\n")
        test_num += 1

if __name__ == "__main__":
    test_api()