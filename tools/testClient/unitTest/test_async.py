# Copyright 2012 Citrix Systems, Inc. Licensed under the
# Apache License, Version 2.0 (the "License"); you may not use this
# file except in compliance with the License.  Citrix Systems, Inc.
# reserves all rights not expressly granted by the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# Automatically generated by addcopyright.py at 04/03/2012
from cloudstackAPI import *
import cloudstackException
import cloudstackTestClient
import sys
import uuid
    
class jobs():
    def __init__(self, zoneId):
        self.zoneId = zoneId
        
    def run(self):
        try:
            cmd = destroyVirtualMachine.destroyVirtualMachineCmd()
            cmd.id = 4
            self.apiClient.destroyVirtualMachine(cmd)
        except cloudstackException.cloudstackAPIException, e:
            print str(e)
        except :
            print sys.exc_info()

if __name__ == "__main__":
    ''' to logging the testclient
    logger = logging.getLogger("test_async")
    fh = logging.FileHandler("test.log")
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    testclient = cloudstackTestClient.cloudstackTestClient(mgtSvr="localhost", logging=logger)
    '''
    testclient = cloudstackTestClient.cloudstackTestClient(mgtSvr="localhost", port=8080, apiKey="rUJI62HcbyhAXpRgqERZHXlrJz9GiC55fmAm7j4WobLUTFkJyupBm87sbMki1-aRFox7TDs436xYvNW9fTHcew", securityKey="2_SIz9HULx5guCLypSoRoePCBFnTZGIrA3gQ0qhy__oca6dDacJwibMSQh-kVeJivJHeA55AwJZPJAu4U3V5KQ")
    testclient.dbConfigure()
    api = testclient.getApiClient()
    '''
    testclient.submitJob(jobs(1), 10, 10, 1)
    
    js = []
    for i in range(10):
        js.append(jobs(1))
        
    testclient.submitJobs(js, 10, 1)
    '''
    cmds = []
    for i in range(20):
        cmd = deployVirtualMachine.deployVirtualMachineCmd()
        cmd.zoneid =1
        cmd.templateid = 10
        cmd.serviceofferingid = 16
        cmd.displayname = str(uuid.uuid4())
        cmds.append(cmd)
    
    asyncJobResult = testclient.submitCmdsAndWait(cmds, 6)
    
    for jobStatus in asyncJobResult:
        if jobStatus.status:
            print jobStatus.result[0].id, jobStatus.result[0].templatename, jobStatus.startTime, jobStatus.endTime
        else:
            print jobStatus.result, jobStatus.startTime, jobStatus.endTime
            
        print jobStatus.duration
