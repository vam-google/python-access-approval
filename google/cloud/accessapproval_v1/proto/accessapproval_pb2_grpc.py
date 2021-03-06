# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!

import grpc

from google.cloud.accessapproval_v1.proto import (
    accessapproval_pb2 as google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AccessApprovalStub(object):
    """This API allows a customer to manage accesses to cloud resources by
  Google personnel. It defines the following resource model:

  - The API has a collection of
  [ApprovalRequest][google.cloud.accessapproval.v1.ApprovalRequest]
  resources, named `approvalRequests/{approval_request_id}`
  - The API has top-level settings per Project/Folder/Organization, named
  `accessApprovalSettings`

  The service also periodically emails a list of recipients, defined at the
  Project/Folder/Organization level in the accessApprovalSettings, when there
  is a pending ApprovalRequest for them to act on. The ApprovalRequests can
  also optionally be published to a Cloud Pub/Sub topic owned by the customer
  (for Beta, the Pub/Sub setup is managed manually).

  ApprovalRequests can be approved or dismissed. Google personel can only
  access the indicated resource or resources if the request is approved
  (subject to some exclusions:
  https://cloud.google.com/access-approval/docs/overview#exclusions).

  Note: Using Access Approval functionality will mean that Google may not be
  able to meet the SLAs for your chosen products, as any support response times
  may be dramatically increased. As such the SLAs do not apply to any service
  disruption to the extent impacted by Customer's use of Access Approval. Do
  not enable Access Approval for projects where you may require high service
  availability and rapid response by Google Cloud Support.

  After a request is approved or dismissed, no further action may be taken on
  it. Requests with the requested_expiration in the past or with no activity
  for 14 days are considered dismissed. When an approval expires, the request
  is considered dismissed.

  If a request is not approved or dismissed, we call it pending.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.ListApprovalRequests = channel.unary_unary(
            "/google.cloud.accessapproval.v1.AccessApproval/ListApprovalRequests",
            request_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ListApprovalRequestsMessage.SerializeToString,
            response_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ListApprovalRequestsResponse.FromString,
        )
        self.GetApprovalRequest = channel.unary_unary(
            "/google.cloud.accessapproval.v1.AccessApproval/GetApprovalRequest",
            request_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.GetApprovalRequestMessage.SerializeToString,
            response_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ApprovalRequest.FromString,
        )
        self.ApproveApprovalRequest = channel.unary_unary(
            "/google.cloud.accessapproval.v1.AccessApproval/ApproveApprovalRequest",
            request_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ApproveApprovalRequestMessage.SerializeToString,
            response_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ApprovalRequest.FromString,
        )
        self.DismissApprovalRequest = channel.unary_unary(
            "/google.cloud.accessapproval.v1.AccessApproval/DismissApprovalRequest",
            request_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.DismissApprovalRequestMessage.SerializeToString,
            response_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ApprovalRequest.FromString,
        )
        self.GetAccessApprovalSettings = channel.unary_unary(
            "/google.cloud.accessapproval.v1.AccessApproval/GetAccessApprovalSettings",
            request_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.GetAccessApprovalSettingsMessage.SerializeToString,
            response_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.AccessApprovalSettings.FromString,
        )
        self.UpdateAccessApprovalSettings = channel.unary_unary(
            "/google.cloud.accessapproval.v1.AccessApproval/UpdateAccessApprovalSettings",
            request_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.UpdateAccessApprovalSettingsMessage.SerializeToString,
            response_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.AccessApprovalSettings.FromString,
        )
        self.DeleteAccessApprovalSettings = channel.unary_unary(
            "/google.cloud.accessapproval.v1.AccessApproval/DeleteAccessApprovalSettings",
            request_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.DeleteAccessApprovalSettingsMessage.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class AccessApprovalServicer(object):
    """This API allows a customer to manage accesses to cloud resources by
  Google personnel. It defines the following resource model:

  - The API has a collection of
  [ApprovalRequest][google.cloud.accessapproval.v1.ApprovalRequest]
  resources, named `approvalRequests/{approval_request_id}`
  - The API has top-level settings per Project/Folder/Organization, named
  `accessApprovalSettings`

  The service also periodically emails a list of recipients, defined at the
  Project/Folder/Organization level in the accessApprovalSettings, when there
  is a pending ApprovalRequest for them to act on. The ApprovalRequests can
  also optionally be published to a Cloud Pub/Sub topic owned by the customer
  (for Beta, the Pub/Sub setup is managed manually).

  ApprovalRequests can be approved or dismissed. Google personel can only
  access the indicated resource or resources if the request is approved
  (subject to some exclusions:
  https://cloud.google.com/access-approval/docs/overview#exclusions).

  Note: Using Access Approval functionality will mean that Google may not be
  able to meet the SLAs for your chosen products, as any support response times
  may be dramatically increased. As such the SLAs do not apply to any service
  disruption to the extent impacted by Customer's use of Access Approval. Do
  not enable Access Approval for projects where you may require high service
  availability and rapid response by Google Cloud Support.

  After a request is approved or dismissed, no further action may be taken on
  it. Requests with the requested_expiration in the past or with no activity
  for 14 days are considered dismissed. When an approval expires, the request
  is considered dismissed.

  If a request is not approved or dismissed, we call it pending.
  """

    def ListApprovalRequests(self, request, context):
        """Lists approval requests associated with a project, folder, or organization.
    Approval requests can be filtered by state (pending, active, dismissed).
    The order is reverse chronological.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetApprovalRequest(self, request, context):
        """Gets an approval request. Returns NOT_FOUND if the request does not exist.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ApproveApprovalRequest(self, request, context):
        """Approves a request and returns the updated ApprovalRequest.

    Returns NOT_FOUND if the request does not exist. Returns
    FAILED_PRECONDITION if the request exists but is not in a pending state.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DismissApprovalRequest(self, request, context):
        """Dismisses a request. Returns the updated ApprovalRequest.

    NOTE: This does not deny access to the resource if another request has been
    made and approved. It is equivalent in effect to ignoring the request
    altogether.

    Returns NOT_FOUND if the request does not exist.

    Returns FAILED_PRECONDITION if the request exists but is not in a pending
    state.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetAccessApprovalSettings(self, request, context):
        """Gets the settings associated with a project, folder, or organization.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateAccessApprovalSettings(self, request, context):
        """Updates the settings associated with a project, folder, or organization.
    Settings to update are determined by the value of field_mask.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteAccessApprovalSettings(self, request, context):
        """Deletes the settings associated with a project, folder, or organization.
    This will have the effect of disabling Access Approval for the project,
    folder, or organization, but only if all ancestors also have Access
    Approval disabled. If Access Approval is enabled at a higher level of the
    hierarchy, then Access Approval will still be enabled at this level as
    the settings are inherited.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AccessApprovalServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ListApprovalRequests": grpc.unary_unary_rpc_method_handler(
            servicer.ListApprovalRequests,
            request_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ListApprovalRequestsMessage.FromString,
            response_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ListApprovalRequestsResponse.SerializeToString,
        ),
        "GetApprovalRequest": grpc.unary_unary_rpc_method_handler(
            servicer.GetApprovalRequest,
            request_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.GetApprovalRequestMessage.FromString,
            response_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ApprovalRequest.SerializeToString,
        ),
        "ApproveApprovalRequest": grpc.unary_unary_rpc_method_handler(
            servicer.ApproveApprovalRequest,
            request_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ApproveApprovalRequestMessage.FromString,
            response_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ApprovalRequest.SerializeToString,
        ),
        "DismissApprovalRequest": grpc.unary_unary_rpc_method_handler(
            servicer.DismissApprovalRequest,
            request_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.DismissApprovalRequestMessage.FromString,
            response_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.ApprovalRequest.SerializeToString,
        ),
        "GetAccessApprovalSettings": grpc.unary_unary_rpc_method_handler(
            servicer.GetAccessApprovalSettings,
            request_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.GetAccessApprovalSettingsMessage.FromString,
            response_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.AccessApprovalSettings.SerializeToString,
        ),
        "UpdateAccessApprovalSettings": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateAccessApprovalSettings,
            request_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.UpdateAccessApprovalSettingsMessage.FromString,
            response_serializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.AccessApprovalSettings.SerializeToString,
        ),
        "DeleteAccessApprovalSettings": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteAccessApprovalSettings,
            request_deserializer=google_dot_cloud_dot_accessapproval__v1_dot_proto_dot_accessapproval__pb2.DeleteAccessApprovalSettingsMessage.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.accessapproval.v1.AccessApproval", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
