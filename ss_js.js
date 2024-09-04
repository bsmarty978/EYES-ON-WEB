// This will create a global variable to store the coordinates
window.selectedRegion = null;

var startX, startY, endX, endY;
var box = document.createElement('div');
box.style.border = '2px dashed red';
box.style.position = 'absolute';
box.style.zIndex = '10000';
document.body.appendChild(box);

function onMouseDown(event) {
    startX = event.clientX;
    startY = event.clientY;
    box.style.left = startX + 'px';
    box.style.top = startY + 'px';
    box.style.width = '0px';
    box.style.height = '0px';
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
}

function onMouseMove(event) {
    var width = event.clientX - startX;
    var height = event.clientY - startY;
    box.style.width = Math.abs(width) + 'px';
    box.style.height = Math.abs(height) + 'px';
    box.style.left = (width > 0 ? startX : startX + width) + 'px';
    box.style.top = (height > 0 ? startY : startY + height) + 'px';
}

function onMouseUp(event) {
    endX = event.clientX;
    endY = event.clientY;
    
    // Store the coordinates in a global variable for later access by Selenium
    window.selectedRegion = {
        startX: startX,
        startY: startY,
        endX: endX,
        endY: endY
    };
    
    // Clean up the event listeners
    document.removeEventListener('mousemove', onMouseMove);
    document.removeEventListener('mouseup', onMouseUp);
}

// Attach the event listener
document.addEventListener('mousedown', onMouseDown);
