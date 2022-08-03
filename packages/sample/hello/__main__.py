from http import HTTPStatus
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# url: /hello?from=<email>&to=<email>&subject=<subject>&content=<body>
def main(args):
    key = "SG.xxx"
    user_from = args.get("from")
    user_to = args.get("to")
    user_subject = args.get("subject")
    content = args.get("content")

    sg = SendGridAPIClient(key)
    message = Mail(
        from_email = "hello@khophi.co",
        to_emails = user_to,
        subject = user_subject,
        html_content = content)
    response = sg.send(message)

    if response.status_code != 202:
        return {
            "statusCode" : response.status_code,
            "body" : "email failed to send"
        }
    return {
        "statusCode" : HTTPStatus.ACCEPTED,
        "body" : "success"
    }
