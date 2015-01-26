# airtel-usage
Python script that finds your Airtel Broadband usage and sends a notification to OS X's notification center.

#### Screenshot
![Airtel Usage Screenshot](https://raw.githubusercontent.com/paambaati/airtel-usage/master/screenshot.png)

#### Requisites
1. OS X.
2. [terminal-notifier](https://github.com/alloy/terminal-notifier). You can install this using `brew install terminal-notifier`.

#### Notes
1. Tested only on OS X Yosemite 10.10.1
2. The script can be run on startup. To do that,
    1. Modify `com.gp.airtel.plist` with the correct paths of your script; at lines `8` and `10`.
    2. Copy `com.gp.airtel.plist` to`~/Library/LaunchAgents`
    3. Run `launchctl load ~/Library/LaunchAgents/com.gp.airtel.plist`
    4. Run `launchctl start com.gp.airtel`
    5. Restart and check if it runs on boot.

#### Changelog

__1.1 (25 January 2015)__

`+ Support for logging to OS X Console.`

`+ Added optional PLIST for running script as LaunchAgent.`

__1.0 (25 January 2015)__

`+ Initial release.`
  
#### License

The MIT License (MIT)

Copyright (c) 2015 Ganesh Prasannah (exchequer598@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
