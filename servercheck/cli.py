# -*- coding: utf-8 -*-
"""
This module creates the cli function that takes the input for the checkserver application
"""

import sys
import json
import click
from .http import make_req

@click.command()
@click.option("--server", "-s", default=None, help="A server/port combination", multiple=True)
@click.option("--filename", "-f", default=None, help="Read the input from a file")
def cli(server=None, filename=None):
    """
    The cli tool function
    """
    if not server and not filename:
        raise click.UsageError("Must provide json file or define servers")

    # Create a set to store all the defined servers
    servers = set()

    # Try to open and read the given file
    if filename:
        try:
            with open(filename) as f:
                file_servers = json.load(f)
                for s in file_servers:
                    servers.add(s)
        except (EnvironmentError, IOError) as err:
            print(err)
            sys.exit(1)

    # Read the defined servers
    if server:
        for s in server:
            servers.add(s)

    results = make_req(servers)

    # Print the results
    print("Successful Connections")
    print("----------------------")
    for iserver in results["success"]:
        print(iserver)
    print("\nFailed Connections")
    print("------------------")
    for iserver in results["failure"]:
        print(iserver)

if __name__ == "__main__":
    cli()
