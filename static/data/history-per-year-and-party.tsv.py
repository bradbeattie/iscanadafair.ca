#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
import csv

def group_as_other(seats, ballots, total_ballots):
    return ballots / total_ballots < 0.02 and not seats

OTHERS = "others"

with open("history-per-year-and-party.tsv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter="\t")
    writer.writerow([
        "Date",
        "Party",
        "Shortname",
        "Longname",
        "Seats",
        "Seat %",
        "Votes",
        "Vote %",
    ])

    for election in GeneralElection.objects.all():
        print()
        print(election)
        seats = defaultdict(int)
        ballots = defaultdict(int)
        for election_riding in election.election_ridings.all():
            for election_candidate in election_riding.election_candidates.all():
                seats[election_candidate.party] += 1 if election_candidate.elected else 0
                ballots[election_candidate.party] += election_candidate.ballots or 0

        total_seats = sum(seats.values())
        total_ballots = sum(ballots.values())

        results = defaultdict(dict)
        for party in seats:
            if party:
                if group_as_other(seats[party], ballots[party], total_ballots):
                    slug = OTHERS
                    results[slug].setdefault("seats", 0)
                    results[slug].setdefault("ballots", 0)
                    results[slug]["seats"] += seats[party]
                    results[slug]["ballots"] += ballots[party]
                    results[slug]["shortname"] = "(Others)"
                    results[slug]["longname"] = "(Others)"
                else:
                    results[party.slug]["shortname"] = party.names["EN"]["Library of Parliament, Short"]
                    results[party.slug]["longname"] = party.names["EN"]["Library of Parliament, History of Federal Ridings"]
                    results[party.slug]["seats"] = seats[party]
                    results[party.slug]["ballots"] = ballots[party]

        pprint(results)
        for party_name in sorted(results.keys(), key=lambda x: -results[x]["seats"]):
            writer.writerow([
                election.date,
                party_name,
                results[party_name]["shortname"],
                results[party_name]["longname"],
                results[party_name]["seats"],
                results[party_name]["seats"] / total_seats,
                results[party_name]["ballots"],
                results[party_name]["ballots"] / total_ballots,
            ])
