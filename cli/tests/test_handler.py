import os
import boto3

# prepare environment before importing main
region = boto3.session.Session().region_name
account = boto3.client("sts").get_caller_identity().get("Account")
os.environ["TOPIC_ARN_BUILD_STATUS_CHANGE"] = "arn:aws:sns:" + region + ":" + account + ":build_status_change"

import main

event = {u'Records': [{u'EventVersion': u'1.0',
                       u'EventSubscriptionArn': u'arn:aws:sns:us-west-2:000000000000:build_scheduled:00000000-0000-0000-0000-000000000000',
                       u'EventSource': u'aws:sns',
                       u'Sns': {u'SignatureVersion': u'1', u'Timestamp': u'2017-04-10T05:12:56.297Z',
                                u'Signature': u'xxx',
                                u'SigningCertUrl': u'xxx',
                                u'MessageId': u'0000000000000-0000-0000-000000000000', u'Message': u'abc',
                                u'MessageAttributes': {
                                    u'AWS.SNS.MOBILE.MPNS.NotificationClass': {u'Type': u'String',
                                                                               u'Value': u'realtime'},
                                    u'AWS.SNS.MOBILE.WNS.Type': {u'Type': u'String', u'Value': u'wns/badge'},
                                    u'AWS.SNS.MOBILE.MPNS.Type': {u'Type': u'String', u'Value': u'token'}},
                                u'Type': u'Notification',
                                u'UnsubscribeUrl': u'xxx',
                                u'TopicArn': u'arn:aws:sns:us-west-2:000000000000:build_scheduled', u'Subject': None}}]}


def test_builder():
    main.handler(event, None)