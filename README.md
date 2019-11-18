Scripts which realise different scenarios for testing [egts-debugger](https://github.com/SatisSoft/egts-debugger).\
1) success.py - success scenario;
2) disconnect.py - disconnect scenario;
3) incorrect_first.py - first message is incorrect scenario;
4) incorrect_nav.py - incorrect navigation packet scenario;
5) not_enough_packets.py - received not enough packets scenario;
6) only_auth.py - received only auth packet scenario;
7) two_auth.py - receive two auth packet scenario;
8) without_auth.py - didn't received auth packet scenario;
9) incorrect_dit.py - incorrect dispatcher type
10) incorrect_did.py - incorect dispatcher id scenario;
11) success_without_did - success without dispatcher id scenario;
12) incorrect_did_default - didn't specify dispathcer id and receive some scenario.

To test some scenario open two consoles. In the first start [egts-debugger](https://github.com/SatisSoft/egts-debugger):
\python3.6 start_server_debugger.py [flags]\
In the second start test scenario:\
python3.6 success.py\
Then look to the logs in egts-debugger's console to make sure the debugger is working correctly.