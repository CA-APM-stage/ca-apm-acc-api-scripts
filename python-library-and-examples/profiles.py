#!/usr/bin/env python

from __future__ import print_function

import pyacc


class App(pyacc.AccCommandLineApp):
    """
    List IntroscopeAgent profile fragments associated with bundles
    """
    def build_arg_parser(self):
        """
        Add some more args to the standard set
        """
        super(App, self).build_arg_parser()
        self.parser.add_argument('bundle_ids', metavar='BUNDLE_ID', nargs='*', type=str,
                                 help='Query the given bundle ids')

    def main(self):

        if self.args.bundle_ids:
            # Create a list of Bundle objects initialized with the bundle id.
            # The data will be fetched from the Config Server when the object
            # is queried (e.g. "bundle["xxx"])
            bundles = self.acc.bundles_many(self.args.bundle_ids)
        else:
            # This will fetch all agents (a page a time)
            bundles = self.acc.bundles()

        for bundle in bundles:

            # Print the bundle details
            # bundle["id"]
            # print("Bundle:", bundle)

            p = pyacc.Profile(self.acc, bundle.item_id)

            props = p["properties"]

            if props:
                # print(bundle)
                print("# BUNDLE:", bundle.item_id)
                for prop in props:
                    # print(prop)
                    print("#", prop["description"])
                    print("%s=%s" % (prop["name"], prop["value"]))

if __name__ == "__main__":
    App().run()
