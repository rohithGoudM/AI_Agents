output = ([{'id': '192672b01b5d4f1f', 'threadId': '192672270834bd43', 'labelIds': ['UNREAD', 'IMPORTANT', 'CATEGORY_PERSONAL', 'INBOX'], 'snippet': 'Dantada, tada tada Dantada, tada tada On Mon, 7 Oct, 2024, 6:49 pm , &lt;yuvraj07102024@gmail.com&gt; wrote: ACHA CHAL TA HU DUA OH ME YAAD RAKHNA!! TA DA DA DA DADA DADA DAAAA', 'payload': {'partId': '', 'mimeType': 'multipart/alternative', 'filename': '', 'headers': [{'name': 'Delivered-To', 'value': 'yuvraj07102024@gmail.com'}, {'name': 'Received', 'value': 'by 2002:a05:6022:b14f:b0:5c:5e30:a8d9 with SMTP id z15csp1832892laa;        Mon, 7 Oct 2024 06:28:44 -0700 (PDT)'}, {'name': 'X-Received', 'value': 'by 2002:a92:c569:0:b0:39d:637f:97bc with SMTP id e9e14a558f8ab-3a3757ca174mr105410375ab.0.1728307724415;        Mon, 07 Oct 2024 06:28:44 -0700 (PDT)'}, {'name': 'ARC-Seal', 'value': 'i=1; a=rsa-sha256; t=1728307724; cv=none;        d=google.com; s=arc-20240605;        b=Y+jbuRdE9D2UTvoQgdRUSLRjsuXQHNe489jsu+HVegEqKrbttXR1/qkzqVFW1kKoHG         SYKwsYNLN3bwPqWozEVdj2R864qB7G7S3C6OR+tRl4eAz/LhCWEwBY8F68MnoR2Oy6ew         KERXPizFqFD0bOW6q3rNGlk//AGtZs5uBXHuDI04DiRkhwFMFkNv++oGRgDlUSgkqF5i         RpXTZhIz0v6bUL9ubHdneNcKheawwOIPRqFHV47XCE+r2DkfBS48PentDpD8ZNWnIdqF         JPjB0AW7zHJGnlCpZ0OKZ8BDrab9bQ2nx/MJYmfGsw2KbR5qkvcUmbMTfPCczLsnajDm         sRNw=='}, {'name': 'ARC-Message-Signature', 'value': 'i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;        h=to:subject:message-id:date:from:in-reply-to:references:mime-version         :dkim-signature;        bh=AJaVH5e9A9K5DtnJRsVilKLVvZFgOE9MCz2/fkSKniU=;        fh=c1dJMzAWEdVHHUD0FOvk+oaNKnFnFNI2xxMZ0XC3m7A=;        b=agmJTWPOIDkqclO3bkYJTGu8tc+A6YNqiG3QFvrRX5/rZisceu8LLIM78HzdzFLJs5         JtCo8cMkWfxRxOnkl9BBZNOQf7y6BKwF171NOVqdKoqWAfsnd3WeHl+mI25a6eClNnLc         zBtILr43k/bx2P9Hf+0/adEHyjACJ6SYMdCztIBbV/NQrvp6aaF9rJEYaKR/SUf8FjJW         u/hY7KDQ6N2Mue/DjkwUwl6GA7eXqzN7gRJ/3JuJzFANNSaGC54l3qhkCnLwAVo52ExQ         T9tMRGmIg8QIe4/XH/VPo9z3lERmRtIW55LYVw1JavG+xhSxXhFvx8mWXLeHQcxr6Z7F         A7qw==;        dara=google.com'}, {'name': 'ARC-Authentication-Results', 'value': 'i=1; mx.google.com;       dkim=pass header.i=@gmail.com header.s=20230601 header.b=nTDP+eGO;       spf=pass (google.com: domain of mrohithg@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=mrohithg@gmail.com;       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;       dara=pass header.i=@gmail.com'}, {'name': 'Return-Path', 'value': '<mrohithg@gmail.com>'}, {'name': 'Received', 'value': 'from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])        by mx.google.com with SMTPS id e9e14a558f8ab-3a37a7eaa48sor17566895ab.4.2024.10.07.06.28.44        for <yuvraj07102024@gmail.com>        (Google Transport Security);        Mon, 07 Oct 2024 06:28:44 -0700 (PDT)'}, {'name': 'Received-SPF', 'value': 'pass (google.com: domain of mrohithg@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;'}, {'name': 'Authentication-Results', 'value': 'mx.google.com;       dkim=pass header.i=@gmail.com header.s=20230601 header.b=nTDP+eGO;       spf=pass (google.com: domain of mrohithg@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=mrohithg@gmail.com;       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;       dara=pass header.i=@gmail.com'}, {'name': 'DKIM-Signature', 'value': 'v=1; a=rsa-sha256; c=relaxed/relaxed;        d=gmail.com; s=20230601; t=1728307723; x=1728912523; dara=google.com;        h=to:subject:message-id:date:from:in-reply-to:references:mime-version         :from:to:cc:subject:date:message-id:reply-to;        bh=AJaVH5e9A9K5DtnJRsVilKLVvZFgOE9MCz2/fkSKniU=;        b=nTDP+eGOLQb4+Ue6fgenFRm7ZKPQLRNTu1E8XM7VwgvRsfZsiqyg2VZBrkF7MaJI7K         2VYP5CUPHlbQBCZoR1qAwyvFbMTN/c0Yp27yXf39u7W/fWNhTjtAtVvaQvex71YAldYL         poklXJ4yYetGuogJTKpueEGzf6lOhibWuoabcCwBzGBUH6K0fTqaKZf5gJuYypdEk1Ln         IetQpPP3WqY36bbX+nJbmYH2m3lkSoptBW9IBIi0+Owa37sZLIij8NXT1blltB+6CW/c         JkePRZFmeIC+JA+n2KkHvi9cZ5maQbX81JtK+hfGwapQ17WJQ+nNpJ8M72dg0Y4CxQ9A         DJDQ=='}, {'name': 'X-Google-DKIM-Signature', 'value': 'v=1; a=rsa-sha256; c=relaxed/relaxed;        d=1e100.net; s=20230601; t=1728307723; x=1728912523;        h=to:subject:message-id:date:from:in-reply-to:references:mime-version         :x-gm-message-state:from:to:cc:subject:date:message-id:reply-to;        bh=AJaVH5e9A9K5DtnJRsVilKLVvZFgOE9MCz2/fkSKniU=;        b=NbE++aaAaC4/N/w3UbTv6R9zjBHxZGAWoIEBHDwmgJid73oHg2bQ55IZoR2LrXyBXG         USBYvF9dbwXCliC7IaBH0NGWaFhrzYtq7FLJ4rwuWpaYKjK4BuudX2g0AwBY5Jo+qlzc         Dn1yOJkKe1bMWjFyqiVK7j139YMJLo1KhqqyYDfIoLATlu8xAYY7NZLztKAtReS91xU4         EwAphBPcvBvLwixe/HuP0KDNJNk8IbpZcd/TKymgR7VIDFEePsnwQHC5cfbCDgAfOtSF         54+n3D5DWbAp1IY66Ie3GseiWIDpZZu4nbX6xf8BykhMllq4xfFKlGLuuOUWWGW0DZhC         FDbw=='}, {'name': 'X-Gm-Message-State', 'value': 'AOJu0Yx4ti9FdTopDNOjppjv43bGa+ajXUITcA9pZYiHAq2gXuj/5TAM bFmceAktDqg6dVL+oQSWLvMd5P59uG9tDqWwVxuakz0n+jO9sBmRVdM1BQ9gIQiJmgtILeWnxqe kSAt9Xg8WzXsTteDTZwQ9MEipkcCQK6Q='}, {'name': 'X-Google-Smtp-Source', 'value': 'AGHT+IFWxabiBm+s+/2duW9ncvaKW2oYRgdzIULiXMfh5EaSfIh0SUOEc09m9+Wtu9+fW/E7S98pEagFjde0QuhTEY4='}, {'name': 'X-Received', 'value': 'by 2002:a92:c24c:0:b0:3a3:449b:5981 with SMTP id e9e14a558f8ab-3a375be76cbmr95333245ab.26.1728307723527; Mon, 07 Oct 2024 06:28:43 -0700 (PDT)'}, {'name': 'MIME-Version', 'value': '1.0'}, {'name': 'References', 'value': '<CAC+BvBnFedBoMhpK8WVJNRBXWDAAvhY5hfiKWDPt-Rj_ZdiU5Q@mail.gmail.com>'}, {'name': 'In-Reply-To', 'value': '<CAC+BvBnFedBoMhpK8WVJNRBXWDAAvhY5hfiKWDPt-Rj_ZdiU5Q@mail.gmail.com>'}, {'name': 'From', 'value': 'M Rohith Goud <mrohithg@gmail.com>'}, {'name': 'Date', 'value': 'Mon, 7 Oct 2024 18:58:31 +0530'}, {'name': 'Message-ID', 'value': '<CAB-HA9YZcZffQSboU296KWr5D=QvH7SH8+LUWPfpGuxyC4GLkA@mail.gmail.com>'}, {'name': 'Subject', 'value': 'Re: Sent from EMAIL AUTOMATION AGENT'}, {'name': 'To', 'value': 'yuvraj07102024@gmail.com'}, {'name': 'Content-Type', 'value': 'multipart/alternative; boundary="000000000000ec6e150623e2ff23"'}], 'body': {'size': 0}, 'parts': [{'partId': '0', 'mimeType': 'text/plain', 'filename': '', 'headers': [{'name': 'Content-Type', 'value': 'text/plain; charset="UTF-8"'}, {'name': 'Content-Transfer-Encoding', 'value': 'quoted-printable'}], 'body': {'size': 190, 'data': 'RGFudGFkYSwgdGFkYSB0YWRhDQpEYW50YWRhLCB0YWRhIHRhZGENCg0KDQoNCk9uIE1vbiwgNyBPY3QsIDIwMjQsIDY6NDnigK9wbSAsIDx5dXZyYWowNzEwMjAyNEBnbWFpbC5jb20-IHdyb3RlOg0KDQo-IEFDSEEgQ0hBTCBUQSBIVSBEVUEgT0ggTUUgWUFBRCBSQUtITkEhISBUQSBEQSBEQSBEQSBEQURBIERBREEgREFBQUENCj4NCg=='}}, {'partId': '1', 'mimeType': 'text/html', 'filename': '', 'headers': [{'name': 'Content-Type', 'value': 'text/html; charset="UTF-8"'}, {'name': 'Content-Transfer-Encoding', 'value': 'quoted-printable'}], 'body': {'size': 519, 'data': 'PGRpdiBkaXI9ImF1dG8iPkRhbnRhZGEsIHRhZGEgdGFkYTxkaXYgZGlyPSJhdXRvIj5EYW50YWRhLCB0YWRhIHRhZGE8L2Rpdj48ZGl2IGRpcj0iYXV0byI-PGJyPjwvZGl2PjxkaXYgZGlyPSJhdXRvIj48YnI-PC9kaXY-PC9kaXY-PGJyPjxkaXYgY2xhc3M9ImdtYWlsX3F1b3RlIj48ZGl2IGRpcj0ibHRyIiBjbGFzcz0iZ21haWxfYXR0ciI-T24gTW9uLCA3IE9jdCwgMjAyNCwgNjo0OeKAr3BtICwgJmx0OzxhIGhyZWY9Im1haWx0bzp5dXZyYWowNzEwMjAyNEBnbWFpbC5jb20iPnl1dnJhajA3MTAyMDI0QGdtYWlsLmNvbTwvYT4mZ3Q7IHdyb3RlOjxicj48L2Rpdj48YmxvY2txdW90ZSBjbGFzcz0iZ21haWxfcXVvdGUiIHN0eWxlPSJtYXJnaW46MCAwIDAgLjhleDtib3JkZXItbGVmdDoxcHggI2NjYyBzb2xpZDtwYWRkaW5nLWxlZnQ6MWV4Ij5BQ0hBIENIQUwgVEEgSFUgRFVBIE9IIE1FIFlBQUQgUkFLSE5BISEgVEEgREEgREEgREEgREFEQSBEQURBIERBQUFBPGJyPg0KPC9ibG9ja3F1b3RlPjwvZGl2Pg0K'}}]}, 'sizeEstimate': 6301, 'historyId': '1896', 'internalDate': '1728307711000'}], [])
# for i in output[0]:
#     print(i)
#     print('\n')
#     print('\n')
#     print('\n')

