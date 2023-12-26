﻿# --------------------------------------------------------------------------------------------

from .models import *
from .build_client import BuildClient

__all__ = [
    'AgentPoolQueue',
    'AgentSpecification',
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
    'JobReference',
    'JsonPatchOperation',
    'MinimalRetentionLease',
    'NewRetentionLease',
    'PhaseReference',
    'PipelineGeneralSettings',
    'PipelineReference',
    'ProcessParameters',
    'ProjectRetentionSetting',
    'PullRequest',
    'ReferenceLinks',
    'ReleaseReference',
    'RepositoryWebhook',
    'ResourceRef',
    'RetentionLease',
    'RetentionPolicy',
    'RetentionSetting',
    'SourceProviderAttributes',
    'SourceRepositories',
    'SourceRepository',
    'SourceRepositoryItem',
    'StageReference',
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
    'UpdateProjectRetentionSettingModel',
    'UpdateRetentionSettingModel',
    'UpdateStageParameters',
    'VariableGroup',
    'VariableGroupReference',
    'WebApiConnectedServiceRef',
    'XamlBuildControllerReference',
    'BuildClient'
]
