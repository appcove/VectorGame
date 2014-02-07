# vim:encoding=utf-8:ts=2:sw=2:expandtab

from Project import *


def UI_text(data, field, label, classes = None, placeholder=''):
  if hasattr(data, field):
    val = getattr(data, field)
  else:
     val = data[field]
  return '''
    <div class="form-group">
      <label class="col-sm-4 control-label" for=''' + QA(field) + ''' >''' + HS(label) + ''':</label>
      <div class="col-sm-8">
        <input type="text" class="form-control" name=''' + QA(field) + ''' id=''' + QA(field) + ''' value=''' + QA(val) + ''' ''' + ('placeholder='+QA(placeholder) if placeholder else '') + '''>
      </div>
    </div>
    '''

def UI_text_hidden(data, field, label, classes = None, placeholder=''):
  if hasattr(data, field):
    val = getattr(data, field)
  else:
    val = data[field]
  return '''
    <div class="form-group" style="display: none; height: 1px; width: 1px">
      <label class="col-sm-4 control-label" for=''' + QA(field) + ''' >''' + HS(label) + ''':</label>
      <div class="col-sm-8">
        <input type="text"  class="form-control" style="display: none" name=''' + QA(field) + ''' id=''' + QA(field) + ''' value=''' + QA(val) + ''' ''' + ('placeholder='+QA(placeholder) if placeholder else '') + '''>
      </div>
    </div>
    '''

def UI_editable(data, field, label, classes = None, placeholder=''):
  return '''
    <div class="form-group">
      <label class="col-sm-4 control-label" for=''' + QA(field) + ''' >''' + HS(label) + ''':</label>
      <div class="col-sm-8">
        <input type="text" class="form-control" style="background-color: #dcdcdc; color: #595959"  name=''' + QA(field) + ''' id=''' + QA(field) + ''' value=''' + QA(data[field]) + ''' ''' + ('placeholder='+QA(placeholder) if placeholder else '') + '''>
      </div>
    </div>
    '''

def UI_note_grayed(text, label):
  return '''
    <div class="form-group">
      <label class="col-sm-4 control-label">''' + HS(label) + ''':</label>
      <div class="col-sm-8">
        <span class="form-control" style="display: inline-block; height: auto; min-height: 34px; background-color: #dcdcdc; color: #595959">''' + HS(text) + '''</span>
      </div>
    </div>
    '''

def UI_note(text, label):
  return '''
    <div class="form-group">
      <label class="col-sm-4 control-label">''' + HS(label) + ''':</label>
      <div class="col-sm-8">
        <span class="form-control" style="display: inline-block; height: auto; min-height: 34px;">''' + HS(text) + '''</span>
      </div>
    </div>
    '''


def UI_textarea(data, field, label):
  if hasattr(data, field):
    val = getattr(data, field)
  else:
    val = data[field]
  return '''
    <div class="form-group">
      <label class="col-sm-4 control-label" for=''' + QA(field) + ''' >''' + HS(label) + ''':</label>
      <div class="col-sm-8">
        <textarea class="form-control" name=''' + QA(field) + ''' id=''' + QA(field) + '''>''' + HS(val) + '''</textarea>
      </div>
    </div>
    '''

def UI_textarea_grayed(data, field, label):
  if hasattr(data, field):
    val = getattr(data, field)
  else:
    val = data[field]
  return '''
    <div class="form-group">
      <label class="col-sm-4 control-label" for=''' + QA(field) + ''' >''' + HS(label) + ''':</label>
      <div class="col-sm-8">
        <textarea rows="4" disabled class="form-control" style="display: inline-block; height: auto; min-height: 34px; resize: none; cursor:default; background-color: #dcdcdc; color: #595959"'  name=''' + QA(field) + ''' id=''' + QA(field) + '''>''' + HS(val) + '''</textarea>
      </div>
    </div>
    '''


def UI_select(data, field, label, *, SelectMap, EmptyLabel = None, classes = None):
  if hasattr(data, field):
    val = getattr(data, field)
  else:
    val = data[field]
  return '''
    <div class="form-group">
      <label class="col-sm-4 control-label" for=''' + QA(field) + '''>''' + HS(label) + ''':</label>
      <div class="col-sm-8">
        <select class="form-control" name=''' + QA(field) + ''' id=''' + QA(field) + '''>
          <option value="">''' + (HS(EmptyLabel) if EmptyLabel else '') + '''</option>
          ''' + JN('<option value=' + QA(k) + ' ' + ('selected' if str(k) == str(val) else '') + '>' + HS(v) + '</option>' for k, v in SelectMap.items()) + '''
        </select>
      </div>
    </div>
    '''

def UI_password(data, field, label):
  if hasattr(data, field):
    val = getattr(data, field)
  else:
    val = data[field]

  return '''
    <div class="form-group">
      <label class="col-sm-4 control-label">''' + HS(label) + ''':</label>
      <div class="col-sm-8">
        <input type="password" class="form-control" name=''' + QA(field) + ''' value=''' + QA(val) + '''>
      </div>
    </div>
    '''

def UI_checkbox(data, field, label, desc = None, classes = None):
  if hasattr(data, field):
    val = getattr(data, field)
  else:
    val = data[field]
  return '''
    <div class="checkbox ''' + (classes if classes else '') + '''">
      <label>
        <input type="checkbox" name=''' + QA(field) + (' checked="checked"' if val else '') + '''>
        <strong>
          ''' + HS(label) + '''
        </strong>
      </label>
      <p>
        ''' + (HS(desc) if desc else '') + '''
      </p>
    </div>
    '''

def UI_checkbox_disabled(data, field, label, desc = None, classes = None):
  if hasattr(data, field):
    val = getattr(data, field)
  else:
    val = data[field]
  return '''
    <div class="checkbox ''' + (classes if classes else '') + '''">
      <label>
        <input disabled type="checkbox" name=''' + QA(field) + (' checked="checked"' if val else '') + '''>
        <strong>
          ''' + HS(label) + '''
        </strong>
      </label>
      <p>
        ''' + (HS(desc) if desc else '') + '''
      </p>
    </div>
    '''

def UI_field(data, fmfield, **kwargs):
  if fmfield.Type == 'select':
    return UI_select(data, fmfield.Name, fmfield.Label, SelectMap = fmfield.SelectMap, **kwargs)
  elif fmfield.Type == 'text':
    return UI_text(data, fmfield.Name, fmfield.Label, **kwargs)
  elif fmfield.Type == 'textarea':
    return UI_textarea(data, fmfield.Name, fmfield.Label, **kwargs)
  else: 
    raise ValueError('Invalid field type for `UI_Field` function: ' + str(fmfield.Type))


