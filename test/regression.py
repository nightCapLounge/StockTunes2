import unittest
import json

print("====================================")
print("> Beginning Regression Test\n\n")

test_loader = unittest.TestLoader()
test_suite = test_loader.discover(".", "*_test.py")
test_result = unittest.TestResult()
test_suite.run(test_result)


print("\n")
print("> Total Tests Run:\t" + str(test_result.testsRun))
print("> Failed Tests:\t\t" + str(len(test_result.failures)))
print("> Skipped Tests:\t" + str(len(test_result.skipped)))
print("> Errors:\t\t" + str(len(test_result.errors)))
print(test_result.errors)

print("\n\n> Testing Complete")
print("====================================")
