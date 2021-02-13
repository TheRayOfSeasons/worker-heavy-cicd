from aws_cdk import aws_codebuild as codebuild
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as codepipeline_actions
from aws_cdk import core

from .web_app import WebApp


class WebAppPipeline(core.Stack):
    """
    A stack that defines the CI/CD pipeline of
    the front-end web application.
    """

    def __init__(
            self, scope: core.Construct, construct_id: str,
            app: WebApp, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket = app.bucket

    def _create_pipeline(self) -> codepipeline.Pipeline:
        """
        Define and apply the specifications on how
        the deployment process will go.
        """
        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()
        return codepipeline.Pipeline(
            self,
            'Pipeline',
            stages=[
                self._create_source_stage('Source', source_output),
                # self._create_image_build_stage(
                #     'Build', source_output, build_output),
                # self._create_deploy_stage('Deploy', build_output)
            ]
        )

    def _create_source_stage(
            self, stage_name: str, output: codepipeline.Artifact):
        """
        A pipeline stage that is responsible
        with fetching the application from
        GitHub.
        """
        secret_token = ''
        repo = ''
        owner = ''
        github_action = codepipeline_actions.GitHubSourceAction(
            action_name='Github_Source',
            owner=owner,
            repo=repo,
            oauth_token=secret_token,
            output=output
        )
        return {
            'stageName': stage_name,
            'actions': [github_action]
        }

