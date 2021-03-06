"""
The Sims 4 Community Library is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) COLONOLNUTTY
"""
from sims4communitylib.enums.enumtypes.int_enum import CommonEnumIntBase
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.testing.common_assertion_utils import CommonAssertionUtils
from sims4communitylib.testing.common_test_service import CommonTestService


# noinspection PyMissingOrEmptyDocstring
class TestEnum(CommonEnumIntBase):
    TEST_VALUE_ONE = 1
    TEST_VALUE_TWO = 2
    TEST_VALUE_THREE = 3


# noinspection PyMissingOrEmptyDocstring
@CommonTestService.test_class(ModInfo.get_identity())
class CommonIntEnumTests:
    @staticmethod
    @CommonTestService.test(TestEnum.TEST_VALUE_ONE, 1)
    @CommonTestService.test(TestEnum.TEST_VALUE_TWO, 2)
    @CommonTestService.test(TestEnum.TEST_VALUE_THREE, 3)
    def _enum_should_convert_int_properly(enum_val, expected_value) -> None:
        CommonAssertionUtils.are_equal(int(enum_val), expected_value)
