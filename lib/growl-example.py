#!/usr/bin/env python -i

# May 12, 2007
# by tooru
#
# clickable growl example
#
# requires pyobjc and growl.framework

import objc
from Foundation import *
from AppKit import *
from PyObjCTools import NibClassBuilder, AppHelper
import time


# load Growl.framework
myGrowlBundle=objc.loadBundle("GrowlApplicationBridge", globals(), bundle_path=objc.pathForFramework(
        u'/Library/Frameworks/Growl.framework'))


# growl delegate
class rcGrowl(NSObject):

    def rcSetDelegate(self):

        GrowlApplicationBridge.setGrowlDelegate_(self)

    def registrationDictionaryForGrowl(self):

        return {u'ApplicationName':u'rcGrowlMacTidy',u"AllNotifications":[u'test1'],u"DefaultNotifications":[u'test1']}
   
    # don't know if it is working or not
    def applicationNameForGrowl_(self):

        return u'rcGrowlMacTidy'

    # the method below is called when notification is clicked
    def growlNotificationWasClicked_(self,clickContextS):

        print ''
        print 'clicked at',time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())
        print 'clickContextS =',clickContextS

    # the method below is called when notification is timed out
    def growlNotificationTimedOut_(self,clickContextS):

        print ''
        print 'timeout at',time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())
        print 'clickContextS =',clickContextS
    
    # doesn't seem to work
    def growlIsReady(self):

        print 'growl IS READY'



# delegate for setting up NSStatusitem  
class Timer(NSObject):

    statusbar = None
    state = 'idle'

    def applicationDidFinishLaunching_(self, notification):
        statusbar = NSStatusBar.systemStatusBar()
        # Create the statusbar item
        self.statusitem = statusbar.statusItemWithLength_(NSVariableStatusItemLength)


        # Let it highlight upon clicking
        self.statusitem.setHighlightMode_(1)
        # Set a tooltip
        self.statusitem.setToolTip_('GrowlExample')
        # Set an initial title
        self.statusitem.setTitle_('GrowlExample')

        # Build a very simple menu
        self.menu = NSMenu.alloc().init()

        menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Popup notification', 'rcNotification:', '')
        self.menu.addItem_(menuitem)
        # Default event
        menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Quit', 'terminate:', '')
        self.menu.addItem_(menuitem)
        # Bind it to the status item
        self.statusitem.setMenu_(self.menu)


    def rcNotification_(self,notification):

        print ''
        print time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()), 'Growl notification...'

        GrowlApplicationBridge.notifyWithTitle_description_notificationName_iconData_priority_isSticky_clickContext_(\
            u'myTitle',u'test',u'test1',None,0,False,time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))
    
    

if __name__ == "__main__":

    # set up system statusbar GUI
    app = NSApplication.sharedApplication()
    delegate = Timer.alloc().init()
    app.setDelegate_(delegate)

    # set up growl delegate
    rcGrowlDelegateO=rcGrowl.new()
    rcGrowlDelegateO.rcSetDelegate()

    AppHelper.runEventLoop()