from django.shortcuts import render
import openpyxl
import africastalking


def index(request):
    if "GET" == request.method:
        return render(request, 'smssender/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_file)

        # getting all sheets
        sheets = wb.sheetnames
        print(sheets)

        # getting a particular sheet
        worksheet = wb["Sheet1"]
        print(worksheet)

        # reading a cell
        # print(worksheet["A1"].value)
        # print(worksheet["B1"].value)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
                # print(cell.value)
            excel_data.append(row_data)
            print(row_data[0])
            print(row_data[1])
            print(type(row_data[0]))
            print(type(row_data[1]))
            print(row_data)

            name = (row_data[0])
            phone = (row_data[1])

            # sending the messages
            username = "testjoe"
            apikey = "06d9a470c343c22736180a35024919857798173f77c6629447344398a21495ca"

            # Initialize the SDK
            africastalking.initialize(username, apikey)

            # Get SMS service
            sms = africastalking.SMS

            # Define some options to send the SMS
            recipients = [phone]
            message = f'Hey {name}, and am all cool all day and all night'
            # sender = '33334'

            # Send the SMS
            try:
                # Once this is done, that's it! We'll handle the rest
                response = sms.send(message, recipients)
                print(response)
            except Exception as e:
                print(f"yoh bad ass nigger, we have a problem {e}")

        return render(request, 'smssender/index.html', {"excel_data": excel_data})
