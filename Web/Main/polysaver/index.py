# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *

from os.path import dirname, join, basename

@Expose
def Request(self):
  yield


  self.UI.JSDeps.append(join(dirname(self.Env.ScriptPath), basename(self.Env.ScriptPath) or 'index' + '.js'))
  
  self.UI.Body('''
    <h2>Polysaver</h2>
    <hr>
    This is an example of hue and handling events.
    
  
    ''')
  yield self.UI
