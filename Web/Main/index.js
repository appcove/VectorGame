/* 
vim:encoding=utf-8:ts=2:sw=2:expandtab 
*/

define(['exports', 'App'], function(self, App) {


  // Get a reference to the canvas object
  var canvas = document.getElementById('canvas');
  // Create an empty project and a view for the canvas:
  paper.setup(canvas);
  
  // Create a Paper.js Path to draw a line into it:
  var path = new paper.Path();
  // Give the stroke a color
  path.strokeColor = 'black';
  
  
  _.each(App.Data.PlayerList, function(row) {
    var c = paper.Path.Circle(row.Location_Current, 10);
    c.setFillColor(row.Color);
    

  });

  
  // Draw the view now:
  paper.view.draw();


});

