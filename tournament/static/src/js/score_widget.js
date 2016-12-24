odoo.define('tournament.score', function (require) {
"use strict";

// var core = require('web.core');
var kanban_widgets = require('web_kanban.widgets');
// var formats = require('web.formats');
// var Model = require('web.Model');

// var QWeb = core.qweb;

var MatchScoreWidget = kanban_widgets.AbstractField.extend({
    // init: function(parent, field, $node) {
    //     this._super.apply(this, arguments);
    //     this.set("value", field.raw_value);
    // },
    // renderElement: function() {
    //     var digits_precision = this.options.digits || session.weight_uom.digits;
    //     var value = formats.format_value(this.field.raw_value * session.weight_uom.factor || 0, {type: "float", digits: digits_precision}, '0');
    //     value += ' ' + session.weight_uom.name;
    //     this.$el.text(value);
    // }
    renderElement: function() {
        var self = this;
        // this.$el.addClass('container');
        var score = JSON.parse(this.get('value')) || [];
        score.forEach(
            function(set) {
                self.$el.append(
                    '<div class="row">' +
                        '<div class="col-xs-2 col-xs-offset-3">'
                            + set[0].toString() +
                        '</div>' +
                        '<div class="col-xs-1"> - </div>' +
                        '<div class="col-xs-2">'
                            + set[1].toString() +
                        '</div>'+
                    '</div>');
            });
    },
});

kanban_widgets.registry.add('match_score', MatchScoreWidget);

});