from django.shortcuts import render
from jobs_board_main.models import Job, Subscriber, Subscription
from .signals import new_subscriber

def get_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs_board_main/jobs.html', {'jobs': jobs})


def get_job(request, id):
    job = Job.objects.get(pk=id)
    return render(request, 'jobs_board_main/job.html', {'job': job})

def subscribe(request, id):
    job = Job.objects.get(pk=id)
    subscriber = Subscriber(email=request.POST['email'])
    subscriber.save()

    subscription = Subscription(user=subscriber, job=job, email=subscriber.email)
    subscription.save()

    # Add this line that sends our custom signal
    new_subscriber.send(sender=Subscription, job=job, subscriber=subscriber)

    payload = {
      'job': job,
      'email': request.POST['email']
    }
    return render(request, 'jobs_board_main/subscribed.html', {'payload': payload})