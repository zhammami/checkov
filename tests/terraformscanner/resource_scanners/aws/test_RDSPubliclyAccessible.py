

import unittest

from checkov.terraform.models.enums import CheckResult
from checkov.terraform.checks.resource.aws.RDSPubliclyAccessible import check


class TestRDSPubliclyAccessible(unittest.TestCase):

    def test_failure(self):
        resource_conf =  {'engine': ['postgres'], 'engine_version': ['9.6.3'], 'multi_az': [False], 'backup_retention_period': [10], 'auto_minor_version_upgrade': [True], 'storage_encrypted': [False],'publicly_accessible':[True]}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILURE, scan_result)

    def test_success(self):
        resource_conf =  {'engine': ['postgres'], 'engine_version': ['9.6.3'], 'multi_az': [False], 'backup_retention_period': [10], 'auto_minor_version_upgrade': [True], 'storage_encrypted': [True]}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.SUCCESS, scan_result)


if __name__ == '__main__':
    unittest.main()