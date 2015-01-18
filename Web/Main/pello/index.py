# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *

from os.path import dirname, join, basename

from . import PelloURL


@Expose
def Request(self):
  yield
  
  BoardList = App.DB.RowList('''
    SELECT
      "Board_GSID"
    FROM
      "Pello"."Board"
    WHERE True
      AND "User_MNID" = $User_MNID
    ORDER BY 
      "CreateDate" DESC
    LIMIT 
      40
    ''',
    User_MNID = self.User.User_MNID
    )
  
  self.UI.Body('''
    <h2>Pello</h2>
    <p>
      Pello is a test of an advanced way to manage tasks using geometry.  
      People are excellent at seeing patterns.  Lists and grids are sterile and uniform.  
      Very little information is available at a glance.  Let's see what we can do.
    </p>
    
    <p>
      <small>
        You can enter one of your existing boards or start a new one.
      </small>
    </p>
    <hr>
    <p>
      <strong><a href="/polysaver/">Start A New Board</a></strong>
    </p>
    <h4>Your Boards</h4>
    ''' + JN('''
      <a style=''' + QA('font-weight: bold;' if Board_GSID == row.Board_GSID else '') + ''' href=''' + QA(PelloURL(row.Board_GSID)) + '''>''' + HS(row.Board_GSID) + '''</a><br>  
    ''' for row in BoardList) + '''
    
    
    ''')
  yield self.UI
