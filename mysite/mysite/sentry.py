import os
import sentry_sdk


def sentry_init():
    try:
        from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
        from sentry_sdk.integrations.boto3 import Boto3Integration
        from sentry_sdk.integrations.django import DjangoIntegration
    except ModuleNotFoundError as exc:
        print('Unable to find module', exc)
        return

    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_DSN"),
        environment="dev",
        integrations=[
            AwsLambdaIntegration(),
            Boto3Integration(),
            DjangoIntegration(),
        ],
        send_default_pii=False,
        traces_sample_rate=1.0,
        debug=True,
        # event_scrubber=EventScrubber(denylist=denylist),
        # before_send=strip_sensitive_data,
        # before_send_transaction=filter_transactions,
        # traces_sampler=traces_sampler,
    )