// Generated by CoffeeScript 1.7.1
(function() {
  $(document).on('ready', function() {
    var authorfield, countView, gcfield, hpAuthorSearch, hpCitySearch, hpSuggestAuthors, positionError, recentPlacesView, updateMapLinksWithLocation, updateMapLinksWithUserLocation;
    hpCitySearch = function() {
      var address, geocoder;
      address = gcfield.value;
      geocoder = new google.maps.Geocoder();
      return geocoder.geocode({
        'address': address
      }, (function(_this) {
        return function(results, status) {
          var lat, lng, mapUrl, position;
          if (status === google.maps.GeocoderStatus.OK) {
            position = results[0].geometry.location;
            lat = position[Object.keys(position)[0]];
            lng = position[Object.keys(position)[1]];
            mapUrl = window.location.protocol + '//' + window.location.host;
            mapUrl += '/map/' + lat + ',' + lng;
            return window.location = mapUrl;
          } else {
            return alert("geocode was not successful: " + status);
          }
        };
      })(this));
    };
    hpAuthorSearch = function() {
      var authorq, mapUrl;
      authorq = authorfield.value;
      mapUrl = window.location.protocol + '//' + window.location.host;
      mapUrl += '/map/filter/author/' + authorq;
      return window.location = mapUrl;
    };
    hpSuggestAuthors = function() {
      var author_data;
      author_data = [];
      return $.ajax({
        url: "/places/authors",
        success: function(data) {
          $.each(data, function(key, value) {
            return author_data.push(value.author.toString());
          });
          return $('#authorq').typeahead({
            source: author_data
          });
        }
      });
    };
    updateMapLinksWithLocation = function(position) {
      var lat, lng;
      lat = position.coords.latitude;
      lng = position.coords.longitude;
      return $('#hpbuttons').find('a').attr('href', 'map?lat=' + lat + '&lng=' + lng);
    };
    positionError = function(error) {
      console.log('error', error);
      return console.log('client ip', window.REMOTE_ADDR);
    };
    updateMapLinksWithUserLocation = function() {
      if (navigator.geolocation) {
        return navigator.geolocation.getCurrentPosition(updateMapLinksWithLocation, positionError);
      }
    };
    hpSuggestAuthors();
    recentPlacesView = new PlacingLit.Views.RecentPlaces;
    countView = new PlacingLit.Views.Countview;
    $('.carousel').carousel();
    gcfield = document.getElementById('gcf');
    gcfield.addEventListener('keydown', (function(_this) {
      return function(event) {
        if (event.which === 13 || event.keyCode === 13) {
          event.preventDefault();
          return hpCitySearch();
        }
      };
    })(this));
    authorfield = document.getElementById('authorq');
    return authorfield.addEventListener('keydown', (function(_this) {
      return function(event) {
        if (event.which === 13 || event.keyCode === 13) {
          event.preventDefault();
          return hpAuthorSearch();
        }
      };
    })(this));
  });

}).call(this);
