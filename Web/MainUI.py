# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *

from AppStruct.Web.Response import LayoutResponse
from AppStruct.UI import StringBuilder, SimpleMenu, ErrorList, InfoList, CSSList, JSList

###############################################################################
class PrimaryLayout(LayoutResponse):
  #============================================================================
  def __init__(self, *, Header):
    
    # Remember, Header, Status, and Buffer are reserved by the baseclass

    super().__init__(Header=Header)

    self.Title = 'Vector Game'

    self.Body = StringBuilder()
    self.Head = StringBuilder()
    self.Script = StringBuilder()
    self.Style = StringBuilder()

    self.CSS = CSSList()
    self.JS = JSList()

    self.JSDeps = ['App']
    self.JSData = aadict()

  def Process(self):


    self.Buffer.write('''
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

        <title>'''+HS(self.Title)+'''</title>

        <link rel="stylesheet" href="/lib/bootstrap-3.3.1/css/bootstrap.min.css">
        <link rel="stylesheet" href="/lib/bootstrap-3.3.1/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="/lib/font-awesome-4.2.0/css/font-awesome.css">
        <link rel="stylesheet" href="/lib/select2-3.5.2/select2.css">
        ''' + self.CSS.HTML() + '''
        ''' + WIF(self.Style.Value, '<style>', '</style>') + '''
        ''' + self.Head.Value + '''
      </head>

      <body style="margin: 10px;">
        ''' + self.Body.Value + '''

        <script src="/lib/underscore-1.7.0.min.js"></script>
        <script src="/lib/jquery-2.1.3.min.js"></script>
        <script src="/lib/bootstrap-3.3.1/js/bootstrap.min.js"></script>
        <script src="/lib/select2-3.5.2/select2.min.js"></script>
        <script src="/lib/jquery.autosize.min.js"></script>
        <script src="/lib/paperjs-0.9.21/paper-full.js"></script>

        ''' + self.JS.HTML() + '''
        ''' + WIF(self.Script.Value, '<script>', '</script>') + '''
        <script>
          var require = {
            baseUrl: '/',
            urlArgs: ''' + JS(JE(App.CacheTime)) + ''',
            deps: ''' + JS(JE(self.JSDeps)) + ''',
            config: {'App': ''' + JS(JE(self.JSData)) + '''}
          };
        </script>
        <script src="/lib/require-2.1.15.min.js"></script>
      </body>
    </html>

    ''')



