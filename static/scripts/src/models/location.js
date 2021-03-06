// Generated by CoffeeScript 1.7.1
(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  PlacingLit.Models.Location = (function(_super) {
    __extends(Location, _super);

    function Location() {
      return Location.__super__.constructor.apply(this, arguments);
    }

    Location.prototype.defaults = {
      title: 'Put Title Here',
      author: 'Someone\'s Name goes here'
    };

    Location.prototype.url = '/places/add';

    return Location;

  })(Backbone.Model);

  PlacingLit.Collections.Locations = (function(_super) {
    __extends(Locations, _super);

    function Locations() {
      return Locations.__super__.constructor.apply(this, arguments);
    }

    Locations.prototype.model = PlacingLit.Models.Location;

    Locations.prototype.url = '/places/show';

    Locations.prototype.initialize = function() {
      return this.on('add', function(model) {
        return alert('adding model');
      });
    };

    return Locations;

  })(Backbone.Collection);

}).call(this);
