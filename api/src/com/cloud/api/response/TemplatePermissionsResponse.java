// Copyright 2012 Citrix Systems, Inc. Licensed under the
// Apache License, Version 2.0 (the "License"); you may not use this
// file except in compliance with the License.  Citrix Systems, Inc.
// reserves all rights not expressly granted by the License.
// You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// 
// Automatically generated by addcopyright.py at 04/03/2012
package com.cloud.api.response;

import java.util.List;

import com.cloud.api.ApiConstants;
import com.cloud.utils.IdentityProxy;
import com.cloud.serializer.Param;
import com.google.gson.annotations.SerializedName;

@SuppressWarnings("unused")
public class TemplatePermissionsResponse extends BaseResponse {
    @SerializedName(ApiConstants.ID) @Param(description="the template ID")
    private IdentityProxy id = new IdentityProxy("vm_template");

    @SerializedName(ApiConstants.IS_PUBLIC) @Param(description="true if this template is a public template, false otherwise")
    private Boolean publicTemplate;

    @SerializedName(ApiConstants.DOMAIN_ID) @Param(description="the ID of the domain to which the template belongs")
    private IdentityProxy domainId = new IdentityProxy("domain");

    @SerializedName(ApiConstants.ACCOUNT) @Param(description="the list of accounts the template is available for")
    private List<String> accountNames;
    
    @SerializedName(ApiConstants.PROJECT_IDS) @Param(description="the list of projects the template is available for")
    private List<String> projectIds;
    

    public void setId(Long id) {
        this.id.setValue(id);
    }

    public void setPublicTemplate(Boolean publicTemplate) {
        this.publicTemplate = publicTemplate;
    }

    public void setDomainId(Long domainId) {
        this.domainId.setValue(domainId);
    }

    public void setAccountNames(List<String> accountNames) {
        this.accountNames = accountNames;
    }

    public void setProjectIds(List<String> projectIds) {
        this.projectIds = projectIds;
    }
}
