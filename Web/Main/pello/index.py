# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *

from os.path import dirname, join, basename

from . import PolySaverURL


@Expose
def Request(self):
  yield

  Board_GSID = self.Map.get('Board_GSID', None)

  self.UI.JSData.Board = aadict()
  self.UI.JSData.Board.Board_GSID = Board_GSID
  self.UI.JSData.Board.Data = None
  
  if Board_GSID:
    try:
      tmp = App.DB.Value('''
        SELECT
          "Data"
        FROM
          "PolySaver"."Board"
        WHERE True
          AND "Board_GSID" = $Board_GSID
        ''',
        Board_GSID = Board_GSID
        )
      
      self.UI.JSData.Board.Data = JD(tmp)
    except App.DB.NotOneFound:
      yield self.RedirectResponse('/polysaver/?404')


  BoardList = App.DB.RowList('''
    SELECT
      "Board_GSID"
    FROM
      "PolySaver"."Board"
    ORDER BY 
      "CreateDate" DESC
    LIMIT 
      40
    ''')

  self.UI.JSDeps.append(join(dirname(self.Env.ScriptPath), 'index.js'))
  
  self.UI.Body('''
    <h2>polysaver</h2>
    <p>
      A fun little game of drawing polygons.
    </p>
    
    <p>
      <small>
        Click anywhere to start a polygon, then click elsewhere to add segments.
        When you are done making the polygon, click the starting position to finish.
        Hold the `Shift` key and click on any polygon to remove it.
      </small>
    </p>
    <hr>
    <p>
      <strong><a href="/polysaver/">Start A New Board</a></strong>
    </p>
    <p>
      <strong>Current Board:</strong> ''' + HS(Board_GSID or 'Unsaved') + '''
    </p>
    <p>
      <a id="savelink" class="btn btn-primary" href="#">Save</a>
      <a id="discardlink" class="btn btn-warning" href="">Discard</a>
    </p>
    <hr>
    <h4>Recent Boards</h4>
    ''' + JN('''
      <a style=''' + QA('font-weight: bold;' if Board_GSID == row.Board_GSID else '') + ''' href=''' + QA(PolySaverURL(row.Board_GSID)) + '''>''' + HS(row.Board_GSID) + '''</a><br>  
    ''' for row in BoardList) + '''
    
    
    ''')
  yield self.UI
