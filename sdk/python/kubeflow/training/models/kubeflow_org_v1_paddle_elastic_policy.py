# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.7.0rc0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.training.configuration import Configuration


class KubeflowOrgV1PaddleElasticPolicy(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'max_replicas': 'int',
        'max_restarts': 'int',
        'metrics': 'list[K8sIoApiAutoscalingV2MetricSpec]',
        'min_replicas': 'int'
    }

    attribute_map = {
        'max_replicas': 'maxReplicas',
        'max_restarts': 'maxRestarts',
        'metrics': 'metrics',
        'min_replicas': 'minReplicas'
    }

    def __init__(self, max_replicas=None, max_restarts=None, metrics=None, min_replicas=None, local_vars_configuration=None):  # noqa: E501
        """KubeflowOrgV1PaddleElasticPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_replicas = None
        self._max_restarts = None
        self._metrics = None
        self._min_replicas = None
        self.discriminator = None

        if max_replicas is not None:
            self.max_replicas = max_replicas
        if max_restarts is not None:
            self.max_restarts = max_restarts
        if metrics is not None:
            self.metrics = metrics
        if min_replicas is not None:
            self.min_replicas = min_replicas

    @property
    def max_replicas(self):
        """Gets the max_replicas of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501

        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas, defaults to null.  # noqa: E501

        :return: The max_replicas of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """Sets the max_replicas of this KubeflowOrgV1PaddleElasticPolicy.

        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas, defaults to null.  # noqa: E501

        :param max_replicas: The max_replicas of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501
        :type: int
        """

        self._max_replicas = max_replicas

    @property
    def max_restarts(self):
        """Gets the max_restarts of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501

        MaxRestarts is the limit for restart times of pods in elastic mode.  # noqa: E501

        :return: The max_restarts of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501
        :rtype: int
        """
        return self._max_restarts

    @max_restarts.setter
    def max_restarts(self, max_restarts):
        """Sets the max_restarts of this KubeflowOrgV1PaddleElasticPolicy.

        MaxRestarts is the limit for restart times of pods in elastic mode.  # noqa: E501

        :param max_restarts: The max_restarts of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501
        :type: int
        """

        self._max_restarts = max_restarts

    @property
    def metrics(self):
        """Gets the metrics of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501

        Metrics contains the specifications which are used to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated with multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the HPA will not be created.  # noqa: E501

        :return: The metrics of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501
        :rtype: list[K8sIoApiAutoscalingV2MetricSpec]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this KubeflowOrgV1PaddleElasticPolicy.

        Metrics contains the specifications which are used to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated with multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the HPA will not be created.  # noqa: E501

        :param metrics: The metrics of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501
        :type: list[K8sIoApiAutoscalingV2MetricSpec]
        """

        self._metrics = metrics

    @property
    def min_replicas(self):
        """Gets the min_replicas of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501

        minReplicas is the lower limit for the number of replicas to which the training job can scale down.  It defaults to null.  # noqa: E501

        :return: The min_replicas of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """Sets the min_replicas of this KubeflowOrgV1PaddleElasticPolicy.

        minReplicas is the lower limit for the number of replicas to which the training job can scale down.  It defaults to null.  # noqa: E501

        :param min_replicas: The min_replicas of this KubeflowOrgV1PaddleElasticPolicy.  # noqa: E501
        :type: int
        """

        self._min_replicas = min_replicas

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KubeflowOrgV1PaddleElasticPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubeflowOrgV1PaddleElasticPolicy):
            return True

        return self.to_dict() != other.to_dict()
