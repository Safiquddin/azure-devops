﻿# --------------------------------------------------------------------------------------------

from ...v5_1.tfvc.models import *
from .tfvc_client import TfvcClient

__all__ = [
    'AssociatedWorkItem',
    'Change',
    'CheckinNote',
    'FileContentMetadata',
    'GitRepository',
    'GitRepositoryRef',
    'GraphSubjectBase',
    'IdentityRef',
    'ItemContent',
    'ItemModel',
    'ReferenceLinks',
    'TeamProjectCollectionReference',
    'TeamProjectReference',
    'TfvcBranch',
    'TfvcBranchMapping',
    'TfvcBranchRef',
    'TfvcChange',
    'TfvcChangeset',
    'TfvcChangesetRef',
    'TfvcChangesetSearchCriteria',
    'TfvcChangesetsRequestData',
    'TfvcItem',
    'TfvcItemDescriptor',
    'TfvcItemRequestData',
    'TfvcLabel',
    'TfvcLabelRef',
    'TfvcLabelRequestData',
    'TfvcMappingFilter',
    'TfvcMergeSource',
    'TfvcPolicyFailureInfo',
    'TfvcPolicyOverrideInfo',
    'TfvcShallowBranchRef',
    'TfvcShelveset',
    'TfvcShelvesetRef',
    'TfvcShelvesetRequestData',
    'TfvcStatistics',
    'TfvcVersionDescriptor',
    'VersionControlProjectInfo',
    'VstsInfo',
    'TfvcClient'
]
