/*
vim:encoding=utf-8:ts=2:sw=2:expandtab
*/

define([
    'exports',
    'module',
    'AppStruct/Util'
  ], 
  function(
    App,
    module,
    Util
  ){
  
  //This is to support in python:
  //  self.UI.JSData.Foo = 10;
  //Access in JS by:
  //  App.Data.Foo
  App.Data = module.config();
  
  // AppToken is passed as part of RequireJS config
  //  App.AppToken = module.config().AppToken;

  // An object of handelers to be called on Post ops which return this Type.
  App.PostHandlers = {
    Success: function(data) {console.log(data);}
  };
  
  // Application specific POST function
  App.Post = function(URI, Data, Handlers) {
    var post = {
      AppToken: App.AppToken,
      Data: JSON.stringify(Data)
    };

    $.post(URI, post, function(data){
      var h;
      if(h = Handlers[data.Type]) {  // yes, an assignment
        h(data.Data);
      }
      else if(h = App.PostHandlers[data.Type]) {
        h(data.Data);
      }
      else {
        alert('Ajax call failed.');
        console.log(data);
      }
    });
  };



  /////////////////////////////////////////////////////////////////////////////
});
