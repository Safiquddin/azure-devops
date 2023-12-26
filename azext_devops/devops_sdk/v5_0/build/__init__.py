﻿# --------------------------------------------------------------------------------------------

from .models import *
from .build_client import BuildClient

__all__ = [
    'AgentPoolQueue',
    'AggregatedResultsAnalysis',
    'AggregatedResultsByOutcome',
    'AggregatedResultsDifference',
    'AggregatedRunsByOutcome',
    'AggregatedRunsByState',
    'ArtifactResource',
    'AssociatedWorkItem',
    'Attachment',
    'AuthorizationHeader',
    'Build',
    'BuildArtifact',
    'BuildBadge',
    'BuildController',
    'BuildDefinition',
    'BuildDefinition3_2',
    'BuildDefinitionReference',
    'BuildDefinitionReference3_2',
    'BuildDefinitionRevision',
    'BuildDefinitionStep',
    'BuildDefinitionTemplate',
    'BuildDefinitionTemplate3_2',
    'BuildDefinitionVariable',
    'BuildLog',
    'BuildLogReference',
    'BuildMetric',
    'BuildOption',
    'BuildOptionDefinition',
    'BuildOptionDefinitionReference',
    'BuildOptionGroupDefinition',
    'BuildOptionInputDefinition',
    'BuildReportMetadata',
    'BuildRepository',
    'BuildRequestValidationResult',
    'BuildResourceUsage',
    'BuildSettings',
    'Change',
    'DataSourceBindingBase',
    'DefinitionReference',
    'DefinitionResourceReference',
    'Deployment',
    'Folder',
    'GraphSubjectBase',
    'IdentityRef',
    'Issue',
    'JsonPatchOperation',
    'ProcessParameters',
    'PullRequest',
    'ReferenceLinks',
    'ReleaseReference',
    'RepositoryWebhook',
    'ResourceRef',
    'RetentionPolicy',
    'SourceProviderAttributes',
    'SourceRepositories',
    'SourceRepository',
    'SourceRepositoryItem',
    'SupportedTrigger',
    'TaskAgentPoolReference',
    'TaskDefinitionReference',
    'TaskInputDefinitionBase',
    'TaskInputValidation',
    'TaskOrchestrationPlanReference',
    'TaskReference',
    'TaskSourceDefinitionBase',
    'TeamProjectReference',
    'TestResultsContext',
    'Timeline',
    'TimelineAttempt',
    'TimelineRecord',
    'TimelineReference',
    'VariableGroup',
    'VariableGroupReference',
    'WebApiConnectedServiceRef',
    'XamlBuildControllerReference',
    'BuildClient'
]
