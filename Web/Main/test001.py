# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *

@Expose
def Request(self):
  yield



  self.UI.JSDeps.append('./test001.js')
  

  self.UI.Body('''
    <strong>Handling Events</strong>
    <hr>
    This is an example of hue and handling events.
    
  
    ''')
  yield self.UI
