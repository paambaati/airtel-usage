#!/usr/bin/python

# airtel.py
# Finds Airtel Broadband usage and sends a notification to OS X's Notification Center.
# (C) 2015 - GP (exchequer598@gmail.com)
# https://github.com/paambaati/airtel-usage

import urllib2
import sys
from subprocess import Popen, PIPE, call
from plistlib import readPlist

# Global variables.
AirportPath = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport'
AirtelSmartbytesUrl = 'http://122.160.230.125:8080/gbod/gb_on_demand.do'
HomeSsid = 'YellPenisForPassword'
NotificationTitle = 'Airtel Broadband Usage'
NotificationImage = 'airtel.png'
NotificationSound = 'default'


def getUsage(url):
    """
    Sends a request to `AirtelSmartbytesUrl`, hack-parses for
    quota, data limit and days left and returns them.
    """
    response = urllib2.urlopen(url)
    data = response.read()
    quota = data.split('<li>Balance quota:&nbsp;&nbsp;&nbsp;')[1].split(
        '</li>')[0].replace('&nbsp;', ' ')
    limit = data.split('<li>High speed data limit:&nbsp;&nbsp;&nbsp;')[
        1].split('</li>')[0].replace('&nbsp;', ' ')
    days_left = data.split(
        '<li>No. of days left in the current bill cycle:&nbsp;&nbsp;&nbsp;')[1].split('</li>')[0]
    return {'quota': quota, 'limit': limit, 'days_left': days_left}


def getWifiSSID():
    """
    Gets SSID of currently connected WiFi network.
    Works by reading Airport's PLIST file.
    I am just assuming that the last SSID is the one we're connected to.
    Any exception and the method simply returns None.

    NOTE 1: Will work only for OS X.
    NOTE 2: Tested *only* on OS X Yosemite 10.10.1
    """
    try:
        proc = Popen([AirportPath, '-s', '-x'], stdout=PIPE)
        ssid_data = readPlist(proc.stdout)
        ssid_length = len(ssid_data)
        ssid = ssid_data[ssid_length - 1]['SSID']
        ssid = ssid.data
    except:
        ssid = None
    return ssid


def sendNotification(title, subtitle, message):
    """
    Sends a notification to the notification center.

    NOTE 1: Needs `terminal-notifier` to be installed. Install with `brew install terminal-notifier`.
    NOTE 2: Will work only on OS X.
    """
    call(['terminal-notifier', '-group', 'airtel-usage', '-title', title, '-subtitle', subtitle, '-message', message,
          '-contentImage', NotificationImage, '-sender', 'com.apple.notificationcenterui', '-sound', NotificationSound])

# Main
if(HomeSsid == getWifiSSID()):
    usage = getUsage(AirtelSmartbytesUrl)
    subtitle = '{0} of {1} remaining'.format(usage['quota'], usage['limit'])
    message = '{0} days remaining until cycle ends.'.format(usage['days_left'])
    sendNotification(NotificationTitle, subtitle, message)
