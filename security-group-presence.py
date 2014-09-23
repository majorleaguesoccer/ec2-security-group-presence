import time
import sys
import signal
import os
import boto.ec2

region = os.getenv('AWS_REGION', 'us-west-2')
presence_sg = os.getenv('SECURITY_GROUP_ID') # should be id of presence security group

print "Initializing ec2 connection"
conn = boto.ec2.connect_to_region(region)

def sighandler(signum, frame):

    # We have been terminated. Set the groups
    print 'Received signal: %s. Removing security group %s' % (signum, presence_sg)
    conn.modify_instance_attribute(instance_id, 'groupSet', sg_ids_rm)
    sys.exit()

def main(argv=None):
    global sg_ids_rm, instance_id

    signal.signal(signal.SIGTERM, sighandler) # so we can handle kill gracefully
    signal.signal(signal.SIGINT, sighandler) # so we can handle ctrl-c

    # Get host instance id
    instance_id = boto.utils.get_instance_metadata()['instance-id']

    # Find security groups that are there and calculate the union. Also
    # store the set without the target group so we can remove when exiting
    sgs = conn.get_instance_attribute(instance_id, 'groupSet')
    sg_ids_add = set([g.id for g in sgs['groupSet']]) | set([presence_sg])
    sg_ids_rm = set([g.id for g in sgs['groupSet']]) - set([presence_sg])

    # Make the call to modify the instance
    print "Adding security group %s to instance %s" % (presence_sg, instance_id)
    conn.modify_instance_attribute(instance_id, 'groupSet', sg_ids_add)

if __name__ == '__main__':
    main(sys.argv)
    while 1:  # Force main thread to live until SIG
       print "Running"
       time.sleep(100)
