'''
Problem Statement -> 

Description: You’re analyzing test execution logs to detect duplicate test IDs, which indicate a misconfiguration in the testing framework. Each log entry is a string in the format <test_id>:<status>, where <test_id> is an alphanumeric string and <status> is either "PASS" or "FAIL". Write a function that takes a list of log entries and returns a list of test IDs that appear more than once, sorted alphabetically. If no duplicates exist, return an empty list. Ensure all log entries are valid (non-empty test_id, valid status).

Input: ["TEST1:PASS", "TEST2:FAIL", "TEST1:PASS", "TEST3:PASS"]
Output: ["TEST1"]
Input: ["TEST1:PASS", "TEST2:FAIL", "TEST3:PASS"]
Output: []
Input: ["TEST1:PASS", "TEST2:ERROR"]
Output: []  # Invalid status, return empty
'''

