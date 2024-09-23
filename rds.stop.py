import os
import os.path
import sys

envLambdaTaskRoot = os.environ.get("LAMBDA_TASK_ROOT", None)
if envLambdaTaskRoot:
    sys.path.insert(0, envLambdaTaskRoot + "/NewBotoVersion")

import boto3

# GET RDS Instance Lists
def get_rds_instanceslists():
    print("Lambda Parameter:RDS_instances : " + os.environ['RDS_instances'])
    InstancesLists = []
    InstancesLists = os.environ['RDS_instances'].split(',')
    return InstancesLists

# STOP RDS Instances
def stop_rds_Instance(Instanceidentifier):
    RDSClient = boto3.client('rds')
    print("RDS is going to be stopped: " + Instanceidentifier)
    try:
        response = RDSClient.stop_db_instance(DBInstanceIdentifier=Instanceidentifier)
    except Exception as e:
        print('Error! stop_rds_Instance:stop_db_instance: ' + str(e))

# Handler
def lambda_handler(event, context):
    # RDS instance
    RDSInstanceLists = get_rds_instanceslists()
    if len(RDSInstanceLists) > 0:
        for RDSInstance in RDSInstanceLists:
            try:
                stop_rds_Instance(str(RDSInstance))
                print('stop: ' + str(RDSInstance))
            except Exception as e:
                print('Error! lambda_handler:stop_rds_Instance: ' + str(e))
