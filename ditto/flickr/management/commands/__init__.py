from django.core.management.base import CommandError

from ....core.management.commands import DittoBaseCommand


class FetchCommand(DittoBaseCommand):
    """
    Parent for all classes that fetch some things from Flickr. Photos,
    Photosets, Files, etc.
    """

    def add_arguments(self, parser):
        "All children will have the --account option."
        super().add_arguments(parser)

        parser.add_argument(
            "--account",
            action="store",
            default=False,
            help=(
                "The NSID of the Flickr User associated with the one "
                "Account to fetch for."
            ),
        )


class FetchPhotosCommand(FetchCommand):

    # What we're fetching:
    singular_noun = "Photo"
    plural_noun = "Photos"

    # Child classes should supply some help text for the --days and --start/--end arguments:
    days_help = ""
    range_help = ""

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--days", action="store", default=False, help=self.days_help
        )

        parser.add_argument(
            "--start", action="store", default=False, help=self.range_help
        )
        parser.add_argument(
            "--end", action="store", default=False, help=self.range_help
        )

    def handle(self, *args, **options):

        # We might be fetching for a specific account or all (None).
        nsid = options["account"] if options["account"] else None

        if options["days"] and (options["start"] or options["end"]):
            raise CommandError("You can't use --days with --start or --end")

        if options["days"]:
            # Will be either 'all' or a number; make the number an int.
            if options["days"].isdigit():
                options["days"] = int(options["days"])
            elif options["days"] != "all":
                raise CommandError("--days should be an integer or 'all'.")

            results = self.fetch_photos(nsid, options["days"], start=None, end=None)
            self.output_results(results, options.get("verbosity", 1))
        elif options["start"] or options["end"]:
            results = self.fetch_photos(
                nsid, options["days"], options["start"], options["end"]
            )
            self.output_results(results, options.get("verbosity", 1))
        elif options["account"]:
            raise CommandError("Specify --days as well as --account.")
        else:
            raise CommandError("Specify --days , eg --days=3 or --days=all.")

    def fetch_photos(self, nsid, days, start, end):
        """Child classes should override this method to call a method that
        fetches photos and returns results, eg:
            return RecentPhotosMultiAccountFetcher(nsid=nsid).fetch(days=days)
        """
        return {}
