QA Automation Challenge Script
==============================

It is a modularized script made up of 4 files, qaGet.py, qaSet.py, qaMain.py and XML.py.

These are the instructions and considerations to take into account when executing the script.
---------------------------------------------------------------------------------------------


* Webdriver path is: C:\WebDriver

* Python 3.10 and Selenium Webdriver version 115.0.5790.170 (r1148114), was used.

* The script was designed to run with Google Chrome Version 115.0.5790.171.

* The script is started by running the qaMain.py file.

* Above each test case in the qaMain.py file, is the line #@unittest.skip(''), which allows you to isolate test cases if required.

* Once the script is finished, an HTML and an XML reports will be generated, which will be saved in the "reports" folder.

* The file text.txt will be generated, which captures the text of case 6, and a file test.png will be generated, which captures a screenshot of case 5.

* The XML.py file contains the script to generate the XML report from the testsuit.

* In the "Docs" folder, you will find the file that contains the RTM.


Tester: Cristian Montero