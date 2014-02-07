
            
            var newCircle1 = new Path.Circle({
                center: new Point(100,100),
                radius: 100,
                fillColor: 'blue',
                strokeColor: 'black',
                strokeWidth: 2,
                data: {ThisIsAMakerCircle: true}
              });
              
            var newCircle2 = new Path.Circle({
                center: new Point(300,100),
                radius: 100,
                fillColor: 'red',
                strokeColor: 'black',
                strokeWidth: 2,        
                data: {ThisIsAMakerCircle: true}
              });
            var newCircle3 = new Path.Circle({
                center: new Point(500,100),
                radius: 100,
                fillColor: 'yellow',
                strokeColor: 'black',
                strokeWidth: 2,        
                data: {ThisIsAMakerCircle: true}
              });
            var newCircle4 = new Path.Circle({
                center: new Point(700,100),
                radius: 100,
                fillColor: 'green',
                strokeColor: 'black',
                strokeWidth: 2,        
                data: {ThisIsAMakerCircle: true}
              });

              
                // These two variables store the selected item when dragging across the screen.
            var selectedItem = null;
            var selectedItemOffset = null;
            
            // This checks if you click down on an empty space or an existing item.
            function onMouseDown(event) {
              // Are we clicking the new circle?
              if(event.item && event.item.data.ThisIsAMakerCircle) {
                // Create a new circle and make it selected
                selectedItem = new Path.Circle({
                  center: event.item.position,
                  radius: 100,
                  fillColor: event.item.fillColor,
                  strokeColor: event.item.strokeColor,
                  strokeWidth: 2        
                });
                selectedItemOffset = selectedItem.position - event.point;
              }
              // Are we clicking an existing circle?
              else if(event.item) {
                selectedItem = event.item;
                selectedItemOffset = selectedItem.position - event.point;
              }
              else {
                // Do nothing
              }
            };
            
            function onMouseUp(event) {
              selectedItem = null;
              selectedItemOffset = null;
            };
    
            function onMouseDrag(event) {
              // If we are dragging with a selected item, then move it.
              if(selectedItem) {
                selectedItem.position = event.point + selectedItemOffset;
              }
              // But if we just drag over another item, then remove it
              else if(event.item) {
                // Only remove it if it is NOT (!) a Maker Circle
                if(! event.item.data.ThisIsAMakerCircle) {
                  event.item.remove();
                }
              }
            };
