import csv

def load_data_from_csv(csv_file):
    data = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def schedule_email(time_to_send, email_data):
    # Logic to schedule email, possibly using Celery or an in-memory scheduler
    pass
