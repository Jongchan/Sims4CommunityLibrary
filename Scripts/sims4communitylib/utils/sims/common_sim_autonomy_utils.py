from autonomy.settings import AutonomyState
from sims.sim_info import SimInfo
from sims4communitylib.enums.types.component_types import CommonComponentType
from sims4communitylib.utils.common_component_utils import CommonComponentUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils


class CommonSimAutonomyUtils:
    """ Utilities for manipulating the autonomy of Sims. """

    @staticmethod
    def get_autonomy_state(sim_info: SimInfo) -> AutonomyState:
        """get_autonomy_state_setting(sim_info)

        Retrieve the current autonomy state of a Sim.

        :param sim_info: An instance of a Sim.
        :type sim_info: SimInfo
        """
        from autonomy.autonomy_component import AutonomyComponent
        sim = CommonSimUtils.get_sim_instance(sim_info)
        if sim is None:
            return AutonomyState.UNDEFINED
        autonomy_component: AutonomyComponent = CommonComponentUtils.get_component(sim, CommonComponentType.AUTONOMY)
        if autonomy_component is None or not hasattr(autonomy_component, 'get_autonomy_state_setting'):
            return AutonomyState.UNDEFINED
        return autonomy_component.get_autonomy_state_setting()

    @staticmethod
    def has_disabled_autonomy(sim_info: SimInfo) -> bool:
        """has_disabled_autonomy(sim_info)

        Determine if the autonomy state of a Sim is set to Disabled.

        :param sim_info: An instance of a Sim.
        :type sim_info: SimInfo
        :return: True, if the autonomy state of the Sim is set to Disabled. False, if not.
        :rtype: bool
        """
        return CommonSimAutonomyUtils.has_autonomy_state(sim_info, AutonomyState.DISABLED)

    @staticmethod
    def has_limited_autonomy(sim_info: SimInfo) -> bool:
        """has_limited_autonomy(sim_info)

        Determine if the autonomy state of a Sim is set to Limited Only.

        :param sim_info: An instance of a Sim.
        :type sim_info: SimInfo
        :return: True, if the autonomy state of the Sim is set to Limited Only. False, if not.
        :rtype: bool
        """
        return CommonSimAutonomyUtils.has_autonomy_state(sim_info, AutonomyState.LIMITED_ONLY)

    @staticmethod
    def has_medium_autonomy(sim_info: SimInfo) -> bool:
        """has_medium_autonomy(sim_info)

        Determine if the autonomy state of a Sim is set to Medium.

        :param sim_info: An instance of a Sim.
        :type sim_info: SimInfo
        :return: True, if the autonomy state of the Sim is set to Medium. False, if not.
        :rtype: bool
        """
        return CommonSimAutonomyUtils.has_autonomy_state(sim_info, AutonomyState.MEDIUM)

    @staticmethod
    def has_full_autonomy(sim_info: SimInfo) -> bool:
        """has_full_autonomy(sim_info)

        Determine if the autonomy state of a Sim is set to Full.

        :param sim_info: An instance of a Sim.
        :type sim_info: SimInfo
        :return: True, if the autonomy state of the Sim is set to Full. False, if not.
        :rtype: bool
        """
        return CommonSimAutonomyUtils.has_autonomy_state(sim_info, AutonomyState.FULL)

    @staticmethod
    def has_autonomy_state(sim_info: SimInfo, autonomy_state: AutonomyState) -> bool:
        """has_autonomy_state(sim_info, autonomy_state)

        Determine if the autonomy state of a Sim matches an autonomy state.

        :param sim_info: An instance of a Sim.
        :type sim_info: SimInfo
        :param autonomy_state: An autonomy state.
        :type autonomy_state: AutonomyState
        :return: True, if the autonomy state of the Sim matches the specified autonomy state. False, if not.
        :rtype: bool
        """
        return CommonSimAutonomyUtils.get_autonomy_state(sim_info) == autonomy_state