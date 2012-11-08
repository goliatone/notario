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
class MinionNotesController(controller.CementBaseController):
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

	def _setup(self, base_app):
		super(MinionNotesController, self)._setup(base_app)

		self.dir = os.path.dirname(os.path.realpath(__file__))
		#TODO: Get from config file.
		#TODO: We want to use $EDITOR, how to expant to value?
		self.note = Note(self.dir+"/.notes/",".txt", "subl")



	@controller.expose(hide=True, aliases=['run'])
	def default(self):
		action = "list"
		if self.pargs.note:
			if not self._exists(): action = "new"
			else: action = "show"
			if self.pargs.content: action = "edit"

		if self.pargs.copy:
			self.copy()
		
		if self.pargs.paste:
			self.pargs.content = self._get_clip()
			action = "edit"

		if self.pargs.editor:
			self.editor = self.pargs.editor
		else: self.editor = None

		self.log.info("We are executing action: "+action)

		action = getattr(self, action)
		action()

		if (self.pargs.e or self.pargs.editor):
			self.note.open(self.pargs.note, self.editor)

		#x = 'default' if not x else x
		(namespace, n,c,cp,pt,e,editor,p) = vars(self.pargs)
		c = 'empty' if not c else c
		self.log.info('Hola'+c)
		# Send a simple growl message with mostly default values
		#gntp.notifier.mini("Here's a quick message", callback="http://github.com/")
		#self.log.info("Received option foo with value '%s'"% o)

	@controller.expose(aliases=['ls'], help="more stuff on list")
	def list(self):
		o = self.note.list()
		if not o:
			print "No Notes found."
		else:
			# print "Listing all Notes:" 
			print o

	@controller.expose(help="Shows the Note with given id.")
	def show(self):
		note = self.note.get(self.pargs.note)
		if not note:
			print "The note %s is empty."%self.pargs.note
		else:
			print note

	@controller.expose(help="Opens the Note in a new editor window.")
	def open(self, editor="subl"):
		note = self.pargs.note
		self.note.open(note)

	@controller.expose(help="Create a new thang.")
	def new(self):
		name    = self.pargs.note
		content = self.pargs.content
		self._save(content, name)

		if not content:
			self.open()
		
	
	@controller.expose(help="Add content to a note. Optionally opens editor.")
	def edit(self):
		name = self.pargs.note
		content = "%s" % self.pargs.content
		self._save(content, name)

	@controller.expose(help="Delete Note.")
	def delete(self):
		name = self.pargs.note
		self.note.delete(name)

	@controller.expose(aliases=['cp'], help="This command does relatively nothing.")
	def copy(self):
		"""
		Puts the content of a note into the clipboard.
		"""
		self.log.info("Inside base.copy function")

		name = self.pargs.note
		content = self.note.get(self.pargs.note)
		self._copy_clip(content)

	@controller.expose(help="Use clipboard contents")
	def clip(self):
		name = self.pargs.note
		content = self._get_clip()
		self._save(content, name)

	#TODO Make modular file access.
	def _save(self, content, name):
		if self.note.edit(name, content):
			if content:
				self._copy_clip(content)

	def _get_clip(self):
		outf = os.popen('pbpaste', 'r')
		content = outf.read()
		outf.close()
		return content
     	
	def _copy_clip(self, content):
		outf = os.popen('pbcopy', 'w')
		outf.write(content)
		outf.close()
	def _exists(self):
		return self.note.exists(self.pargs.note)

class Minion(foundation.CementApp):
	class Meta:
		label = 'teo'
		base_controller = MinionNotesController

if __name__ == "__main__":

	# TODO: Before release, figure out if we want to have also a ~/notable.ini
	config_path = os.path.dirname(os.path.abspath(__file__))+'/config.ini'

	#create the app
	app = Minion(config_files=[config_path],)


	# handler.register(MinionCliController)

	try:
		app.setup()
		# print app.config.get('notable', 'ext')
		print app.config.get_sections()
		print app.config.options('notable')
		app.run()
	finally:
		app.close()