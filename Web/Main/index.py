# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *

@Expose
def Request(self):
  yield


  self.UI.Body('''
    <h1>Welcome to Vector Land</h1>
    <hr>
    <h4><a href="/game/">Vector Game</a></h4>
    This is a game of strategy, intel, and patience.
    <hr>
    <h4><a href="/demo/polysaver/">Polysaver</a></h4>
    This is a fun vector graphics program.
    
  
    ''')
  yield self.UI
