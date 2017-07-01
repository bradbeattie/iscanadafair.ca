#!/usr/bin/env python
import csv

with open("general-election-turnout.tsv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter="\t")
    writer.writerow([
        "Number",
        "Name",
        "Date",
        "Population",
        "Registered",
        "Ballots",
    ])

    for election in GeneralElection.objects.all():
        writer.writerow([
            election.number,
            str(election),
            election.date.isoformat(),
            election.population,
            election.registered,
            election.ballots_total,
        ])
