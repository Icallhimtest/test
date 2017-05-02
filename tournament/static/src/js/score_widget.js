odoo.define('tournament.score', function (require) {
"use strict";

// var core = require('web.core');
var basicFields = require('web.basic_fields');
var fieldRegistry = require('web.field_registry');
var AbstractField = require('web.AbstractField');
// var formats = require('web.formats');
// var Model = require('web.Model');

// var QWeb = core.qweb;

var FieldScore = basicFields.DebouncedField.extend({
    className: 'o_field_score o_list_number',
    supportedFieldTypes: ['char', 'text'],
    events: _.extend({}, AbstractField.prototype.events, {
        'change input': '_evaluate_score',
    }),

    /**
     * Float fields using a monetary widget have an additional currency_field
     * parameter which defines the name of the field from which the currency
     * should be read.
     *
     * They are also displayed differently than other inputs in
     * edit mode. They are a div containing a span with the currency symbol and
     * the actual input.
     *
     * If no currency field is given or the field does not exist, we fallback
     * to the default input behavior instead.
     *
     * @override
     */
    init: function (options) {
        this._super.apply(this, arguments);

        this.score = JSON.parse(this.value) || [];
        this.points_per_set = this.record.data.points_per_set;
        this.sets_to_win = this.record.data.sets_to_win;

        if (this.mode === 'edit') {
            this.tagName = 'div';
        }
    },

    //--------------------------------------------------------------------------
    // Public
    //--------------------------------------------------------------------------

    /**
     * For monetary fields, 0 is a valid value.
     *
     * @override
     */
    isSet: function () {
        if (this.score.length === 0) {
            return false
        }
        return this._super.apply(this, arguments);
    },
    /**
     * This function should be implemented by widgets that are not able to
     * notify their environment when their value changes (maybe because their
     * are not aware of the changes). It is called before saving, and should
     * call _setValue() to notify the environment if the value changed.
     *
     * @abstract
     */
    commitChanges: function () {
        this._setValue(this._getValue());
    },
    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * trash management :D
     *
     * @private
     * @returns {value} the content of the input
     */
    _evaluate_score: function () {
        var input_scores = this.$el.find('input')
        var player1won = 0;
        var player2won = 0;
        this.score = this._getValue(); // CLEAN NEXT PART USING this.score ! and call _setValue !   
        for (var i=0; i<input_scores.length/2; i++) {
            //auto-fill the other score value if not set
            if($(input_scores[2*i]).val().length && ! $(input_scores[2*i+1]).val().length) {
                $(input_scores[2*i+1]).val(Math.max(this.points_per_set, parseInt($(input_scores[2*i]).val())+2).toString());
            } else if(! $(input_scores[2*i]).val().length && $(input_scores[2*i+1]).val().length) {
                $(input_scores[2*i]).val(Math.max(this.points_per_set, parseInt($(input_scores[2*i+1]).val())+2).toString());
            } else if (parseInt($(input_scores[2*i]).val()) < parseInt($(input_scores[2*i+1]).val())) {
                player2won++;
            } else if (parseInt($(input_scores[2*i]).val()) > parseInt($(input_scores[2*i+1]).val())) {
                player1won++;
            } else {
                return false; // error score 1 = score 2
            }
            if (Math.max(player1won, player2won) == this.sets_to_win && input_scores.length > 2*(i+1)) {
                this.$el.find('div.row').slice(i+1).remove();
                break;
            }
        }
        console.log('player1won ' + player1won);
        console.log('player2won ' + player2won);
        if (Math.max(player1won, player2won) < this.sets_to_win) {
            this.$el.append(
                '<div class="row">' +
                    '<input type="number" style="width:16.666667%" class="col-xs-2 col-xs-offset-3">'
                        +
                    '</input>' +
                    '<div class="col-xs-1"> - </div>' +
                    '<input type="number" style="width:16.666667%" class="col-xs-2">'
                        +
                    '</input>'+
                '</div>');
            return false;
        }
        return true;
    },
    /**
     * @override
     * @returns {array} the content of the input
     */
    _getValue: function () {
        var input_scores = this.$el.find('input')
        var score = [];
        for (var i=0; i<input_scores.length; i++) {
            if (!(i%2)) {
                score[i/2] = [parseInt($(input_scores[i]).val()), undefined];
            } else {
                score[(i-1)/2][1] = parseInt($(input_scores[i]).val());
            }
        }
        return score;
    },
    /**
     * this method is called by the widget, to change its value and to notify
     * the outside world of its new state.  This method also validates the new
     * value.  Note that this method does not rerender the widget, it should be
     * handled by the widget itself, if necessary.
     *
     * @private
     * @param {any} value
     */
    _setValue: function (value) {
        // we try to avoid doing useless work, if the value given has not
        // changed.  Note that we compare the unparsed values.
        if (this.lastSetValue === value || (value !== false && value === this.value)) {
            return;
        }
        this.lastSetValue = value;
        this.value = this._getValue();
        var changes = {};
        changes[this.name] = JSON.stringify(this.value);
        this.trigger_up('field_changed', {
            dataPointID: this.dataPointID,
            changes: changes,
        });

    },
    /**
     * For monetary fields, the input is inside a div, alongside a span
     * containing the currency symbol.
     *
     * @override
     * @private
     */
    _renderEdit: function () {
        var self = this;
        this.$el.empty();
        // Prepare and add the inputs
        this.score.forEach(
            function(set) {
                self.$el.append(
                    '<div class="row">' +
                        '<input type="number" style="width:16.666667%;text-align:center;" class="col-xs-2 col-xs-offset-3">' +
                        '</input>' +
                        '<div class="col-xs-1"> - </div>' +
                        '<input type="number" style="width:16.666667%;text-align:center;" class="col-xs-2">' +
                        '</input>'+
                    '</div>');
            });
        var input_scores = this.$el.find('input')
        for (var i=0; i<input_scores.length/2; i++) {
            $(input_scores[2*i]).val(this.score[i][0].toString());
            $(input_scores[2*i+1]).val(this.score[i][1].toString());
        }
        this._evaluate_score();
    },
    /**
     * For monetary fields, the input is inside a div, alongside a span
     * containing the currency symbol.
     *
     * @override
     * @private
     */
    _renderReadonly: function () {
        var self = this;
        this.$el.empty();
        this.score.forEach(
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

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * might be controversial: intercept the tab key, to allow the editable list
     * view to control where the focus is.
     *
     * @private
     * @param {KeyEvent} event
     */
    _onKeydown: function (event) {
        if (event.which === $.ui.keyCode.ENTER) {
            // the event needs to be stopped, to prevent other field widgets
            // to retrigger a move event
            event.stopPropagation();
            if (this._evaluate_score()) {
                this.trigger_up('move_next');
            }
            event.preventDefault();
        }
    },
});

fieldRegistry.add('score', FieldScore);

});