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

  
  var xpath = new paper.Path.Rectangle([75, 75], [100, 100]);
  xpath.strokeColor = 'black';
  xpath.fillColor = 'blue';

  paper.view.onFrame = function(event) {
    xpath.rotate(.5);
    xpath.fillColor.hue += .5;
  };

  var path = null;
  var cir = null;
  var hue = 0;

  var tool = new paper.Tool();
  tool.onMouseDown = function(event) {
    if(path) {
      if(cir.position.isClose(event.point, 10)) {
        path.add(cir.position);
        path.fillColor = 'blue';
        hue += 10;
        path.fillColor.hue += hue;
        cir.remove();
        cir = null;
        path = null;
      }
      else {
        path.add(event.point);
      };
    }
    else {
      cir = paper.Path.Circle(event.point, 10);
      cir.fillColor = 'red';
      
      path = new paper.Path();
      path.strokeColor = 'black';
      path.add(event.point);
    }
  };


  // Draw the view now:
  paper.view.draw();


});

