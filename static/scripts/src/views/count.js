// Generated by CoffeeScript 1.7.1
(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  PlacingLit.Views.Countview = (function(_super) {
    __extends(Countview, _super);

    function Countview() {
      return Countview.__super__.constructor.apply(this, arguments);
    }

    Countview.prototype.el = '#count';

    Countview.prototype.initialize = function() {
      this.model = new PlacingLit.Models.Metadata;
      this.model.fetch({
        url: '/places/count'
      });
      return this.listenTo(this.model, 'all', this.render);
    };

    Countview.prototype.render = function(event) {
      if (event === 'change:count') {
        return this.showCount();
      }
    };

    Countview.prototype.showCount = function() {
      return $(this.el).text(this.model.get('count') + ' scenes have been mapped');
    };

    return Countview;

  })(Backbone.View);

}).call(this);
