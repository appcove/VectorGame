# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *
import re


IS_IDENTIFIER = re.compile('^[a-zA-Z_][a-zA-Z0-9_]*$').match


def MakeSIUD(Schema, Table, *primarykeys):

  if len(primarykeys) == 0:
    raise TypeError('Must pass at least one primary key argument')

  if not IS_IDENTIFIER(Schema):
    raise ValueError('Invalid schema: {0}'.format(Schema))
    
  if not IS_IDENTIFIER(Table):
    raise ValueError('Invalid table: {0}'.format(Table))

  sqlTable = '"{0}"."{1}"'.format(Schema, Table)
  sqlWhere = ''
  sqlPrimaryFields = ''

  for i,k in enumerate(primarykeys):
    if not IS_IDENTIFIER(k):
      raise ValueError('Invalid primary key field: {0}'.format(k))

    sqlWhere += 'AND "{0}" = $PK_{1}\n'.format(k, i)
    sqlPrimaryFields += '"{0}", '.format(k)

  sqlPrimaryFields = sqlPrimaryFields[:-2]  #strip comma space


  #============================================================================
  def SELECT(self, fields):
    kwargs = dict((('PK_{0}'.format(i),v) for i,v in enumerate(self.PrimaryKey)))
    return App.DB.Row('''
      SELECT
        [Field] 
      FROM 
        ''' + sqlTable + '''
      WHERE True 
        ''' + sqlWhere + '''
      ''',
      *fields,
      **kwargs
      )
  
  def INSERT(self, data):
    return App.DB.TRow('''
      INSERT INTO 
        ''' + sqlTable + '''
        ([Field])
      VALUES
        ([Value])
      RETURNING
        ''' + sqlPrimaryFields + '''
      ''',
      *data.items()
      )

  def UPDATE(self, data):
    kwargs = dict((('PK_{0}'.format(i),v) for i,v in enumerate(self.PrimaryKey)))
    App.DB.Execute('''
      UPDATE 
        ''' + sqlTable + '''
      SET
        [Field=Value]
      WHERE True
        ''' + sqlWhere + '''
      ''',
      *data.items(),
      **kwargs
      )
  
  def DELETE(self):
    kwargs = dict((('PK_{0}'.format(i),v) for i,v in enumerate(self.PrimaryKey)))
    App.DB.Execute('''
      DELETE FROM  
        ''' + sqlTable + '''
      WHERE True
        ''' + sqlWhere + '''
      ''',
      **kwargs
      )

  return SELECT, INSERT, UPDATE, DELETE





###################################################################################################
# CODE IN THIS NEXT FUNCTION IS `test grade` AND MUST BE ROLLED INTO Project/Base.py function/class
###################################################################################################

LField = {'Node_MNID', 'Node_MNID__Parent', 'Node_MSID', 'NodeType', 'Sequence', 'Title'}
RField = {'Node_MNID'}

###############################################################################
def Node_SIUD(Table):

  sqlLeftTable = '"CN"."Node"'
  sqlRightTable = '"CN"."{0}"'.format(Table)
  sqlWhere = 'AND "Node_MNID" = $pk0'

  #============================================================================
  def SELECT(self, fields):
    
    fields = set(fields)
    
    # Left fields are the ones that match the Left Field list
    LF = set.intersection(LField, fields)   

    # Right fields are the remaining ones that do not match the (left fields - shared fields)
    RF = set.difference(fields, set.difference(LField, RField))

    rval = {}
    
    if LF:
      rval.update(App.DB.Row('''
        SELECT
          [Field] 
        FROM 
          ''' + sqlLeftTable + '''
        WHERE True 
          ''' + sqlWhere + '''
        ''',
        *LF,
        pk0 = self.PrimaryKey[0]
        ))
    
    if RF:
      rval.update(App.DB.Row('''
        SELECT
          [Field] 
        FROM 
          ''' + sqlRightTable + '''
        WHERE True 
          ''' + sqlWhere + '''
        ''',
        *RF,
        pk0 = self.PrimaryKey[0]
        ))

    return rval

  #============================================================================
  
  def INSERT(self, data):
    
    fields = set(data)
    
    # Left fields are the ones that match the Left Field list
    LF = set.intersection(LField, fields)   
    LData = {k:data[k] for k in data if k in LF}

    # Right fields are the remaining ones that do not match the (left fields - shared fields)
    RF = set.difference(fields, set.difference(LField, RField))
    RData = {k:data[k] for k in data if k in RF}

    pk = App.DB.TRow('''
      INSERT INTO 
        ''' + sqlLeftTable + '''
        ([Field])
      VALUES
        ([Value])
      RETURNING
        "Node_MNID"
      ''',
      *LData.items()
      )

    RData['Node_MNID'] = pk[0]

    App.DB.Execute('''
      INSERT INTO 
        ''' + sqlRightTable + '''
        ([Field])
      VALUES
        ([Value])
      ''',
      *RData.items()
      )

    return pk
  

  #============================================================================
  def UPDATE(self, data):
    fields = set(data)
    
    # Left fields are the ones that match the Left Field list
    LF = set.intersection(LField, fields)   
    LData = {k:data[k] for k in data if k in LF}

    # Right fields are the remaining ones that do not match the (left fields - shared fields)
    RF = set.difference(fields, set.difference(LField, RField))
    RData = {k:data[k] for k in data if k in RF}
    
    if LData:
      App.DB.Execute('''
        UPDATE 
          ''' + sqlLeftTable + '''
        SET
          [Field=Value]
        WHERE True
          ''' + sqlWhere + '''
        ''',
        *LData.items(),
        pk0 = self.PrimaryKey[0]
        )
    
    if RData:
      App.DB.Execute('''
        UPDATE 
          ''' + sqlRightTable + '''
        SET
          [Field=Value]
        WHERE True
          ''' + sqlWhere + '''
        ''',
        *RData.items(),
        pk0 = self.PrimaryKey[0]
        )
  
  #============================================================================
  def DELETE(self):
    App.DB.Execute('''
      DELETE FROM  
        ''' + sqlLeftTable + '''
      WHERE True
        ''' + sqlWhere + '''
      ''',
      pk0 = self.PrimaryKey[0]
      )
    
    App.DB.Execute('''
      DELETE FROM  
        ''' + sqlRightTable + '''
      WHERE True
        ''' + sqlWhere + '''
      ''',
      pk0 = self.PrimaryKey[0]
      )

  return SELECT, INSERT, UPDATE, DELETE


