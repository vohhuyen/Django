from celery import shared_task

@shared_task
def clear_tokens():
    print("Clearing expired tokens...")
