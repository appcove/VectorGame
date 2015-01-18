# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *
from Project.Web.Util import UI_password, UI_text, UI_checkbox
import Project.Main.User

@Expose
def Request(self):
  yield

  RURI = self.Get.RURI or '/'

  if 'logout' in self.Get:
    App.Redis.delete(self.BrowserSession.User_MNID)
    yield self.RedirectResponse('/')

  Username = IN_Str(self.Post.Username)
  Password = IN_Str(self.Post.Password)
  Error = None

  for _ in ONCEIF(self.Post):
    try:
      if not Username or not Password:
        raise ValidationError("Fields cannot be left blank.")
        break

      Remember = ('Remember' in self.Post)
      User_MNID = Project.Main.User.AuthenticateByUsernameAndPassword(Username, Password)

      App.Redis.set_int(self.BrowserSession.User_MNID, User_MNID)
      App.Redis.expire(self.BrowserSession.User_MNID, (3600 * 24 * 30 if Remember else 3600))
      yield self.RedirectResponse(RURI)
    
    except (AuthenticationError, ValidationError) as e:
      Error = str(e)

  #============================================================================
  self.UI.Body('''
    ''' + ('<div style="color: red;">' + HS(Error) + '</div>' if Error else '') + '''

    <h1>Gahooa Playground</h1>
    A place new ideas are tried, tested, and discarded.
    <hr>
    <div class="row">
      <div class="col-md-6">
        <h4><a href="/game/">Vector Game</a></h4>
        This is a game of strategy, intel, and patience.
        <hr>
        <h4><a href="/polysaver/">Polysaver</a></h4>
        This is a fun vector graphics program.
        <hr>
        <h4><a href="/pello/">Pello</a></h4>
        Some thoughts on managing tasks with splines and polygons.
      </div>
      <div class="col-md-6">
        ''' + ('''
        <h2>Logged in as ''' + HS(self.User.Name) + '''</h2>
        <a href="/?logout">Logout</a>

        ''' if self.User else ''' 
        <h2>Log in</h2>

        <form class="form-horizontal" role="form" method="post">

          ''' + UI_text(self.Post, 'Username', 'User Name') + '''

          ''' + UI_password(self.Post, 'Password', 'Password') + '''

          ''' + UI_checkbox(self.Post, 'Remember', 'Remember Me', classes='col-sm-offset-4') + '''

          <div class="form-group">
            <div class="col-md-8 col-md-offset-4">
              <button type="submit" class="btn btn-default">Login</button>
            </div>
          </div>

        </form>

        ''') + '''
      </div>
    </div>


  
    ''')
  yield self.UI
