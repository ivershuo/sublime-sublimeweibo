import sublime, sublime_plugin
from aweibo import weibo

wb = weibo()

import json, webbrowser, time, os, urllib, random
from weibosdk import APIClient

class WeiboaccessCommand(sublime_plugin.WindowCommand):
	def run(self):
		wb.get_token()

class WeibosendCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Input your status here:", "", self.on_done, None, None)

	def on_done(self, text):
		wb.send(text)

class WeibogettimelineCommand(sublime_plugin.WindowCommand):
	def run(self):
		statuses = wb.get_timlines(True)
		tmpview = self.window.new_file()
		try:
			tmpview.set_syntax_file('Packages/JavaScript/JSON.tmLanguage')
			edit = tmpview.begin_edit()
			tmpview.insert(edit, 0, statuses)
			tmpview.end_edit()
		except:
			pass
			