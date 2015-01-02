/* 
vim:encoding=utf-8:ts=2:sw=2:expandtab 
*/

define(['exports', 'App'], function(self, App) {

  // Get a reference to the canvas object
  var canvas = document.getElementById('canvas');
  
  // Create an empty project and a view for the canvas:
  paper.setup(canvas);

  // Setup the canvas to 
  function ResizeCanvas() {
    paper.view.viewSize = [window.innerWidth-300, window.innerHeight];
  }
  $(window).resize(ResizeCanvas);
  ResizeCanvas();
  
  var xcircle = new paper.Path.Circle([74,74], 72);
  xcircle.strokeColor = 'black';
  xcircle.fillColor = "#ccc";
  
  var xpath = new paper.Path.Rectangle([24, 24], [100, 100]);
  xpath.strokeColor = 'black';
  xpath.fillColor = 'blue';

  var xrotate = .5;
  var xaccel = xrotate * 1.256;
  var xcolor = 1;

  paper.view.onFrame = function(event) {
    if(xcircle.strokeBounds.right > paper.view.size.width || xcircle.strokeBounds.left < 0) {
      xaccel = -xaccel;
      xrotate = -xrotate;
    }

    xpath.rotate(xrotate);
    xpath.fillColor.hue += xcolor;
    xpath.position.x += xaccel;
    xcircle.position.x += xaccel;
  };

  var path = null;
  var cir = null;

  var tool = new paper.Tool();
  tool.onMouseDown = function(event) {
    if(path) {
      if(cir.position.isClose(event.point, 10)) {
        path.add(cir.position);
        path.fillColor = cir.fillColor;
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
      cir.fillColor = xpath.fillColor;
      
      path = new paper.Path();
      path.strokeColor = 'black';
      path.add(event.point);
    }
  };


  // Draw the view now:
  paper.view.draw();


});

