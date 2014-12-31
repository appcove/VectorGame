# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *

import time
import re

import AppStruct.Web.Handler.Point
import AppStruct.Web.Plugin

import Project.Web.GameUI


###############################################################################
class application(
  AppStruct.Web.Handler.Point.PointHandler,
  AppStruct.Web.Plugin.SessionToken,
  AppStruct.Web.Plugin.QueryString,
  AppStruct.Web.Plugin.Post,
  AppStruct.Web.Plugin.Cookie,
  AppStruct.Web.Plugin.Logger,
  ):

  # Settings
  ScriptPathMatch = '/'
  SessionToken_CookieName = 'SessionToken'

  # Custom attributes
  AppSession = None  # App Session Key
  PostData = None  # JSON Decoded data from POST
  
  Auth_Required = True  # Is auth required for this request?
  BrowserSession = None
  EntitySession = None

  Perm_Active_Required = True
  Perm_Admin_Required = False

  # Set to 'http' to force http, 'https' to force https, or None to accept either.
  RequireProtocol = None
  
  # Proxy related information
  ProxySSL = None
  Proxy_HTTP_URL = None
  Proxy_HTTPS_URL = None
  
  # Instance variables
  UI = None
  User = None
  #----------------------------------------------------------------------------

  # Beginning of Request handler
  def RequestStart(self):
    App.Enter(Log = self.Log)
    App.Log('PointHandlerStart:' + self.SessionToken[0:12])# + ':URI=' + self.Env.URI)

    # Setup the browser session key object
    self.BrowserSession = SessionKey('BrowserSession', self.SessionToken)

    self.Env.Log(self.Env)
    if 'HTTP_SCHEME' not in self.Env:
      raise Exception('Cannot run application without Scheme environment variable set')
    elif self.Env['HTTP_SCHEME'] == 'http':
      self.ProxySSL = False
    elif self.Env['HTTP_SCHEME'] == 'https':
      self.ProxySSL = True
    else:
      raise Exception("Cannot run application without Scheme environment variable set to either 'http' or 'https' instead of: {0}".format(self.Env['HTTP_Scheme']))
  
  
  # End of Request handler
  def RequestEnd(self, res, exc):
    App.Log('PointHandlerEnd:' + self.SessionToken[0:12] + ':Header={0}'.format(str(self.ResponseHeader.All())))
    exc and App.Log(exc)
    App.Exit()

    if self.ResponseType == 'json':

      if exc and isinstance(exc, ValidationError):
        return self.JSONResponse(dict(
          Type = 'ValidationError',
          Data = exc.Errors.MessageList(),
          ))

      elif exc:
        return self.JSONResponse(dict(
          Type = exc.__class__.__name__,
          Data = str(exc),
          ))

      else:
        return self.JSONResponse(dict(
          Type = 'Data',
          Data = res,
          ))


###############################################################################


@Expose
def Init(self):
  yield

  
  # Do we need a redirect because of RequireProtocol?
  if self.RequireProtocol == 'http':
    if self.ProxySSL:
      target = self.Proxy_HTTP_URL + self.Env.URI
      App.Log('Due to RequireProtocol==http, redirecting to ' + target)
      yield self.RedirectResponse(target)
  elif self.RequireProtocol == 'https':
    if not self.ProxySSL:
      target = self.Proxy_HTTPS_URL + self.Env.URI
      App.Log('Due to RequireProtocol==https, redirecting to ' + target)
      yield self.RedirectResponse(target)
  elif self.RequireProtocol is not None:
    raise ValueError('Invalid value for self.RequireProtocol: {0}'.format(repr(self.RequireProtocol)))

 
  self.UI = self.Response(Project.Web.GameUI.PrimaryLayout)

  yield

###############################################################################





