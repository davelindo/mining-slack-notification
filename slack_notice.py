import urllib2
import os
import json

slack_webhook = os.environ['SLACK_WEBHOOK']


def slack_notification(slack_webhook, message):
    slack_data = {'text': message}
    request = urllib2.Request(slack_webhook)
    request.add_header('Content-type', 'application/json')
    try:
        response = urllib2.urlopen(request, json.dumps(slack_data))
    except:
        print "Failed to connect to slack!"


def build_message():
    message = """Instance %s started Mining""" % (
        os.popen("curl -s http://169.254.169.254/latest/meta-data/instance-id").read())
    return message


def main(event, context):
    slack_notification(slack_webhook, build_message())

if __name__ == '__main__':
    main('blah', 'blah')
