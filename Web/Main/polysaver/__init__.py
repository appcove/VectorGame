# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *
import Project.Web.DemoUI

@Expose
def Init(self):
  yield
  self.UI = self.Response(Project.Web.DemoUI.PrimaryLayout)
  yield


