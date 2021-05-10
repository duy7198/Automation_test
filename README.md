#  Highlander automation test procedure

##  Setup environment:
1. Enable Developer mode on Window
2. Install WinAppDriver, Python and Pycharm \
		- Link download https://drive.google.com/drive/folders/11BLHStrN5Tse9bcVN-c29agVNaIXfbS7?usp=sharing \
		- Link setup guideline: https://testautomationu.applitools.com/winappdriver-tutorial/chapter1.html
3. Copy all library folders in Lib folder from above link and paste them to the library folder of Python. It will be "C:Python39Lib" if you follow the guideline.

##  Setup Test runner in Pycharm: 
1. Open Pycharm
2. Choose File > Settings > Tools > Python Integrated Tools
3. At Testing, change Default test runner from Unittests to pytest
4. Click Apply and then click OK

##  Add Configurations: 
1. Choose Run > Edit Configuration
2. Click Add button at the top left
3. At Python tests, duple click pytest
4. Insert Name configuration, choose Script path of the file which you want to run
5. Click Apply and then click OK

##  Run test: 
1. Open highlander_auto folder
2. Run testcase.py (on PLC) or testcase_lap.py (on your laptop) with pytest
3. Observe the result.
