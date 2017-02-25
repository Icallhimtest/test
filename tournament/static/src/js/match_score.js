odoo.define('tournament.match_score', function (require) {
"use strict";

var core = require('web.core');
var Model = require('web.Model');
var Widget = require('web.Widget');

var QWeb = core.qweb;
var _t = core._t;


var MatchScore = Widget.extend({
    events: {
        'change input': function(){ this.evaluate_score();},
    },
    // events: {
    //     "click .o_hr_attendance_back_button": function () { this.do_action(this.next_action, {clear_breadcrumbs: true}); },
    //     "click .o_hr_attendance_sign_in_out_icon": function () {
    //         var self = this;
    //         this.$('.o_hr_attendance_sign_in_out_icon').attr("disabled", "disabled");
    //         var hr_employee = new Model('hr.employee');
    //         hr_employee.call('attendance_manual', [[this.employee_id], this.next_action])
    //         .then(function(result) {
    //             if (result.action) {
    //                 self.do_action(result.action);
    //             } else if (result.warning) {
    //                 self.do_warn(result.warning);
    //                 self.$('.o_hr_attendance_sign_in_out_icon').removeAttr("disabled");
    //             }
    //         });
    //     },
    //     'click .o_hr_attendance_pin_pad_button_0': function() { this.$('.o_hr_attendance_PINbox').val(this.$('.o_hr_attendance_PINbox').val() + 0); },
    //     'click .o_hr_attendance_pin_pad_button_1': function() { this.$('.o_hr_attendance_PINbox').val(this.$('.o_hr_attendance_PINbox').val() + 1); },
    //     'click .o_hr_attendance_pin_pad_button_2': function() { this.$('.o_hr_attendance_PINbox').val(this.$('.o_hr_attendance_PINbox').val() + 2); },
    //     'click .o_hr_attendance_pin_pad_button_3': function() { this.$('.o_hr_attendance_PINbox').val(this.$('.o_hr_attendance_PINbox').val() + 3); },
    //     'click .o_hr_attendance_pin_pad_button_4': function() { this.$('.o_hr_attendance_PINbox').val(this.$('.o_hr_attendance_PINbox').val() + 4); },
    //     'click .o_hr_attendance_pin_pad_button_5': function() { this.$('.o_hr_attendance_PINbox').val(this.$('.o_hr_attendance_PINbox').val() + 5); },
    //     'click .o_hr_attendance_pin_pad_button_6': function() { this.$('.o_hr_attendance_PINbox').val(this.$('.o_hr_attendance_PINbox').val() + 6); },
    //     'click .o_hr_attendance_pin_pad_button_7': function() { this.$('.o_hr_attendance_PINbox').val(this.$('.o_hr_attendance_PINbox').val() + 7); },
    //     'click .o_hr_attendance_pin_pad_button_8': function() { this.$('.o_hr_attendance_PINbox').val(this.$('.o_hr_attendance_PINbox').val() + 8); },
    //     'click .o_hr_attendance_pin_pad_button_9': function() { this.$('.o_hr_attendance_PINbox').val(this.$('.o_hr_attendance_PINbox').val() + 9); },
    //     'click .o_hr_attendance_pin_pad_button_C': function() { this.$('.o_hr_attendance_PINbox').val(''); },
    //     'click .o_hr_attendance_pin_pad_button_ok': function() {
    //         var self = this;
    //         this.$('.o_hr_attendance_pin_pad_button_ok').attr("disabled", "disabled");
    //         var hr_employee = new Model('hr.employee');
    //         hr_employee.call('attendance_manual', [[this.employee_id], this.next_action, this.$('.o_hr_attendance_PINbox').val()])
    //         .then(function(result) {
    //             if (result.action) {
    //                 self.do_action(result.action);
    //             } else if (result.warning) {
    //                 self.do_warn(result.warning);
    //                 setTimeout( function() { self.$('.o_hr_attendance_pin_pad_button_ok').removeAttr("disabled"); }, 500);
    //             }
    //         });
    //     },
    // },

    init: function (parent, action) {
        this._super.apply(this, arguments);
        // this.next_action = 'hr_attendance.hr_attendance_action_kiosk_mode';
        this.match_id = action.match_id;
        this.team_1_name = action.team_1_name;
        this.team_2_name = action.team_2_name;
        this.match_score = action.match_score;
        this.match_points_per_set = action.match_points_per_set;
        this.match_sets_to_win = action.match_sets_to_win;
    },

    start: function () {
        var self = this;
        self.$el.html(QWeb.render("HrAttendanceMyMainMenu", {widget: self}));
        // self.$inputs = []
        var score = JSON.parse(this.match_score) || [];
        self.$el.append('<div class="row">' +
                            '<span style="text-align:center;" class="col-xs-2 col-xs-offset-3"><b>'
                                + self.team_1_name +
                            '</b></span>' +
                            '<span style="text-align:center;" class="col-xs-2 col-xs-offset-1"><b>'
                                + self.team_2_name +
                            '</b></span>'+
                        '</div>' + 
                        '<div class="match-score"></div>');
        self.$score_div = self.$el.find('div.match-score');
        // var i = 0;
        score.forEach(
            function(set) {
                // self.$inputs[i] = $('<input></input>').val(set[0].toString());
                // self.$inputs[i].val()
                self.$score_div.append(
                    '<div class="row">' +
                        '<input type="number" style="width:16.666667%;text-align:center;" class="col-xs-2 col-xs-offset-3">' +
                        '</input>' +
                        '<div class="col-xs-1"> - </div>' +
                        '<input type="number" style="width:16.666667%;text-align:center;" class="col-xs-2">' +
                        '</input>'+
                    '</div>');
            });
        var input_scores = this.$score_div.find('input')
        for (var i=0; i<input_scores.length/2; i++) {
            $(input_scores[2*i]).val(score[i][0].toString());
            $(input_scores[2*i+1]).val(score[i][1].toString());
        }
        this.evaluate_score();
        return self._super.apply(this, arguments);
    },

    evaluate_score: function () {
        var input_scores = this.$score_div.find('input')
        var player1won = 0;
        var player2won = 0;
        for (var i=0; i<input_scores.length/2; i++) {
            if($(input_scores[2*i]).val().length && ! parseInt($(input_scores[2*i+1]).val())) {
                $(input_scores[2*i+1]).val(Math.max(this.match_points_per_set, parseInt($(input_scores[2*i]).val())+2).toString());
            } else if(! parseInt($(input_scores[2*i]).val()) && $(input_scores[2*i+1]).val().length) {
                $(input_scores[2*i]).val(Math.max(this.match_points_per_set, parseInt($(input_scores[2*i+1]).val())+2).toString());
            } else 
            if (parseInt($(input_scores[2*i]).val()) < parseInt($(input_scores[2*i+1]).val())) {
                player2won++;
            } else if (parseInt($(input_scores[2*i]).val()) > parseInt($(input_scores[2*i+1]).val())) {
                player1won++;
            } else {
                return false; // error score 1 = score 2
            }
            if (Math.max(player1won, player2won) == this.match_sets_to_win && input_scores.length > 2*(i+1)) {
                this.$score_div.find('input').slice(2*(i+1)).remove();
                break;
            }
        }
        console.log('player1won ' + player1won)
        console.log('player2won ' + player2won)
        if (Math.max(player1won, player2won) < this.match_sets_to_win) {
            this.$score_div.append(
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
        return this.set_score();
    },

    set_score: function () {
        var tournament_match = new Model('tournament.match');
        var input_scores = this.$score_div.find('input')
        var score = [];
        for (var i=0; i<input_scores.length; i++) {
            if (!(i%2)) {
                score[i/2] = [parseInt($(input_scores[i]).val()), undefined];
            } else {
                score[(i-1)/2][1] = parseInt($(input_scores[i]).val());
            }
        }
        var self = this;
        tournament_match.call('set_score', [[this.match_id], JSON.stringify(score)])
        .then(function(result) {
            if (result) {
                // debugger;
                // self.destroy() // doesn't work ! :'(
            }
        });
    }
    // start_clock: function () {
    //     this.clock_start = setInterval(function() {this.$(".o_hr_attendance_clock").text(new Date().toLocaleTimeString(navigator.language, {hour: '2-digit', minute:'2-digit'}));}, 500);
    //     // First clock refresh before interval to avoid delay
    //     this.$(".o_hr_attendance_clock").text(new Date().toLocaleTimeString(navigator.language, {hour: '2-digit', minute:'2-digit'}));
    // },

    // destroy: function () {
    //     clearInterval(this.clock_start);
    //     this._super.apply(this, arguments);
    // },
});

core.action_registry.add('tournament_match_score', MatchScore);

return MatchScore;

});
