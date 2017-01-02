function per (value) {
    return (Math.round(value * 10) / 10).toFixed(1);
}

new Vue({
    el: '#app',
    data: {
        examples: [
            {"title": "42nd Canadian Parliament", "parties": [
                {"name": "Liberal", seats: 184, votes: 6943276},
                {"name": "Conservative", seats: 99, votes: 5613614},
                {"name": "New Democrat", seats: 44, votes: 3470350},
                {"name": "Bloc Québécois", seats: 10, votes: 821144},
                {"name": "Green", seats: 1, votes: 602944},
            ]},
        ],
        selectedExample: null,
        totalSeats: 0,
        totalVotes: 0,
        diffSquaredSum: 0,
        gallagherIndex: 0,
    },
    methods: {
        recomputeTotals: function() {
            var v = this;
            v.totalVotes = v.selectedExample.parties.reduce(function(total, party) {
                return total + party.votes;
            }, 0);
            v.totalSeats = v.selectedExample.parties.reduce(function(total, party) {
                return total + party.seats;
            }, 0);
            v.selectedExample.parties.forEach(function(party) {
                party.seatPercentage = 100 * party.seats / v.totalSeats;
                party.votePercentage = 100 * party.votes / v.totalVotes;
                party.difference = party.votePercentage - party.seatPercentage;
            }, 0);
            v.diffSquaredSum = v.selectedExample.parties.reduce(function(total, party) {
                return total + Math.pow(party.difference, 2)
            }, 0);
            v.gallagherIndex = per(Math.pow(v.diffSquaredSum / 2, 0.5));
        }
    },
    created: function() {
        this.selectedExample = this.examples[0];
        this.recomputeTotals();
    },
    watch: {
        examples: {
            handler: function() { this.recomputeTotals() },
            deep: true
        }
    }
})
