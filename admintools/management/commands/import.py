from django.core.management.base import BaseCommand
from ...importers.people import person_issues
from ...importers.orgs import orgs_issues
from ...importers.vote_events import vote_event_issues


class Command(BaseCommand):
    help = 'Import Data Quality Issues into DB'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('all', nargs='+', type=str)

        # Optional arguments
        parser.add_argument(
            '--people',
            action='store_true',
            dest='people',
            default=False,
            help='import Person Related Issues',
        )

        parser.add_argument(
            '--orgs',
            action='store_true',
            dest='organization',
            default=False,
            help='import Organization Related Issues',
        )

        parser.add_argument(
            '--vote_events',
            action='store_true',
            dest='vote_event',
            default=False,
            help='import Vote Event Related Issues',
        )

    def handle(self, *args, **options):
        if options['people']:
            person_issues()
            self.stdout.write(self.style.SUCCESS('Successfully Imported People'
                                                 ' DataQualityIssues into DB'))

        if options['organization']:
            orgs_issues()
            self.stdout.write(self.style.SUCCESS('Successfully Imported Organization'
                                                 ' DataQualityIssues into DB'))

        if options['vote_event']:
            vote_event_issues()
            self.stdout.write(self.style.SUCCESS('Successfully Imported VoteEvent'
                                                 ' DataQualityIssues into DB'))