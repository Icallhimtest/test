odoo.define('hr_attendance.employee_kanban_view_handler', function(require) {
"use strict";

var KanbanRecord = require('web_kanban.Record');

KanbanRecord.include({
    wttttffff: function() {
        console.log('wtfff');
    },
    on_kanban_match_score_clicked: function() {
        var action = {
            type: 'ir.actions.client',
            name: 'Set Score',
            target: 'new',
            tag: 'tournament_match_score',
            match_id: this.record.id.raw_value,
            match_score: this.record.score.raw_value,
            match_points_per_set: this.record.points_per_set.raw_value,
            team_1_name: this.record.first_team_id.raw_value[1],
            team_2_name: this.record.second_team_id.raw_value[1],
            match_sets_to_win: this.record.sets_to_win.raw_value,
        };
        this.do_action(action);
    },
    events: _.defaults({
        'click .o_kanban_match_score': function(){ this.on_kanban_match_score_clicked();},
    }, KanbanRecord.prototype.events),
    // on_card_clicked: function() {
    //     if (this.model === 'tournament.match' && this.$el.parents('.o_tournament_match_kanban').length) {
    // renderElement: function () {
    //     this._super();
    //     this.setup_color_picker();
    //     this.$el.addClass('o_kanban_record');
    //     this.$el.data('record', this);
    //     if (this.$el.hasClass('oe_kanban_global_click') || this.$el.hasClass('oe_kanban_global_click_edit')) {
    //         this.$el.on('click', this.proxy('on_global_click'));
    //     }
    // },
});

});
