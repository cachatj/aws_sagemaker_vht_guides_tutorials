#!/usr/bin/env python3
import os
from aws_cdk import Aspects
import aws_cdk as cdk
import cdk_nag

from patientdiagnosisflow.patientdiagnosisflow_stack import PatientDiagnosisSummaryStack

# Create the CDK app
app = cdk.App()

# Add a tag to the app for the project name
cdk.Tags.of(app).add("Project Name", "Guidance for identifying medical conditions and diagnosis ICD-10 codes from clinical notes on AWS")
Aspects.of(app).add(cdk_nag.AwsSolutionsChecks( verbose=True ))

# Create an instance of the PatientDiagnosisSummaryStack
PatientDiagnosisSummaryStack(app, "PatientDiagnosisSummaryStack")

# Synthesize the CloudFormation template
app.synth()