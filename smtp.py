import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas

def extractRecipients(file_path):
    try:
        data = pandas.read_excel(file_path)
        return data.values.tolist()
    except Exception as e:
        print(f"Error reading recipients from file: {e}")
        return []

def sendEmail(sender_email, password, subject, content, header, footer, recipients):
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, password)

        for student in recipients:
            name = student[2]
            last_name = student[1]
            receiver_email = student[4]
            
            # Customize the content with recipient name
            customized_content = content.replace("{name}", name)
            
            # Construct the HTML email with header, content, and footer
            html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
                
                <div style="width: 100%; background-color: #353135; padding-bottom: 10px; text-align: center; table-layout: fixed;">
                    <table width="100%" style="width: 100%; max-width: 600px; margin: 0 auto; background-color: #252425; box-shadow: 0 0 25px rgba(0, 0, 0, 0.15);">
                        <tr>
                            <td height="8" style="background-color: #000;"></td>
                        </tr>
                        <tr>
                            <td>
                                <header style="text-align: center;"><img src="{header}" alt="" style="max-width: 100%;"></header>
                            </td>
                        </tr>
                            <td>
                                <table width="100%" style="padding: 20px;">
                                    <tr>
                                        <td style="color: white;">
                                            {customized_content}
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        <tr>
                            <td>
                                <footer style="text-align: center;"><img src="{footer}" alt="" style="max-width: 100%;"></footer>
                            </td>
                        </tr>
                    </table>
                </div>

            </body>
            </html>
            """
            
            # Create the MIMEText object with HTML content
            message = MIMEMultipart()
            message.attach(MIMEText(html, "html"))
            message["Subject"] = subject
            message["From"] = sender_email
            message["To"] = receiver_email
            
            # Send the email
            smtp_server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"email sent {name}")

        smtp_server.quit()
        print("Emails sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending emails: {e}")

