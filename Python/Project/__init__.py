# vim:encoding=utf-8:ts=2:sw=2:expandtab

from AppStruct import ThreadedAppMeta, ThreadedAppProperty
import AppStruct.Database.PostgreSQL
import AppStruct.Database.Redis
from AppStruct.Util import *
import AppStruct.Util
from AppStruct.Web.Util import *
import AppStruct.Web.Util
import FileStruct
import locale

from .Local import Postgres, Redis
import re


###############################################################################
# Conf imports that don't need to be exposed in App


class App(metaclass=ThreadedAppMeta):
  
  # Conf imports that need to be exposed in App
  from .Local import Path, Identifier, DevLevel, CacheTime
  from .Local import Main_HTTP_URL, Main_HTTPS_URL
  
  
  # Database Connection
  @ThreadedAppProperty
  def DB(self, client):
    if client is None or client.state == 'closed':
      client = AppStruct.Database.PostgreSQL.Open(**Postgres)
    return client
  
  # Redis Connection
  @ThreadedAppProperty
  def Redis(self, client):
    if client is None:
      client = AppStruct.Database.Redis.Redis(**Redis)
    return client
  
#  # Called once when the app loads
#  def onInit(self):
#    with self:
#      self.Setting.update(self.DB.Row('SELECT * FROM "Main"."Setting"'))

    


###############################################################################
# Global Utility Functions


# Date Long Text
def DLT(DateObject, NoneText='None'):
  return DateObject.strftime('%b %d, %Y') if DateObject else NoneText

# Time Long Text
def TLT(DateTimeObject, NoneText='None'):
  return DateTimeObject.strftime('%b %d, %Y %I:%M %p %z') if DateTimeObject else NoneText

# Decimal format for input
def DFI(Num):
  Num = re.sub('[^0-9.]', '', str(Num))
  return ('0.00' if Num == '' else "%.2f" % Decimal(Num))

# Decimal signed format for input
def DSFI(Num):
  Num = re.sub('[^0-9.-]', '', str(Num))
  return ('0.00' if Num == '' else "%.2f" % Decimal(Num))

# Output Decimal Value
def DFO(Num):
  locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
  Num = str(Num).strip()
  return locale.format("%.2f",(0.00 if Num == '' else Decimal(Num)),grouping=True)

# Integer format for input
def IFI(Num):
  Num = re.sub('[^0-9.]', '', str(Num))
  return "%.0f" % (0.00 if Num == '' else Decimal(Num))

# Output Integer Value
def IFO(Num):
  locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
  Num = str(Num).strip()
  return locale.format("%.0f",(0.00 if Num == '' else Decimal(Num)),grouping=True)

# Output currency value
def CUR(Num):
  locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
  return ('$0.00' if str(Num).strip() == '' else locale.currency(Decimal(Num),grouping=True))

def ELIP(string, length):
  string = str(string).strip()
  length = int(length)

  return (string if len(string) <= length else (string[0:int(length - 3)] + '...'))


###############################################################################
# Define all of the gloabls that will be imported with *

__all__ = \
  AppStruct.Util.__all__ + \
  AppStruct.Web.Util.__all__ + \
  (
    'App',
    'DLT',
    'TLT',
    'DFI',
    'DFO',
    'IFI',
    'IFO',
    'CUR',
    'ELIP',
  )



