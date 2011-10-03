import datetime
from datetime import timedelta
from celery.task import Task, PeriodicTask
from celery.task.schedules import crontab

from twilio.rest import TwilioRestClient


from schedule.models import Event

#class Onceaday(PeriodicTask):
    
#    run_every=crontab(hour=15, minute=22)

#    def run(self, **kwargs):
#        print "task is running"

		                

            
#        return True


class FullNameTask(PeriodicTask):
    """
    A periodic task that concatenates fields to form a person's full name.
    """
    run_every = timedelta(seconds=60)#change this to run every hour

    def run(self, **kwargs):
        twilioaccount = "AC3b08da20f68fc61030d52ab1e115150e"
        twiliotoken = '2f741ba8d077a89f81d21f16f1494ade'
        client = TwilioRestClient(twilioaccount,twiliotoken)
        print "task is running"
        logger = self.get_logger(**kwargs)
        logger.info("Running full name task.")
        starttime_now = datetime.datetime(*datetime.datetime.now().timetuple()[:4])
        starthour_now=starttime_now.hour
        midnight = datetime.datetime(*datetime.datetime.now().replace(hour=23).timetuple()[:4])
        #endtime = midnight
        #Within_the_hour_events=Event.objects.filter(start__gte=starttime, start__lt=endtime)
        #for event in  Within_the_hour_events:
            #print "event is:"
            #print event	
        
        for event in Event.objects.all():
            
            oc=event.get_occurrences(start=starttime_now,end=midnight) #get occ from now until end of day
            if oc:
                lastoc=oc[-1]
                starthour_oc=lastoc.start.timetuple()[:4][3]
                if(starthour_oc==starthour_now): #if occ is within the hour
                    #print "occurence in timeslot is:"
                    #print lastoc
                    msg= "occurrence from %s to %s is %s "%(lastoc.start,lastoc.end,lastoc.title)
                    print msg
                    num=event.creator.get_profile().phone_number
                    print num
                    message = client.sms.messages.create(to="+14154980844",
                                     from_="+14152266087",
                                     body=msg)
            #this else may not be necessary
            #else:
                #if not event.occurrence_set.exists(): 
                    #=event.start.timetuple()[:4][3]
                    #print event.occurrence_set.exists()
                    #print "event has not been dragged around"        
                    #if(starthour_event==starthour_now):
                        #print "event in timeslot is:"
                        #print event
                        #print "event from %s to %s is %s "%(event.start,event.end,event.title)

            
        return True
