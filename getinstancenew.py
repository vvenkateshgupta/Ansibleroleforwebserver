import boto.ec2
import json
import pprint

def get_hosts(ec2,fk,fv):
    hosts = []
    print fv
    print fk
    f={fk:fv}
    print f
    ec2.get_all_instances()
    #reservations = ec2.get_all_instances(filters={'tag:Name': 'awsecsec'})
    reservations = ec2.get_all_instances(filters=f)
    for res in reservations:
        for inst in res.instances:
            if inst.ip_address:
                if inst.state == 'running':
                    #print inst.private_ip_address
                    print 'awsecsec :',inst.ip_address
                    #hosts.append(inst.ip_address)

                    hosts.append(inst.ip_address)
    return hosts    

def main():
    ec2 = boto.ec2.connect_to_region("us-east-1")
    cloudf_group = get_hosts(ec2,"tag:Name","awsecsec")
    print "awsecec:" ,cloudf_group
    all_groups={
                'awsecsec': {
                        'hosts': cloudf_group,
                        'vars': {
                                'group_name': 'aws'
                                }                            
                }
    }
      
    #pprint.pprint (all_groups)
    print json.dumps(all_groups)

if __name__=="__main__":
    main()


