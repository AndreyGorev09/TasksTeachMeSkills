def funcmain(mail):
    mail_name, domain_name = mail.split('@')
    a = domain_name
    if a == 'gmail.com':
        return f'{mail}'
    else:
        return 'DOMAIN NAME is not supported'
