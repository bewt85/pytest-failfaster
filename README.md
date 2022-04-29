# Failfaster

Failfaster makes your tests fail earlier in a test run.

It does this by comparing the project with the last time it was tested and changing the order the tests run.

Tests are prioritised as follows:
* tests which failed
* tests which are new
* tests which didn't run
* tests which were ok last time

Each category is further sorted by how long the test took to finish last time.

It works by sending a list of commits and the names of all the tests to a server.  The server decides the order the tests should run in.