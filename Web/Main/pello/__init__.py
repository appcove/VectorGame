# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *
import Project.Web.DemoUI

import re

VALID_MATCH = re.compile('^[a-z0-9]{16}$').match

def PolySaverURL(Board_GSID):
  return App.Main_HTTPS_URL + '/polysaver/' + (Board_GSID or '')

@Expose
def Mapper(self, parts):
  if len(parts) == 1:
    if VALID_MATCH(parts[0]):
      self.Map.Board_GSID = parts[0]
      return ('index',)


@Expose
def Init(self):
  yield
  self.UI = self.Response(Project.Web.DemoUI.PrimaryLayout)
  yield


