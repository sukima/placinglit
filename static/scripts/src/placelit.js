// Generated by CoffeeScript 1.7.1
(function() {
  $(document).on('ready', function() {
    var alertMessage, mapCanvas, query;
    if (location.search === '?modal=1') {
      $('#mapmodal').modal();
    }
    if (window.SCENES) {
      query = decodeURIComponent(window.location.pathname.replace('/map/filter/author/', ''));
      if (window.SCENES.length === 0) {
        mapCanvas = new PlacingLit.Views.MapCanvasView;
        alertMessage = 'Whoa! No places found for ' + query + '. ';
        alertMessage += 'But that\'s ok!. Be the first to map this author. ';
        alertMessage += 'Click the map to add a book and author.';
        alert(alertMessage);
      } else {
        $('#querymodal').modal();
        mapCanvas = new PlacingLit.Views.MapFilterView(window.SCENES);
      }
    } else {
      mapCanvas = new PlacingLit.Views.MapCanvasView;
    }
    if (!Modernizr.input.placeholder) {
      mapCanvas.handleInputAttributes();
    }
    mapCanvas.showInfowindowFormAtLocation();
    return mapCanvas.handleAllScenesClick();
  });

}).call(this);
