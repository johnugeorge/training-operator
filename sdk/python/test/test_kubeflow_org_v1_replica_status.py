# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.7.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

from kubeflow.training.models import *
from kubeflow.training.models.kubeflow_org_v1_replica_status import KubeflowOrgV1ReplicaStatus  # noqa: E501
from kubeflow.training.rest import ApiException

class TestKubeflowOrgV1ReplicaStatus(unittest.TestCase):
    """KubeflowOrgV1ReplicaStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubeflowOrgV1ReplicaStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.kubeflow_org_v1_replica_status.KubeflowOrgV1ReplicaStatus()  # noqa: E501
        if include_optional :
            return KubeflowOrgV1ReplicaStatus(
                active = 56, 
                failed = 56, 
                label_selector = None, 
                selector = '0', 
                succeeded = 56
            )
        else :
            return KubeflowOrgV1ReplicaStatus(
        )

    def testKubeflowOrgV1ReplicaStatus(self):
        """Test KubeflowOrgV1ReplicaStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
