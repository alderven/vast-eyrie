import requests
import random
import string
import warnings
import datetime
import smtplib

warnings.filterwarnings('ignore')


def from_cache(key, config, timeout=None):
    try:
        return requests.get('{}{}'.format(config['SITE']['URL'], key), verify=False, timeout=timeout)
    except requests.Timeout:
        return None


def random_string():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(0, 100)))


def send_alert(msg, config):

    FROM = config['EMAIL']['Email']
    TO = get_recipients(config)
    SUBJECT = 'Оповещение об ошибке'
    TEXT = msg

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(config['EMAIL']['login'], config['EMAIL']['Password'])
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print('failed to send mail')


def get_recipients(config):

    d = datetime.datetime.now()
    if d.isoweekday() in range(config['WORKDAY']['start'], config['WORKDAY']['end']) and\
       d.hour in range(config['WORKTIME']['start'], config['WORKTIME']['end']):
        return config['EMPLOYEE']['WorkHour']
    else:
        return config['EMPLOYEE']['AfterHour']
