import os
import sys
import pyclbr

class List:

    def __init__(self):
        self.file = 'ClassBrowser.py'

    def listclasses(self):
        dir, file = os.path.split(self.file)
        name, ext = os.path.splitext(file)
        if os.path.normcase(ext) != ".py":
            return []
        try:
            dict = pyclbr.readmodule_ex(name, [dir] + sys.path)
        except ImportError, msg:
            return []
        items = []
        self.classes = {}
        for key, cl in dict.items():
            if cl.module == name:
                s = key
                if hasattr(cl, 'super') and cl.super:
                    supers = []
                    for sup in cl.super:
                        if type(sup) is type(''):
                            sname = sup
                        else:
                            sname = sup.name
                            if sup.module != cl.module:
                                sname = "%s.%s" % (sup.module, sname)
                        supers.append(sname)
                    s = s + "(%s)" % ", ".join(supers)
                items.append((cl.lineno, s))
                self.classes[s] = cl
        items.sort()
        list = []
        for item, s in items:
            list.append(s)
            print s
            self.listmethods(s)
        return list

    def listmethods(self, cl):
        if not cl:
            return []
        items = []
        for name, lineno in self.cl.methods.items():
            items.append((lineno, name))
        items.sort()
        list = []
        for item, name in items:
            list.append(name)
        return list

if __name__ == "__main__":
    List().listclasses()
