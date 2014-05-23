// Generated by CoffeeScript 1.7.1
(function() {
  $(document).on('ready', function() {
    var alertMessage, author_path, mapCanvas, query;
    if (location.search === '?modal=1') {
      $('#mapmodal').modal();
    }
    if (window.SCENES) {
      author_path = '/map/filter/author/';
      query = decodeURIComponent(window.location.pathname.replace(author_path, ''));
      if (window.SCENES.length === 0) {
        mapCanvas = new PlacingLit.Views.MapCanvasView;
        alertMessage = 'Whoa! No places found for ' + query + '. ';
        alertMessage += 'But that\'s ok!. Be the first to map this author. ';
        alertMessage += 'Click the map to add a book and author.';
        alert(alertMessage);
      } else {
        mapCanvas = new PlacingLit.Views.MapFilterView(window.SCENES);
        if (window.location.pathname.indexOf('filter') !== -1) {
          $('#querymodal').modal();
        }
      }
    } else {
      mapCanvas = new PlacingLit.Views.MapCanvasView;
    }
    if (!Modernizr.input.placeholder) {
      mapCanvas.handleInputAttributes();
    }
    return mapCanvas.showInfowindowFormAtLocation();
  });

}).call(this);