import re

def process_email_data(emails):
    extracted_info = []

    for email in emails:
        # Extract email information
        email_data = {
            "id": email.get("id"),
            "threadId": email.get("threadId"),
            "labelIds": email.get("labelIds", []),
            "snippet": email.get("snippet"),
            "from": None,
            "subject": None,
            "date": None,
            "message_id": None,
            "in_reply_to": None,
            "references": None
        }

        # Extract headers from the payload
        if "payload" in email and "headers" in email["payload"]:
            for header in email["payload"]["headers"]:
                if header["name"].lower() == "from":
                    email_data["from"] = header["value"]
                elif header["name"].lower() == "subject":
                    email_data["subject"] = header["value"]
                elif header["name"].lower() == "date":
                    email_data["date"] = header["value"]
                elif header["name"].lower() == "message-id":
                    email_data["message_id"] = header["value"]
                elif header["name"].lower() == "in-reply-to":
                    email_data["in_reply_to"] = header["value"]
                elif header["name"].lower() == "references":
                    email_data["references"] = header["value"]

        # Classify the action based on email's labels and snippet content
        action = categorize_email(email_data)
        email_data["action"] = action

        extracted_info.append(email_data)

    return extracted_info

def categorize_email(email_data):
    # Categorize emails based on certain conditions (can be modified)
    if "INBOX" in email_data["labelIds"]:
        if "UNREAD" in email_data["labelIds"]:
            if re.search(r"(urgent|asap|important)", email_data["snippet"], re.I):
                return "fetch_response"
            elif re.search(r"(follow up|reminder)", email_data["snippet"], re.I):
                return "write_followup"
        else:
            if email_data["from"]:
                return "categorize"
    return "no_action"


processed_emails = process_email_data(output[0])
print(output[0])
print('\n')
print('\n')
print('\n')
print(processed_emails)
