'''
This module just handle the format of the Project File
'''

from xml.dom import minidom

class ProjectParseError(Exception) : pass

class ProjectFile :
	'''
	A class to represent each file inside the project definition
	'''
	def __init__(self, domnode) :
		self._name = domnode.getAttribute('name')
		self._type = domnode.getAttribute('type')
		
	def getName(self) :
		return self._name
		
	def getType(self) :
		return self._type
		
class CulebraProject :
	'''
	Class representing the Main Project File
	'''
	_name = ''
	
	def __init__(self, filename) :
		try :
			self._xmltree = minidom.parse(filename)
		except IOError :
			raise IOError
		except :
			import sys
			print 'Error Opening the File!'
			sys.exit(1)
		project = self._xmltree.getElementsByTagName('culebra')
		if len(project) > 1 :
			raise ProjectParseError
		self._name = project[0].attributes['name'].value
		# -- Now we process the files specified in the file section
		files = project[0].getElementsByTagName('item')
		self._files = [ProjectFile(item) for item in files]
	
	def prjName(self) :
		return self._name
		
	def __getitem__(self, item) :
		return self._files[item]
		
	def __len__(self) :
		return len(self._files)
		
	def getAll(self) :
		return self._files

if __name__ == '__main__' :
	prj = CulebraProject('example.culebra')
	print len(prj)