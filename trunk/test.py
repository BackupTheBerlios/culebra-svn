import gtk

def click(btn=None):
	
	print "click"

w = gtk.Window()

b =  gtk.Button("Click")

w.add(b)

a = 1

b.connect('clicked', click)

w.show_all()
w.connect('delete-event', gtk.main_quit)

gtk.main()