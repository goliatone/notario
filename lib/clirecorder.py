#!/usr/bin/env python
# we make it executable


from cement.core import backend, foundation, controller, handler
from cement.utils import shell

#from gntp.notifier import mini
import gntp.notifier

from path import path
from sarge import shell_format, run, Capture, capture_stdout

import pickle
import subprocess
import os

#Files included in the app.
from lib.breader import BackwardsReader
from lib.note import Note


#pip install sarge
#pip install path
#TODO If we want to make it crossplat: http://coffeeghost.net/src/pyperclip.py

#define an app base controller
#============
#sudo nano ~/.bash_profile 
#alias note='python /Users/emilianoburgos/Development/PYTHON/cement/notable.py'
#=============
class CLIRecorderController(controller.CementBaseController):
	class Meta:
		label = 'base'
		description = "My Application does amazing things!"

		config_defaults = dict(
			note='Note',
			e= 'subl',
			debug=True
			)
		arguments = [
			(['-n', '--note'], dict(action='store', 
									help='the notorious foo option')),
			(['-c', '--content'], dict(action='store', 
										help='Create a new note.')),
			(['-cp', '--copy'], dict(action='store_true',
									help='Copy note to clipboard')),
			(['-pt', '--paste'], dict(action='store_true',
									help='Copy note to clipboard')),
			(['-e'], dict(action='store_const', const='subl',
									help='Opens Note in users default editor.')),
			(['-editor'], dict(action='store',
									help='Opens Note in given editor.'))
		]


	@controller.expose(help='this is some command', aliases=['some-cmd'])
	def some_other_command(self):
		self.log.info(self.pargs.note)
		#pass

	@controller.expose(help="Start record CLI process.")
	def record(self):
		"""
		This simple stores the note name, so we can grep
		the history.
		"""
		storage = path('./.store/')
		if storage.exists() is False:
			storage.makedirs()
		
		# write python dict to a file
		record = {'record': self.pargs.note}
		output = open('./.store/record.pkl', 'wb')
		pickle.dump(record, output)
		output.close()
		#exitcode = shell.exec_cmd2(['echo', 'helloworld'])
		#event = subprocess.Popen(["bash","-i", "-c", "echo record"])
		#output = event.communicate()

	@controller.expose(help="Stops record CLI process.")
	def stop(self):
		# read python dict back from the file
		record = open('./.store/record.pkl', 'rb')
		note = pickle.load(record)
		record.close()
		name = note['record']
		#print name

		#shell_command = 'bash -i -c "history -r; history"'
		#shell_command = "history | sed -n '/-n %s/,/notable.py stop/p' | grep -v 'otable.py stop'" % name
		#print shell_command

		#p = run(shell_command, stdout=Capture(), shell=True)
		#print p.stdout.text
		#"""
		bash_history_text = ''
		homedir = os.path.expanduser('~')
		bash_history = open(homedir+"/.bash_history", 'r')
		br = BackwardsReader(bash_history)
		while  True:
			line = br.readline()
			if not line:
				break
			bash_history_text += line
		#bash_history_text = bash_history.read()		
		print bash_history_text
		#"""

if __name__ == "__main__":

	#create the app
	app = CLIRecorderController(config_files=['/.config.ini'],)

	try:
		app.setup()
		# print app.config.get('notable', 'ext')
		print app.config.get_sections()
		print app.config.options('log')
		app.run()
	finally:
		app.close()