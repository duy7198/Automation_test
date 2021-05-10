# ** Highlander automation test procedure **\
\
## ** Setup environment: **\
____1. Enable Developer mode on Window\
____2. Install WinAppDriver, Python and Pycharm\
		- Link download https://drive.google.com/drive/folders/11BLHStrN5Tse9bcVN-c29agVNaIXfbS7?usp=sharing\
		- Link setup guideline: https://testautomationu.applitools.com/winappdriver-tutorial/chapter1.html\
____3. Copy all library folders in Lib folder from above link and paste them to the library folder of Python. It will be "C:\Python39\Lib" if you follow the guideline.\
\
## ** Setup Test runner in Pycharm: **\
____1. Open Pycharm\
____2. Choose File > Settings > Tools > Python Integrated Tools\
____3. At Testing, change Default test runner from Unittests to pytest\
____4. Click Apply and then click OK\
\
## ** Add Configurations: **\
____1. Choose Run > Edit Configuration\
____2. Click Add button at the top left\
____3. At Python tests, duple click pytest\
____4. Insert Name configuration, choose Script path of the file which you want to run\
____5. Click Apply and then click OK\
\
## ** Run test: **\
____1. Open highlander_auto folder\
____2. Run testcase.py (on PLC) or testcase_lap.py (on your laptop) with pytest\
____3. Observe the result.\
