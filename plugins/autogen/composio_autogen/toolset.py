import hashlib
import types
import typing as t
from inspect import Signature

import autogen
from autogen.agentchat.conversable_agent import ConversableAgent

from composio.client.enums import Action, App, Tag
from composio.constants import DEFAULT_ENTITY_ID
from composio.sdk.exceptions import UserNotAuthenticatedException
from composio.sdk.shared_utils import get_signature_format_from_schema_params
from composio.tools import ComposioToolSet as BaseComposioToolSet


class ComposioToolSet(BaseComposioToolSet):
    """
    Composio toolset for autogen framework.
    """

    def __init__(
        self,
        caller: t.Optional[ConversableAgent] = None,
        executor: t.Optional[ConversableAgent] = None,
        api_key: t.Optional[str] = None,
        base_url: t.Optional[str] = None,
        entity_id: str = DEFAULT_ENTITY_ID,
    ) -> None:
        """
        Initialize composio toolset.

        :param caller: Caller agent.
        :param executor: Executor agent.
        :param api_key: Composio API key
        :param base_url: Base URL for the Composio API server
        :param entity_id: Entity ID for making function calls
        """
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            runtime="autogen",
            entity_id=entity_id,
        )
        self.caller = caller
        self.executor = executor

    def register_tools(
        self,
        tools: t.Sequence[App],
        caller: t.Optional[ConversableAgent] = None,
        executor: t.Optional[ConversableAgent] = None,
        tags: t.Optional[t.Sequence[Tag]] = None,
    ) -> None:
        """
        Register tools to the proxy agents.

        :param tools: List of tools to register.
        :param caller: Caller agent.
        :param executor: Executor agent.
        :param tags: Filter by the list of given Tags.
        """
        if isinstance(tools, App):
            tools = [tools]

        caller = caller or self.caller
        if caller is None:
            raise RuntimeError("Please provide `caller` agent")

        executor = executor or self.executor
        if executor is None:
            raise RuntimeError("Please provide `executor` agent")

        schemas = self.client.actions.get(apps=tools, tags=tags)
        for schema in schemas:
            self._register_schema_to_autogen(
                schema=schema.model_dump(
                    exclude_defaults=True,
                    exclude_none=True,
                    exclude_unset=True,
                ),
                caller=caller,
                executor=executor,
            )

    def register_actions(
        self,
        actions: t.Sequence[Action],
        caller: t.Optional[ConversableAgent] = None,
        executor: t.Optional[ConversableAgent] = None,
    ):
        """
        Register tools to the proxy agents.

        :param actions: List of tools to register.
        :param caller: Caller agent.
        :param executor: Executor agent.
        """

        caller = caller or self.caller
        if caller is None:
            raise RuntimeError("Please provide `caller` agent")

        executor = executor or self.executor
        if executor is None:
            raise RuntimeError("Please provide `executor` agent")

        schemas = self.client.actions.get(actions=actions)
        for schema in schemas:
            self._register_schema_to_autogen(
                schema=schema.model_dump(
                    exclude_defaults=True,
                    exclude_none=True,
                    exclude_unset=True,
                ),
                caller=caller,
                executor=executor,
            )

    def _process_function_name_for_registration(
        self,
        input_string: str,
        max_allowed_length: int = 64,
        num_hash_char: int = 10,
    ):
        """Process function name for proxy registration."""
        hash_hex = hashlib.sha256(input_string.encode(encoding="utf-8")).hexdigest()
        hash_chars_to_attach = hash_hex[:10]
        num_input_str_char = max_allowed_length - (num_hash_char + 1)
        input_str_to_attach = input_string[-num_input_str_char:]
        processed_name = input_str_to_attach + "_" + hash_chars_to_attach
        return processed_name

    def _register_schema_to_autogen(
        self,
        schema: t.Dict,
        caller: ConversableAgent,
        executor: ConversableAgent,
    ):
        name = schema["name"]
        appName = schema["appName"]
        description = schema["description"]

        def execute_action(**kwargs: t.Any) -> t.Dict:
            """Placeholder function for executing action."""
            return self.execute_action(
                action=Action.from_app_and_action(
                    app=appName,
                    name=name,
                ),
                params=kwargs,
                entity_id=self.entity_id,
            )

        function = types.FunctionType(
            code=execute_action.__code__,
            globals=globals(),
            name=self._process_function_name_for_registration(
                input_string=name,
            ),
            closure=execute_action.__closure__,
        )
        function.__signature__ = Signature(  # type: ignore
            parameters=get_signature_format_from_schema_params(
                schema_params=schema["parameters"],
            ),
        )
        function.__doc__ = (
            description if description else f"Action {name} from {appName}"
        )
        autogen.agentchat.register_function(
            function,
            caller=caller,
            executor=executor,
            name=self._process_function_name_for_registration(
                input_string=name,
            ),
            description=description if description else f"Action {name} from {appName}",
        )