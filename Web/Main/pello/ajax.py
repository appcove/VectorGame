# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *
import AppStruct.Web.Mapper
import AppStruct.Security

from . import PolySaverURL

@Expose
class Mapper(AppStruct.Web.Mapper.JSONMapper):
  pass



@Expose
def Save(self):
  self.RequestType = 'json'
  self.ResponseType = 'json'
  yield
  
  Board_GSID__Parent = self.PostData['Board_GSID']
  Board_GSID = AppStruct.Security.RandomHex()[0:16]
  Data = self.PostData['Data']

  App.DB.Execute('''
    INSERT INTO 
      "PolySaver"."Board"
      ([Field])
    VALUES
      ([Value])
    ''',
    ('Board_GSID', Board_GSID),
    ('Board_GSID__Parent', Board_GSID__Parent),
    ('CreateAddr', self.Env.RemoteAddr),
    ('Data', JE(Data)),
    )

  yield {
    'Board_GSID': Board_GSID, 
    'URL': PolySaverURL(Board_GSID)    
    }
  


