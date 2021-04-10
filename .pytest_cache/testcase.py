from appium import webdriver
import unittest
import data
import function


class Test(unittest.TestCase):
    jive = function.Function(webdriver)
    robot = function.Function(webdriver)

    def test1_VerifyGUI(self):
        Test.jive.open(data.driver, data.jivePath)
        version = Test.jive.get(data.jiveVersion)
        self.assertEqual(data.jiveVersion, version)

    def test2_FindNoneRobot(self):
        Test.jive.click(data.findRobot)
        ip = Test.jive.get(data.ipRobotBox)
        self.assertEqual(data.ipNone, ip)

    def test3_FindRobot(self):
        Test.robot.open(data.driver, data.robotPath)
        Test.jive.click(data.findRobot)
        ip = Test.jive.get(data.ipRobotBox)
        self.assertEqual(data.ipRobot, ip)

    def test4_ConnectRobot(self):
        Test.jive.click(data.connect)
        status = Test.jive.get(data.connected)
        self.assertEqual(data.connected, status)

    def test5_ConnectRobotLifeTime(self):
        Test.robot.close()
        status = Test.jive.get(data.disconnected)
        result = [status]
        Test.robot.open(data.driver, data.robotPath)
        _status = Test.jive.get(data.connected)
        result.append(_status)
        self.assertEqual([data.disconnected, data.connected], result)
        # End testing
        Test.jive.close()
        Test.robot.close()


if __name__ == '__main__':
    unittest.main()
