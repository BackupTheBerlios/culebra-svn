'''
This file is for the Project Manager module of the Culebra IDE
'''
try :
	import pygtk
	pygtk.require('2.0')
except :
	import sys
	print 'We need PyGTK version 2.0 or superior to continue'
	sys.exit(1)

import gtk
import gtk.glade

# -- Propias internas
import culebraprj

class ProjectManager :
	gladefile = 'project-manager.glade'
	projectName = 'Culebra IDE'
	def __init__(self) :
		self.wxTree = gtk.glade.XML(self.gladefile)
		self.wxTree.signal_autoconnect(self)
		self.wxTree.get_widget('prjToolBar_Main').set_style(gtk.TOOLBAR_ICONS)
		# -- Nos ecargamos del modelo principal y caracteristicas de la treeview
		self.treeview = self.wxTree.get_widget('prjTreeView_Project')
		self.treemodel = gtk.ListStore(str)
		self.treeview.set_model(self.treemodel)
		self.treeview.append_column(gtk.TreeViewColumn('archivo', gtk.CellRendererText(), text=0))
		
		# -- Al principio no hay nada...
		self.wxTree.get_widget('prjWindow_Main').set_title('Unamed Project')
		
	def on_window_destroy(self, *widgets) :
		gtk.main_quit()
		
	def on_prjToolButton_Open_clicked(self, *widgets) :
		print 'Open button clicked!'
		
	def on_prjToolButton_Save_clicked(self, *widgets) :
		print 'Save button clicked'
		
	def on_prjToolButton_Add_clicked(self, *widgets) :
		print 'Add button clicked'
		
	def on_prjToolButton_Remove_clicked(self, *widgets) :
		print 'Remove Button clicked'
	
	def loadProjectFile(self, projectfile) :
		try :
			prjFile = culebraprj.CulebraProject(projectfile)
		except IOError :
			print 'Error abriendo el archivo'
			return
		except culebraprj.ProjectParseError :
			print '%s No parece ser un archivo valido' % projectfile
			return
		# -- Ahora revisamos todo
		self.projectName = prjFile.prjName()
		for fileitem in prjFile.getAll() :
			self.treemodel.append([fileitem.getName()])
		
if __name__ == '__main__' :
	app = ProjectManager()
	app.loadProjectFile('example.culebra')
	gtk.main()