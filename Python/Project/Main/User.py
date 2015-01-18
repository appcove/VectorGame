# vim:encoding=utf-8:ts=2:sw=2:expandtab

from AppStruct.Base.V1 import *
from AppStruct.Security import SHA1, RandomHex
from Project import *
from Project.Base import MakeSIUD

#==============================================================================
def UsernameExists(Username = None):
  return App.DB.Bool('''
    SELECT COUNT(*) = 1 
    FROM "Main"."User"
    WHERE "Login_Username" = $Username
    ''',
    Username = Username,
    )

#============================================================================
def List():
  return [User(r) for r in 
    App.DB.ValueList('''
      SELECT
        "User_MNID"
      FROM
        "Main"."User"
      ORDER BY
        "Name"
      '''
      )
    ]
###############################################################################
class User(metaclass=MetaRecord):
  PrimaryKeyFields = ['User_MNID']
  SELECT,INSERT,UPDATE,DELETE = MakeSIUD('Main', 'User', *PrimaryKeyFields)

  class User_MNID(Integer): 
    Flags = +Read
    Label = 'User'

  class CreateDate(Datetime):
    Flags = +UpdateRead  
    @property
    def InsertDefault(self):
      return SQL('NOW()')

  class FirstName(String):
    Flags = +Read +Write +InsertRequired
    MaxLength = 70
    Label = 'Name'

  class LastName(String):
    Flags = +Read +Write +InsertRequired
    MaxLength = 70
    Label = 'Name'

  @property
  def Name(self):
    return "{0} {1}".format(self.FirstName, self.LastName)
  class Email(String):
    Flags = +Read +Write +InsertRequired 
    MaxLength = 100
    Label = 'Primary Email'
        
  class Phone(String):
    Flags = +Read +Write +InsertRequired 
    MaxLength = 20
    Label = 'Phone'


  class Login_Username(String):
    Flags = +Write +Read
    MaxLength = 40
    Label = 'User Name'
    AllowEmpty = True
    AllowNone = True
    def Validate(self, record, fv):
      fv.value = fv.value.lower()
      if not String.Validate(self, record, fv):
        return False
      
      if fv.value == '':
        fv.value = None
        
      if fv.value != '' and App.DB.Bool('''
        SELECT EXISTS
        (
          SELECT 
            True
          FROM
            "Main"."User" 
          WHERE True
            AND lower("Login_Username") = lower($A)
            AND "User_MNID" != COALESCE($B, 0)
        )
        ''',
        A = fv.value,
        B = record._User_MNID,
        ):
        fv.AddError("Username '{un}' already in use.", un=fv.value)
        return False
      return True

  class Login_Password_Hash(String):
    Flags = +Read +Write
    MaxLength = 40

  class Login_Password(String):
    Flags = +Read +Write +Virtual
    MaxLength = 40
    AllowNone = True
    AllowEmpty = False
    Label = 'Password '
    def Validate(self, record, fv):
      if not String.Validate(self, record, fv):
        return False
      
      if fv.value is None:
        record.Login_Password_Hash = None
      else:
        record.Login_Password_Hash = SHA1(fv.value + str(record.Login_Password_Salt)) #todo, salt should not be Nullable
      
      return True

  class Login_Password_Salt(String):
    Flags = +Read +Write 
    AllowNone = False
    MinLength = 60
    MaxLength = 60
    @property
    def InsertValue(self):
      return RandomHex()[:60]

  class Perm_Active(Boolean):
    Flags = +Read +Write
    Label = 'Status'
    InsertDefault = True

  class Perm_Super(Boolean):
    Flags = +Read +Write
    InsertDefault = False
    
###############################################################################
def SaltAndHashPassword(Username, Password):
  Salt = App.DB.Value('''
    SELECT 
      "Login_Password_Salt"
    FROM  
      "Main"."User"
    WHERE true
      AND "Login_Username" = $A
    ''',
    A = Username,
    )
  return SHA1(Password + Salt)

###############################################################################
def AuthenticateByUsernameAndPassword(Username, Password):
  '''
  Returns a User_MNID in the event that the authentication was successful
  '''
  try:
    Password_Hash = SaltAndHashPassword(Username, Password)
    User_MNID = App.DB.Value('''
      SELECT 
        "User_MNID"
      FROM  
        "Main"."User"
      WHERE true
        AND "Login_Username" = $A
        AND "Login_Password_Hash" = $B
      ''',
      A = Username,
      B = Password_Hash,
      )
  except App.DB.NotOneFound:
    raise AuthenticationError('Invalid Username or Password')

  return User_MNID

